import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
REGISTRY_PATH = SCHEMAS / "common" / "component-registry.json"


def entity(category, content):
    return {
        "entity_id": f"test_{category}",
        "component_ids": ["comp_cornea"],
        "category": category,
        "nomenclature": {"en": "Test entity", "ar": "اختبار", "aliases": []},
        "content": content,
        "relationships": [],
        "metadata": {
            "keywords": ["test"],
            "references": ["wolff_anatomy"],
            "last_updated": "2026-10-15",
            "version": "1.0.0",
            "priority": 1,
        },
    }


def valid_disease():
    result = entity("disease", {
        "definition": "Test disease definition",
        "pathophysiology": "Test mechanism",
        "causes": ["cause"],
        "risk_factors": ["risk"],
        "symptoms": ["symptom"],
        "signs": ["sign"],
        "diagnosis": "Test diagnosis",
        "investigations": ["test"],
        "treatment": ["Test treatment"],
        "complications": ["complication"],
        "prevention": "Test prevention",
        "classification": ["Test type"],
        "differential_diagnosis": ["Other disease"],
        "prognosis": "Test prognosis",
        "epidemiology": "Test epidemiology",
        "imaging_findings": ["Test finding"],
        "icd10": "H34.1",
    })
    result["references"] = [
        {
            "content_field": field,
            "status": "documented",
            "sources": [{"reference_id": "wolff_anatomy", "section": "Test section"}],
        }
        for field in validate.DISEASE_CONTENT_FIELDS
    ]
    return result


def valid_physiology():
    return entity("physiology", {
        "definition": "Test physiology definition",
        "mechanism": "Test mechanism",
        "regulation": "Test regulation",
        "feedback_loop": "Test feedback loop",
        "clinical_consequence": "Test consequence",
    })


def valid_anatomy():
    result = entity("anatomy", {
        "definition": "Structure definition",
        "location": "Structure location",
        "layers": ["layer"],
        "blood_supply": "Blood supply",
        "venous_drainage": "Venous drainage",
        "innervation": None,
        "histology_summary": "Histology",
        "clinical_importance": "Clinical importance",
    })
    result["references"] = [
        {
            "content_field": field,
            "status": "not_available" if field == "innervation" else "documented",
            "sources": [] if field == "innervation" else [
                {"reference_id": "wolff_anatomy", "section": "Test section"}
            ],
        }
        for field in validate.CONTENT_FIELDS
    ]
    return result


class ComponentRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validators = validate.build_validators(SCHEMAS)
        cls.component_ids = validate.load_component_ids(REGISTRY_PATH)

    def test_registry_preserves_all_rows_and_repeated_ids(self):
        registry = validate.load(REGISTRY_PATH)
        rows = registry["rows"]
        # 37 original docx rows + 7 model-only rows appended 2026-11-06
        # (Good_Eye.blend audit: eye root + 6 cornea annotation objects)
        # + 4 DR lesion rows appended 2026-11-08 (user-reported Blender
        # objects: Microaneurysms, Haemorrhages, Soft_Exudates, Hard_Exudates)
        self.assertEqual(len(rows), 48)
        self.assertEqual(sum(row["component_id"] == "comp_cornea" for row in rows), 2)
        self.assertEqual(rows[0]["unity_name"], "cornea_inside")
        self.assertEqual(rows[0]["medical_name_en"], "Corneal Endothelium")
        self.assertEqual(rows[0]["has_3d_model"], "Yes")
        self.assertEqual(rows[0]["parent"], "—")
        self.assertEqual(rows[2]["component_id"], "—")
        self.assertEqual(rows[2]["has_3d_model"], "No (Empty Parent)")
        self.assertEqual(rows[2]["unity_name"], "eye_muscles")
        self.assertEqual(rows[36]["component_id"], "comp_vitreous")
        # appended model-only rows (Good_Eye.blend audit)
        self.assertEqual(rows[37]["unity_name"], "eye")
        self.assertEqual(rows[37]["reference_category"], "model_only")
        self.assertEqual(rows[43]["unity_name"], "Leader_Endothelium")
        # appended DR lesion rows (2026-11-08)
        self.assertEqual(rows[44]["component_id"], "comp_lesion_microaneurysms")
        self.assertEqual(rows[44]["unity_name"], "Microaneurysms")
        self.assertEqual(rows[44]["category"], "Pathology")
        self.assertEqual(rows[45]["unity_name"], "Haemorrhages")
        self.assertEqual(rows[46]["unity_name"], "Soft_Exudates")
        self.assertEqual(rows[47]["unity_name"], "Hard_Exudates")
        self.assertEqual(rows[44]["parent"], "eye_sphere_inside")
        self.assertEqual(rows[47]["parent"], "eye_sphere_inside")
        self.assertEqual(sum(row["reference_category"] == "model_only" for row in rows), 11)
        self.assertEqual(registry["model_file_findings"]["audit_date"], "2026-11-08")
        self.assertIn("comp_cornea", self.component_ids)
        self.assertNotIn("—", self.component_ids)

    def test_component_ids_distinguish_absent_empty_dash_and_unknown(self):
        cases = [
            ({}, True, []),
            ({"component_ids": []}, True, []),
            ({"component_ids": ["—"]}, True, []),
            ({"component_ids": ["unknown_component"]}, False, ["unknown_component"]),
        ]
        for value, wants_missing, wants_unknown in cases:
            with self.subTest(value=value):
                missing, unknown = validate.check_component_ids(value, self.component_ids)
                self.assertEqual(bool(missing), wants_missing)
                self.assertEqual(unknown, wants_unknown)

    def test_valid_disease_and_physiology_use_real_schemas(self):
        for record in (valid_disease(), valid_physiology()):
            with self.subTest(category=record["category"]):
                errors = validate.validate_entity(
                    record, ROOT / "fixture.json", self.validators, self.component_ids
                )
                self.assertEqual(errors, [])

    def test_invalid_disease_and_physiology_fail_real_schemas(self):
        disease = valid_disease()
        del disease["content"]["treatment"]
        physiology = valid_physiology()
        del physiology["content"]["mechanism"]
        for record, missing_field in ((disease, "treatment"), (physiology, "mechanism")):
            with self.subTest(category=record["category"]):
                errors = validate.validate_entity(
                    record, ROOT / "fixture.json", self.validators, self.component_ids
                )
                self.assertTrue(any(missing_field in error for error in errors))

    def test_disease_schema_and_validator_field_lists_agree(self):
        schema = validate.load(SCHEMAS / "diseases.schema.json")
        enum_fields = schema["properties"]["references"]["items"]["properties"][
            "content_field"
        ]["enum"]
        required = schema["properties"]["content"]["required"]
        self.assertEqual(sorted(enum_fields), sorted(validate.DISEASE_CONTENT_FIELDS))
        self.assertEqual(sorted(required), sorted(validate.DISEASE_CONTENT_FIELDS))

    def test_disease_treatment_must_be_array(self):
        record = valid_disease()
        record["content"]["treatment"] = "Old string style treatment"
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids
        )
        self.assertTrue(any("treatment" in error for error in errors))

    def test_disease_rejects_whitespace_only_values(self):
        record = valid_disease()
        record["content"]["definition"] = "   "
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids
        )
        self.assertTrue(any("definition" in error for error in errors))

        record = valid_disease()
        record["content"]["symptoms"] = ["  "]
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids
        )
        self.assertTrue(any("symptoms" in error for error in errors))

    def test_disease_status_value_linkage_rules(self):
        known_refs = validate.load_reference_ids(SCHEMAS / "common" / "references.json")

        # (a) null value + status documented -> rejected
        record = valid_disease()
        record["content"]["prevention"] = None
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids, known_refs
        )
        self.assertTrue(any(
            "'prevention' is 'documented' but its value is null" in error for error in errors
        ))

        # (b) non-null value + status not_available -> rejected
        record = valid_disease()
        for ref in record["references"]:
            if ref["content_field"] == "prognosis":
                ref["status"] = "not_available"
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids, known_refs
        )
        self.assertTrue(any(
            "'prognosis' is 'not_available' but its value is not null" in error
            for error in errors
        ))

        # (c) null value + not_applicable + empty sources -> accepted
        record = valid_disease()
        record["content"]["icd10"] = None
        for ref in record["references"]:
            if ref["content_field"] == "icd10":
                ref["status"] = "not_applicable"
                ref["sources"] = []
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids, known_refs
        )
        self.assertEqual(errors, [])

    def test_disease_documented_entry_requires_sources(self):
        record = valid_disease()
        record["references"][0]["sources"] = []
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids
        )
        self.assertTrue(any("sources" in error for error in errors))

    def test_disease_missing_reference_entry_for_a_field_fails(self):
        record = valid_disease()
        record["references"] = [
            ref for ref in record["references"] if ref["content_field"] != "signs"
        ]
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids
        )
        self.assertTrue(any("'signs' has no entry in references" in error for error in errors))

    def test_disease_duplicate_reference_entries_fail(self):
        record = valid_disease()
        record["references"].append(dict(record["references"][0]))
        errors = validate.check_disease_rules(record)
        self.assertTrue(any("duplicate reference entry for 'definition'" in error for error in errors))

    def test_disease_unknown_reference_id_fails(self):
        record = valid_disease()
        record["references"][0]["sources"][0]["reference_id"] = "ghost_book"
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids,
            validate.load_reference_ids(SCHEMAS / "common" / "references.json"),
        )
        self.assertTrue(any(
            "UNKNOWN reference_id(s)" in error and "'ghost_book'" in error
            for error in errors
        ))

    def test_disease_reference_entries_target_unknown_field_fails(self):
        record = valid_disease()
        record["references"].append({
            "content_field": "ghost_field",
            "status": "documented",
            "sources": [{"reference_id": "wolff_anatomy", "section": "s"}],
        })
        errors = validate.check_disease_rules(record)
        self.assertTrue(any(
            "unknown content field" in error and "'ghost_field'" in error
            for error in errors
        ))

    def test_disease_documented_without_sources_flagged_by_validator(self):
        record = valid_disease()
        for ref in record["references"]:
            if ref["content_field"] == "definition":
                ref["sources"] = []
        errors = validate.check_disease_rules(record)
        self.assertTrue(any(
            "'definition' is 'documented' but has no sources" in error
            for error in errors
        ))

    def test_disease_not_available_with_sources_flagged_by_validator(self):
        record = valid_disease()
        for ref in record["references"]:
            if ref["content_field"] == "prognosis":
                ref["status"] = "not_available"  # sources stay non-empty
        errors = validate.check_disease_rules(record)
        self.assertTrue(any(
            "'prognosis' is 'not_available' but its value is not null" in error
            for error in errors
        ))
        self.assertTrue(any(
            "'prognosis' is 'not_available' but has sources" in error
            for error in errors
        ))

    def test_disease_all_reference_ids_resolve(self):
        record = valid_disease()
        for ref in record["references"]:
            if ref["content_field"] in ("definition", "pathophysiology"):
                ref["sources"] = [
                    {"reference_id": "wolff_anatomy", "section": "Retina"},
                    {"reference_id": "statpearls", "section": "Introduction"},
                ]
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids,
            validate.load_reference_ids(SCHEMAS / "common" / "references.json"),
        )
        self.assertEqual(errors, [])

    def test_disease_source_requires_section_or_chapter_pages(self):
        record = valid_disease()
        record["references"][0]["sources"] = [{"reference_id": "wolff_anatomy"}]
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids
        )
        self.assertTrue(any(
            "references/0/sources" in error for error in errors
        ))

    def test_unexpected_top_level_properties_fail_real_schemas(self):
        for record in (valid_disease(), valid_physiology()):
            record["unexpected"] = True
            with self.subTest(category=record["category"]):
                errors = validate.validate_entity(
                    record, ROOT / "fixture.json", self.validators, self.component_ids
                )
                self.assertTrue(any(
                    "unevaluated" in error.lower() or "additional" in error.lower()
                    for error in errors
                ))

    def test_anatomy_reference_duplicate_missing_and_status_checks(self):
        record = valid_anatomy()
        record["references"].append(dict(record["references"][0]))
        record["references"] = [
            ref for ref in record["references"] if ref["content_field"] != "location"
        ]
        record["content"]["definition"] = None
        record["content"]["blood_supply"] = "Available text"
        by_field = {ref["content_field"]: ref for ref in record["references"]}
        by_field["blood_supply"]["status"] = "not_available"
        errors = validate.check_anatomy_rules(record)
        self.assertTrue(any("duplicate reference entry for 'definition'" in error for error in errors))
        self.assertTrue(any("'location' has no entry" in error for error in errors))
        self.assertTrue(any("'definition' is 'documented' but its value is null" in error for error in errors))
        self.assertTrue(any("'blood_supply' is 'not_available' but its value is not null" in error for error in errors))

    def test_validate_entity_handles_non_string_categories(self):
        for category in (None, 5, [], {}):
            with self.subTest(category=category):
                errors = validate.validate_entity(
                    {"category": category}, ROOT / "fixture.json",
                    self.validators, self.component_ids
                )
                self.assertTrue(any("category must be a string" in error for error in errors))

    def test_known_reference_ids_pass_real_registry(self):
        record = valid_anatomy()
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids,
            validate.load_reference_ids(SCHEMAS / "common" / "references.json"),
        )
        self.assertEqual(errors, [])

    def test_unknown_reference_ids_fail_real_registry(self):
        record = valid_anatomy()
        record["references"][0]["sources"][0]["reference_id"] = "ghost_book"
        record["metadata"]["references"] = ["wolff_anatomy", "ghost_book"]
        errors = validate.validate_entity(
            record, ROOT / "fixture.json", self.validators, self.component_ids,
            validate.load_reference_ids(SCHEMAS / "common" / "references.json"),
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("UNKNOWN reference_id(s)", errors[0])
        self.assertIn("'ghost_book'", errors[0])

    def test_main_counts_pass_fail_skip_and_reports_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            kb = Path(temp_dir)
            (kb / "valid-disease.json").write_text(json.dumps(valid_disease()), encoding="utf-8")
            (kb / "valid-physiology.json").write_text(json.dumps(valid_physiology()), encoding="utf-8")
            invalid_disease = valid_disease()
            del invalid_disease["content"]["treatment"]
            (kb / "invalid-disease.json").write_text(json.dumps(invalid_disease), encoding="utf-8")
            (kb / "invalid.json").write_text('{"category":', encoding="utf-8")
            (kb / "bad-category.json").write_text(json.dumps({"category": {"bad": True}}), encoding="utf-8")
            (kb / "unknown-category.json").write_text(json.dumps({"category": "unknown"}), encoding="utf-8")
            (kb / "missing-category.json").write_text(json.dumps({"entity_id": "no_category"}), encoding="utf-8")

            output = io.StringIO()
            with patch.object(sys, "argv", ["validate.py", str(SCHEMAS), str(kb)]):
                with contextlib.redirect_stdout(output):
                    result = validate.main()

        text = output.getvalue()
        self.assertEqual(result, 1)
        self.assertIn("2 passed, 3 failed, 2 skipped", text)
        self.assertIn("invalid.json", text)
        self.assertIn("cannot parse entity JSON", text)
        self.assertIn("bad-category.json", text)
        self.assertIn("unsupported category: 'unknown'", text)
        self.assertIn("category is missing", text)


if __name__ == "__main__":
    unittest.main()
