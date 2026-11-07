# RETINAL VESSELS & MACULA — Round Staging (جولة RV)

> **الحالة:** RV-002 (الماكولا والفوفيا) **اتبنى واتسلم 2026-11-07** — v1.0.0، validate 71/71.
> **RV-001 (الأوعية الشبكية) مستني صفحات** — انظر القسم D.

## A. المصادر اللي وصلت (دفعة 2026-11-07)

| الملف | المطبوع | المحتوى |
|---|---|---|
| `Pasted Content_1794050143313.txt` | 146-176 | ch4: ذيل Müller's muscle + 4.19 anomalous EOM (ص147) + 4.20-4.29 (مُجمَع سابقًا) |
| `Pasted Content_1794050207311.txt` | 220-259 | ch6 topographic anatomy كامل (220-233) + بداية ch7 cornea (233-259) |
| `Pasted Content_1794050316624.txt` | 268-296 | ch7 limbus/episclera/sclera (268-278) + ch8 anterior chamber & outflow (279-296) |
| لصق مباشر في الرسالة | 465-469 + 495 + 230 | ch14 rods/cones + ch15 glia (495 مُجمَع سابقًا) + ch6 ص230 (مكرر بالملف) |

## B. اللي اتبنى منه (RV-002)

- **`Knowledge_Base/Retina/macula-fovea.json`** — v1.0.0: التقسيم الطبقي للمنطقة المركزية (Table 6.1 ص220: foveola 0.35 / fovea 1.85 / rod-free 0.57 / parafovea 0.5 / perifovea 1.5 / macula 5 / area centralis 5-6 ملم، 18°20′) + بنية الحفرة (fovea externa، Henle's fibres، clivus، غياب الطبقات الداخلية، إزاحة العقدية → نصف السُّمك) + الأقواس الوعائية الأربعة والشعيرات للطبقات الداخلية فقط + نسبة التدفق المشيمي:الشبكي 10:1 → الفوفولا بلا أوعية + Curcio 1990 (199k/مم²، متوسط؛ Nyquist 66 c/deg) + غياب المخاريط الزرقاء المركزي (100 μm، ص468) + التعلق الزجاجي البقعي الحلقي 3-4 ملم (Fig 6.20) + نضوج الحفرة والتهاب الشبكية الصباغي (albinism).
- references.json: 56 → **57** (+ `curcio_1990_topography`, PMID 2324310).
- علامة مراجعة طبية: [OCR-unverified] مجموع مخاريط الفوفولا (النص ص227 "total 3500" والجدول ص220 "35 000" — واحد فيهم غلط OCR).

## C. مادة مخزّنة لجولات قادمة (من نفس الدفعة)

1. **ch8 ص279-296 (الزاوية والتصريف)** — anterior chamber (عمق 3.15 ملم، الحجم 220 μl، الاختزال السنوي) + limbus الثلاثي المناطق + معالم الزاوية gonioscopically + outflow apparatus (trabecular meshwork، Schlemm 30-45 μm، قنوات جامعة 25-35، scleral spur SSC cells + تعصيبها VIP/nitrergic) — **هذا الذيل ينضم لمخزون ص303-307 الموجود مسبقًا لكروت الزاوية (AC-001..).**
2. **ch4 ص146-147** — علاقات وفعالات Müller's muscle (رفع ~3 ملم، ptosis هورنر 3-4 ملم) + **4.19 anomalous extraocular muscles** (gracilis orbitis/comes obliqui superioris، accessory lateral rectus، tensor trochleae، transversus orbitus مع أعصابها) — **مرشح إثراء لـ MUS-001/OSM-001.**
3. **ch6 ص228-233 surface anatomy** — مسافات من الليمبس (Fig 6.23)، vortex veins (6 مخارج/عين متوسط 5.82، المسار داخل الصلبة 4.53 ملم — Rutnin 1967)، insertions العضلات (SO خلفي 17-19 ملم؛ IO قريب من الماكولا 1-2 ملم من الحفرة!) — **مرشح إثراء لـ vortex-veins + كروت العضلات، ومكمّل لـ RV-001.**
4. **ch7 ص233-259 + 268-278** — cornea/sclera: مقاطع مُجمَّعة غالبًا في كروت COR/SCL؛ الجديد المحتمل: Table 7.1 تركيب الكولاجين، plaques صلبة، Table 7.2 فتحات الأوردة الدوامة.

## D. الناقص لإغلاق الجولة (RV-001 retinal vessels)

**المطلوب من الكتاب — ch14 (The retina) المطبوع ~489-494** (قسم الأوعية الشبكية بعد RPE): مسار الشريان/الوريد الشبكي المركزي داخل العصب، الأقواس الوعائية، الشبكتان الشعريتان السطحية والعميقة، حاجز الدم-شبكية الداخلي، الخلايا المحيطة (pericytes).
- اختياري للإثراء: المطبوع ~452-459 (مقدمات الفصل وصورة الماكولا المبكرة).
- **ملحوظة:** مسار CRA/CRV داخل غمد العصب موثق عندنا بالفعل في كروت ON (ch15 ص527-530) — كارت RV-001 هيركز على الشجرة الشبكية نفسها وهيربط بـ comp_retinal_vessels + comp_vessel_ophthalmic_artery + comp_vessel_central_retinal_vein (الثلاثة صفر تغطية في المودل).

## E. دفعة 2026-11-07 (مساءً): مطبوع 479-492 — `Pasted Content_1794051401285.txt`

### حكم التغطية
- **479-488 (نهاية ch14: بقايا 14.9 + 14.10 IPL + 14.11 GCL + 14.12 NFL + 14.13 ILM): مغطاة بالكامل مسبقًا** — تم التحقق بمطابقة 14 معلومة مميزة (one-to-one midget:cone، كثافة Müller 8-13k/mm²، 24 variety amacrine، >2M synapse/mm²، 1.2M ganglion cell، 32-38k/mm²، parasol/bistratified، axoplasmic flow 0.5-5 و10-2000 mm/day، basement membrane facets، ILM 0.5-2.0 μm…) على الكروت القائمة (inl/ipl/gcl/nfl/ilm وmacula-fovea). صفر إضافة مطلوبة.
- **489-492 (بداية ch15: 15.1 optic nerve — الأقسام والمسار + التنظيم الطوبوغرافي + Fig 15.2): كانت غير مأخودة** → **إثراء 3 كروت** (تحت).

### الإثراء المنفذ (2026-11-07)
| الكارت | الإصدار | الإضافة |
|---|---|---|
| `optic-nerve.json` | 1.3.0 → **1.4.0** | definition: مبدأ tract-of-brain (لا neurolemma، محاط بـ meninges، قياس gracile/cuneate) ص489؛ location: الطول الكلي ~5 cm (intraocular 0.7 mm / intraorbital 3 cm / canalicular 6 mm / intracranial 1 cm) + نقطة الخروج فوق القطب الخلفي بـ 3 mm أنسيًا + تغير المقطع rounded→sinuous→oval→piriform→flat band + تعميم CSF ص489؛ histology: **التنظيم الطوبوغرافي للألياف** (خط الفصل عبر مركز الفوفيا، ألياف الماكولا تفصل العلوي/السفلي في المسار كله، ألياف peripapillary تعبر سطحًا زجاجيًا — van der Hoeve 1920/Minckler 1980؛ **ألياف Bjerrum في إسفين ~30° من الربيعين الصدغيين** — Radius & Anderson 1979) ص490؛ clinical: ربط Bjerrum بالscotoma القوسي للجلوكوما |
| `optic-disc.json` | 1.2.0 → **1.3.0** | layers[0]: **central meniscus of Kuhnt** (تثخّن غشاء Elschnig مركزيًا) ص491؛ layers[1]: **تناظر النسيج الحدودي** — border tissue of Elschnig جهة صدغية بين خلايا القناة ومشيمية، وجهة أنفية المشيمية ملاصقة مباشرة (Anderson & Hoyt, Fig 15.2) ص491 |
| `optic-nerve-septa.json` | 1.2.0 → **1.3.0** | histology: ~1,000 fascicles (Anderson & Hoyt) كتأكيد لنطاق Deyl 800-1200 + **central supporting connective tissue strand** (نسيج محيط بالأوعية المركزية يندمج مع الصفيحة الغربالية) + أصل septal tissue من pia حتى القسوة ص491 |

- references.json: 57 → **58** (+ `anderson_hoyt_1969`, Arch Ophthalmol 1969;82(4):506-530, PMID 4981187 — اتأكد عبر Europe PMC؛ مصدر Fig 15.2).
- الحالة بعد الجولة: **validate 71/71 + pytest 10+14 + audit صفر مشاكل**؛ التراكر ON-001/ON-002/ON-004 اتحدثوا (notes + ref pages + ختم validate).
- **علم OCR:** ص489 يذكر intraocular = 0.7 mm بينما نفس الصفحة تقول امتداد الرأس العصبي ~1 mm — النصان منقولان كما هما وبدون تحيّز.

### لسه ناقص في جولة RV
- **RV-001 (الأوعية الشبكية):** قسم الأوعية الشبكية في ch14 مش في 489-494 (489 = بداية ch15) — مكانه المحتمل داخل ch14 قبل المستقبلات (~470-478؟) أو في فصل الأوعية؛ **المطلوب: أي صفحات فيها retinal blood vessels / central retinal artery & vein / capillary beds.**
