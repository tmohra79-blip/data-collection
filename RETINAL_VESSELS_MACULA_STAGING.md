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

## F. دفعة 2026-11-07 (الثالثة): مطبوع 230-236 + 466-478 + 660-662

### حكم التغطية
- **466-478 (ch14: كثافة المخاريط/العصويات، الأجزاء الداخلية/الخارجية، الصبغات، ELM، ONL، OPL، synapses، بداية INL): مغطاة بالكامل مسبقًا** — تم التحقق بـ 12 معلومة مميزة (1000-1200 قرص مخروطي، 3.5/16.5 nm، calyx 9-12 villi، Schulze baskets، 35,676,000 bipolar، 9 أنواع، 20% rod bipolar، luminosity/chromaticity، Kolmer crystalloid، ONL 45/22/50 μm، triad 10-25، 6-8 horizontal). صفر شغل.
- **230-233 (ch6 surface anatomy): جولة إثراء** (كانت مخزّنة في القسم C.3 كمرشح) — نُفذت تحت.
- **233-236 (ch7 opening: أبعاد القرنية + Table 7.1 + epithelium): الفجوة كانت Table 7.1 والأبعاد** (الـ epithelium مغطى) — نُفذت تحت.
- **660-662 (ch17: تطور العدسة + 17.10 adnexae): فجوة كاملة** → كارت جديد LNS-007.

### المنفذ (2026-11-07)
| الكارت | الإصدار | الإضافة |
|---|---|---|
| `Choroid/vortex-veins.json` | 1.1.0 → **1.2.0** | location: أرقام Rutnin الكمية ص232 (~6 مخارج/عين: 3.36 أنفي vs 2.46 صدغي؛ أقرب للخط الرأسي صدغيًا؛ القوس من الليمبس 19.86 ملم (13.75-25)؛ inferotemporal الأقدم والأكثر تغيرًا، superotemporal الأأخر والأثبت؛ معظمها ~3 ملم خلف الاستواء) |
| `Muscles/superior-oblique.json` | 1.1.0 → **1.2.0** | layers[insertion]: الطول 7-18 ملم، التقعر anterior، الطرف الخلفي 17-19 ملم من الليمبس والأمامي 12-14 ملم قرب الطرف الصدغي لـ SR، الحافة الخلفية حتى 14 ملم من النهاية الأنسية لـ SR (Hogan 1971) ص230-231 |
| `Muscles/inferior-oblique.json` | 1.1.0 → **1.2.0** | layers[insertion]: الطول 5-14 ملم، التقعر inferior، الحافة الخلفية 3-6 ملم أمام حافة العصب البصري، 1 ملم تحت حدّه السفلي، **1-2 ملم من الفوفيا**، قريب من الوريد الدوام السفلي الصدغي + clinical: تحذير جراحي ص232 |
| `Cornea/corneal-stroma.json` | 1.1.0 → **1.2.0** | histology: **Table 7.1** (ماء 78%، كولاجين 15%: I 50-55% / III ~1% / IV 8-10% / VI 25-30%؛ keratan sulphate 0.7%؛ chondroitin/dermatan 0.3%؛ lumican 3-20K + decarin 10-50K؛ تزايد السلفنة محيطيًا) + الأبعاد (11.7×10.6 ملم، خلفي دائري 11.7، أعرض 1% في الذكور، سماكة 0.52/0.67، مساحة 1.3 cm² = 1/6 الكرة، أنصاف انحناء المنطقة البصرية 7.8/6.5) + topography (apex/cap 2-4 ملم، keratometry 7.2-8.4، نصف قطر القمة الخلفي 5.8 ملم — Patel 1993) ص233-234 |
| **`Lens/lens-development.json` (جديد)** | **1.0.0** | ch17 ص660-662: placode (يوم 27) → vesicle (يوم 29، lens pit/pore) → stalk necrosis + انفصال (يوم 33، 0.2 ملم) → primary fibres + embryonic nucleus (توقف DNA، crystallins، إغلاق التجويف يوم 45/20 ملم، fascia adherens، فقدان الظهارة الخلفية) → lens bow + secondary fibres → **درزات Y** (مرحلة 35 ملم ≈ 8.5 أسابيع، تدوم مدى الحياة) → تغيرات الشكل (كروية 18-24 ملم، مولود spheroidal، dehydration) → γ-crystallin 23% قبل الولادة (Bessems 1990) → الزلال (الأسبوع 10/45 ملم → الشهر الخامس) → التروية الحيالوية الأسبوع 7 |

- references.json: **تصحيح** `rutnin_1967_choroid` (كان من 2026-10-27 بـ issue 6 غلط) → issue 5 صح، pages 64(5):821-839، **PMID 6054193** من Europe PMC. يبقى العدد ثابت **58**.
- التراكر: CHO-005 / MUS-006 / MUS-007 / COR-003 اتحدثوا + **LNS-007** جديد (ملاحظة: LNS-006 مشغول بـ ciliary-zonule) → **72 صف**.
- الحالة بعد الجولة: **validate 72/72 + pytest 10+14 + audit صفر مشاكل**.

### مخزّن لجولات قادمة
1. **ص662 (17.10 eyelids/adnexae)**: تطور الجفون (بروز 4-5 أسابيع، اندماج ~10 أسابيع/45 ملم)، goblet cells سيلوموسين في الفورنيكس أولًا (Sellheyer 1988; Miyashita 1992)، mesenchyme — **مرشح لكارت adnexa/conjunctiva development مستقبلًا.**
2. **ص235-236 epithelium ultrastructure** (glycogen 20-30/10 nm، tonofibrils 8 nm، desmosomes/hemidesmosomes، anchoring filaments) — تأكيدات موجودة في corneal-epithelium.json (تم التحقق).
3. **RV-001 لسه واقفة**: صفحات الأوعية الشبكية (الأقواس/الشبكتان الشعريتان/CRA/CRV) لسه مطلوبة.

### إضافة متأخرة على نفس الدفعة (فوفيا)
- `Knowledge_Base/Retina/macula-fovea.json` 1.0.0 → **1.1.0** — صفحات 466-478 نفسها فضلت **صفر إضافة** (histology الفوفيا مغطى)، لكن المعلم الجراحي الجديد من ص231-232 اتعبر مادة فوفياوية مستحقة للكارت: clinical_importance بقي فيه (الحافة الخلفية لمرتكز العضلة المائلة السفلية 3-6 mm أمام حافة العصب البصري، 1 mm تحت حده السفلي، **1-2 mm من الفوفيا**، قرب الوريد الدوامي الصدغي السفلي) بإحالة إلى MUS-007؛ keywords +4 (inferior oblique insertion / surgical landmark / lower temporal vortex vein / خطورة جراحية قرب الفوفيا)؛ مصدر clinical_importance ch6 pages +231,232. التحقق بعدها: **72/72 + pytest 10+14 + audit صفر**؛ التراكر صف RV-002 اتحدث (ref pages + 231-232).
