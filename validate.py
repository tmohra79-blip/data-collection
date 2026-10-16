"""Validate VisionAR knowledge-base entities and component mappings.

Usage:
    python validate.py <schemas_dir> <knowledge_base_dir>

Example:
    python validate.py schemas Knowledge_Base

Requires: pip install jsonschema referencing
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

CONTENT_FIELDS = [
    "definition", "location", "layers", "blood_supply",
    "venous_drainage", "innervation", "histology_summary",
    "clinical_importance",
]

SCHEMA_FILES = {
    "anatomy": "Anatomy.schema.json",
    "disease": "diseases.schema.json",
    "physiology": "physiology.schema.json",
}
MISSING_COMPONENT_SENTINEL = "—"


def load(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_schema_registry(schemas_dir: Path, main_schema: dict) -> Registry:
    """Register schema files by their $id and relative paths for $ref resolution."""
    base = main_schema["$id"].rsplit("/", 1)[0] + "/"
    registry = Registry()
    for path in schemas_dir.rglob("*.json"):
        try:
            schema = load(path)
        except json.JSONDecodeError as e:
            print(f"WARN  cannot parse schema {path}: {e}")
            continue
        if not isinstance(schema, dict):
            continue
        rel = path.relative_to(schemas_dir).as_posix()
        uris = {base + rel}
        if "$id" in schema:
            uris.add(schema["$id"])
        for uri in uris:
            registry = registry.with_resource(
                uri, Resource.from_contents(schema, default_specification=DRAFT202012)
            )
    return registry


def build_validators(schemas_dir: Path) -> dict:
    """Build category validators with the shared schema resources registered."""
    anatomy_schema = load(schemas_dir / SCHEMA_FILES["anatomy"])
    shared_registry = build_schema_registry(schemas_dir, anatomy_schema)
    return {
        category: Draft202012Validator(load(schemas_dir / filename), registry=shared_registry)
        for category, filename in SCHEMA_FILES.items()
    }


def load_component_ids(registry_path: Path) -> set[str]:
    """Read valid IDs from all registry rows; repeated IDs are intentionally allowed."""
    registry = load(registry_path)
    rows = registry.get("rows")
    if not isinstance(rows, list):
        raise ValueError(f"component registry {registry_path} must contain a rows array")
    ids = set()
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"component registry row {index} must be an object")
        component_id = row.get("component_id")
        if isinstance(component_id, str) and component_id and component_id != MISSING_COMPONENT_SENTINEL:
            ids.add(component_id)
    return ids


def check_component_ids(entity: dict, known_component_ids: set[str]) -> tuple[list[str], list[str]]:
    """Return missing and unknown component IDs separately."""
    component_ids = entity.get("component_ids")
    if not isinstance(component_ids, list) or not component_ids:
        return ["component_ids is absent, null, or empty"], []

    missing, unknown = [], []
    for value in component_ids:
        if not isinstance(value, str) or not value.strip() or value == MISSING_COMPONENT_SENTINEL:
            missing.append(repr(value))
        elif value not in known_component_ids:
            unknown.append(value)
    return missing, unknown


def load_reference_ids(registry_path: Path) -> set[str]:
    """Read known reference_ids from the source registry (references.json)."""
    registry = load(registry_path)
    if not isinstance(registry, list):
        raise ValueError(f"reference registry {registry_path} must contain a JSON array")
    ids = set()
    for index, item in enumerate(registry, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"reference registry item {index} must be an object")
        reference_id = item.get("reference_id")
        if isinstance(reference_id, str) and reference_id.strip():
            ids.add(reference_id)
    return ids


def check_anatomy_rules(entity: dict) -> list[str]:
    """Cross-field reference rules retained from the anatomy validator."""
    errors = []
    content = entity.get("content", {})
    refs = entity.get("references", [])
    if not isinstance(content, dict) or not isinstance(refs, list):
        return errors

    by_field = {}
    for ref in refs:
        if not isinstance(ref, dict):
            continue
        field = ref.get("content_field")
        if field in by_field:
            errors.append(f"duplicate reference entry for '{field}'")
        by_field[field] = ref

    for field in CONTENT_FIELDS:
        if field not in content:
            continue  # The schema reports missing required fields.
        ref = by_field.get(field)
        if ref is None:
            errors.append(f"'{field}' has no entry in references")
            continue
        status = ref.get("status")
        value = content[field]
        if status == "documented" and value is None:
            errors.append(f"'{field}' is 'documented' but its value is null")
        if status in ("not_available", "not_applicable") and value is not None:
            errors.append(f"'{field}' is '{status}' but its value is not null")
    return errors


def check_reference_ids(entity: dict, known_reference_ids: set[str]) -> list[str]:
    """Unknown reference IDs in metadata.references or per-field sources."""
    unknown = set()
    metadata_refs = entity.get("metadata", {}).get("references", [])
    if isinstance(metadata_refs, list):
        for value in metadata_refs:
            if isinstance(value, str) and value.strip() and value not in known_reference_ids:
                unknown.add(value)
    refs = entity.get("references", [])
    if isinstance(refs, list):
        for ref in refs:
            if not isinstance(ref, dict):
                continue
            sources = ref.get("sources", [])
            if not isinstance(sources, list):
                continue
            for source in sources:
                if not isinstance(source, dict):
                    continue
                value = source.get("reference_id")
                if isinstance(value, str) and value.strip() and value not in known_reference_ids:
                    unknown.add(value)
    if unknown:
        return ["UNKNOWN reference_id(s): " + ", ".join(f"{value!r}" for value in sorted(unknown))]
    return []


def validate_entity(
    entity,
    path: Path,
    validators: dict,
    known_component_ids: set[str],
    known_reference_ids: set[str] | None = None,
) -> list[str]:
    if not isinstance(entity, dict):
        return ["entity JSON root must be an object"]
    category = entity.get("category")
    if not isinstance(category, str):
        return [f"category must be a string; got {category!r}"]
    if category not in validators:
        return [f"unsupported or missing category: {category!r}"]

    validator = validators[category]
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '(root)'}: {error.message[:200]}"
        for error in validator.iter_errors(entity)
    ]
    missing, unknown = check_component_ids(entity, known_component_ids)
    if missing:
        errors.append("MISSING component ID(s): " + ", ".join(missing))
    if unknown:
        errors.append("UNKNOWN component ID(s): " + ", ".join(unknown))
    if category == "anatomy":
        errors.extend(check_anatomy_rules(entity))
    if known_reference_ids is not None:
        errors.extend(check_reference_ids(entity, known_reference_ids))
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    schemas_dir, kb_dir = Path(sys.argv[1]), Path(sys.argv[2])
    try:
        validators = build_validators(schemas_dir)
        known_component_ids = load_component_ids(schemas_dir / "common" / "component-registry.json")
        known_reference_ids = load_reference_ids(schemas_dir / "common" / "references.json")
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"ERROR  unable to initialize validation: {e}")
        return 2

    passed = failed = skipped = 0
    files = sorted(kb_dir.rglob("*.json"))
    for path in files:
        try:
            entity = load(path)
        except (OSError, UnicodeError, json.JSONDecodeError) as e:
            failed += 1
            print(f"FAIL  {path}\n      - cannot parse entity JSON: {e}")
            continue

        if not isinstance(entity, dict):
            failed += 1
            print(f"FAIL  {path}\n      - entity JSON root must be an object")
            continue

        if "category" not in entity:
            skipped += 1
            print(f"SKIP  {path}\n      - category is missing")
            continue
        category = entity["category"]
        if not isinstance(category, str):
            failed += 1
            print(f"FAIL  {path}\n      - category must be a string; got {category!r}")
            continue
        if category not in validators:
            skipped += 1
            print(f"SKIP  {path}\n      - unsupported category: {category!r}")
            continue

        errors = validate_entity(entity, path, validators, known_component_ids, known_reference_ids)
        if errors:
            failed += 1
            print(f"FAIL  {path}")
            for message in errors:
                print(f"      - {message}")
        else:
            passed += 1
            print(f"OK    {path}")

    print(f"\n{passed} passed, {failed} failed, {skipped} skipped")
    return 1 if failed or skipped else 0


if __name__ == "__main__":
    sys.exit(main())
