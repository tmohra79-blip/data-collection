"""
Validate knowledge-base entities.

Usage:
    python validate.py <schemas_dir> <knowledge_base_dir>

Example:
    python validate.py schemas Knowledge_Base

Requires:  pip install jsonschema referencing
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


def load(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_registry(schemas_dir: Path, main_schema: dict) -> Registry:
    """Register every schema file under its $id, or under a URL derived
    from the main schema's $id, so relative $refs (common/...) resolve."""
    base = main_schema["$id"].rsplit("/", 1)[0] + "/"
    registry = Registry()
    for path in schemas_dir.rglob("*.json"):
        try:
            schema = load(path)
        except json.JSONDecodeError as e:
            print(f"WARN  cannot parse {path}: {e}")
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


def check_rules(entity: dict) -> list[str]:
    """Cross-field rules that JSON Schema can't express."""
    errors = []
    content = entity.get("content", {})
    refs = entity.get("references", [])

    by_field = {}
    for r in refs:
        field = r.get("content_field")
        if field in by_field:
            errors.append(f"duplicate reference entry for '{field}'")
        by_field[field] = r

    for field in CONTENT_FIELDS:
        if field not in content:
            continue  # the schema already reports missing fields
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


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    schemas_dir, kb_dir = Path(sys.argv[1]), Path(sys.argv[2])
    main_schema = load(schemas_dir / "Anatomy.schema.json")
    validator = Draft202012Validator(
        main_schema, registry=build_registry(schemas_dir, main_schema)
    )

    failed = 0
    files = sorted(kb_dir.rglob("*.json"))
    for path in files:
        entity = load(path)
        if entity.get("category") != "anatomy":
            continue
        errors = [
            f"{'/'.join(map(str, e.absolute_path)) or '(root)'}: {e.message[:200]}"
            for e in validator.iter_errors(entity)
        ]
        errors += check_rules(entity)

        if errors:
            failed += 1
            print(f"FAIL  {path}")
            for msg in errors:
                print(f"      - {msg}")
        else:
            print(f"OK    {path}")

    print(f"\n{len(files) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())