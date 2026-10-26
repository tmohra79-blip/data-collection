# -*- coding: utf-8 -*-
"""
إصلاح سجل قطع مجسم العين (component-registry.json)

المشكلة: كروت الجسم الزجاجي الستة بتشير لقطعة اسمها comp_vitreous،
وسجل القطع في الريبو ناقصه السطر ده، فالتحقق بيقول:
    UNKNOWN component ID(s): comp_vitreous

الشغل: السكريبت ده بيضيف سطر واحد بس (comp_vitreous) لو مش موجود.
- لو موجود من قبل: مش هيغير أي حاجة خالص.
- مش بيمس ولا يعدل أي سطر تاني في السجل.

التشغيل من جذر الريبو:
    python add_vitreous_component.py
"""
import json
import sys
from pathlib import Path

REGISTRY = Path("schemas/common/component-registry.json")

# سطر الجسم الزجاجي زي ما هو موجود في السجل المرجعي (source_row 37)
VITREOUS_ROW = {
    "source_row": 37,
    "component_id": "comp_vitreous",
    "category": "Vitreous",
    "medical_name_en": "Vitreous Body",
    "medical_name_ar": "الجسم الزجاجي",
    "unity_name": "vitreous_body",
    "has_3d_model": "No",
    "parent": "—",
    "reference_category": "anatomy",
}


def main() -> int:
    if not REGISTRY.exists():
        print(f"ERROR  مش لاقي الملف: {REGISTRY}")
        print("       شغّلي السكريبت ده من جذر الريبو (الفولدر اللي فيه validate.py)")
        return 2

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    rows = registry.get("rows")
    if not isinstance(rows, list):
        print("ERROR  ملف السجل شكله مش متوقع (مفيش rows) — ابعتيلي الملف قبل أي تعديل")
        return 2

    ids = {r.get("component_id") for r in rows if isinstance(r, dict)}
    if "comp_vitreous" in ids:
        print("OK     comp_vitreous موجود في السجل من قبل — مفيش أي تغيير")
        return 0

    rows.append(VITREOUS_ROW)
    REGISTRY.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("OK     تم إضافة سطر comp_vitreous (الجسم الزجاجي) لسجل القطع")
    print(f"       إجمالي سطور السجل دلوقتي: {len(rows)}")
    print("       جرّبي بعدها: python validate.py schemas Knowledge_Base")
    return 0


if __name__ == "__main__":
    sys.exit(main())
