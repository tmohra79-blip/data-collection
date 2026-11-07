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

## G. دفعة 2026-11-07 (الرابعة): مطبوع 465-467 + Macular Pigment من StatPearls

### حكم التغطية
- **465-467 (14.4-14.5: بداية الطبقة العصوية المخروطية): مغطاة بالكامل مسبقًا** في photoreceptor-layer.json (الإجماليات 77.9-107.3M/92M عصوية و4.08-5.29M/4.6M مخروطية، الأرجوان العصبي وبياض ما بعد الوفاة 5-10 دقائق، تباين الفوفيا/ora، within 8%، Nyquist 48-86/66، الرزقة 0.2-2.0°، النضوج) وmacula-fovea.json (one-to-one 0.5/0.4 ملم، albinism، النضوج حتى 5-8 سنين). الفتات الوحيد غير المغطى أُثري: superior rods +2% وrim cone threefold (Williams 1991) في photoreceptor-layer.json 1.0.0 → **1.1.0**.

### الاكتشاف: نص Wolff نفسه فيه Macular Pigment (ص457)
- الكتاب (في نص مُجمع سابقًا من دفعة ch13/14): "The yellow colouration probably derives from the presence of the carotenoid pigment, **xanthophyll**, in the ganglion and bipolar cells" + منطقة صفراء ~5 ملم + تفسير التباس مصطلحات macula/macular area/macula lutea + حفظ اللون (4°C ساعات-أيام؛ ألدهيد أسابيع-أشهر؛ الكحول يستخلصه — Tripathi & Tripathi 1984). لم يكن مغطى في أي كارت — أُضيف الآن.

### الإثراء المنفذ (macula-fovea.json 1.1.0 → **1.2.0**)
- definition: تسمية lutea (Wolff ص457) + lutein/zeaxanthin كاروتينويدات (StatPearls Retina).
- location: المظهر ophthalmoscopic (Fig 14.3 ص456: منطقة أغمق وانعكاس مُبيض أسفل مركز العصب) + **umbo** (أدنى نقطة لأرضية الفوفولا — قائمة مناطق StatPearls: perifovea→parafovea→fovea→FAZ→foveola→umbo).
- histology: تركيب الصبغة (lutein + zeaxanthin + **meso-zeaxanthin**، تركيز أعلى في الفوفيا) + تفاصيل الحفظ (ص457) + أرقام Fig 14.18 caption (ص466: 0.125/0.42/0.66 ملم، 4:1 على السنّة الفوفياوية).
- clinical: anti-inflammatory + **blue-light filtering** + MPOD وHaidinger brushes (dichroism) + AMD/macular telangiectasia/Stargardt + مكملات lutein/zeaxanthin ↑ MPOD وترتبط بانخفاض خطر DR/ROP.
- aliases/keywords: +umbo، macular pigment، lutein، zeaxanthin، meso-zeaxanthin، xanthophyll، MPOD، Haidinger brush، صبغة البقعة الصفراء.

### مراجع جديدة (58 → **60**)
- `statpearls_retina_2023` — Nguyen KH, Patel BC, Tadi P. Anatomy, Head and Neck: Retina. StatPearls; آخر تحديث 2023-08-08؛ NBK542332؛ **PMID 31194472** (Europe PMC REST).
- `statpearls_haidinger_2023` — Manion GN, Stokkermans TJ. Haidinger Brush Phenomenon. StatPearls؛ آخر تحديث 2023-07-08؛ NBK594225؛ **PMID 37603616** (تذييل صفحة Bookshelf).

### ملاحظة تشغيلية
- Workspace rollback حدث بين الرسائل (التراكر رجع 9 صفوف والكروت الجديدة اختفت) → **استعادة كاملة من origin/main (de9a75e — رفع المستخدم 17:04) بلا أي فقدان**، ثم أُعيد بناء هذه الجولة فوقها. التحقق النهائي: **validate 72/72 + pytest 10+14 + audit**.
- ** RV-001 لسه واقفة**: صفحات الأوعية الشبكية لسه مطلوبة. FAZ لسه كمبدأ (بدون قطر رقمي — لم يُعثر على رقم في المصادر المتاحة).

## H. جولة 2026-11-08 (خامسة): كارت umbo من مصادر خارجية — بالكامل

### السياق
- المستخدمة: «Umbo مش موجودة في الكتاب عندي فا جمع عنها من مصادر تانية انت» — تحقق نصي على كل لصاقات الكتاب المتاحة: لا وجود لـ umbo (الوحيد «Palumbo 1976» اسم مؤلف في ص69) — الـumbo فعلًا غائب عن وولف. الشطب من الكارت: v1.2.0 كان فيه جملة واحدة (StatPearls zonation).
- جولة خارجية كاملة: 7 مصادر جديدة (6 PMC open-access مقروءة نصها الكامل + Webvision) بتحقق اقتباس حرفي 16/16 قبل الكتابة.

### الإثراء المنفذ (macula-fovea.json 1.2.0 → **1.3.0**)
- location: **umbo = central plateau للفوفولا، ~0.15 ملم** (Eye 2023: fovea 1.5 / foveola 0.3 / umbo 0.15 ملم — ومطابقة Webvision)، هو مركز الفوفيا بلا RGCs (Nat Neurosci 2025)، ويطابق «مركز حفرة الفوفيا» (Front Cell Neurosci 2024)؛ **FAZ قطره ~0.2-1 ملم** (MEHDIophthal 2025) — قفل بند FAZ المعلق بدون رقم منذ v1.0.0 (و0.5 ملم عند Webvision).
- histology: أرضية الحفرة Muller cell bodies/processes (MEHDIophthal) وMüller cell cone في الـumbo (Front Cell Neurosci)؛ **مسار الربط: مخاريط الـumbo → محاور شعاعية → bipolars مُزاحة في foveal shoulder → حلقة RGCs حول الـumbo** (Nat Neurosci 2025)؛ مركز 0.1 ملم خالٍ من S-cones (MEHDIophthal) والحفرة خالية من العصويات (Webvision).
- clinical: الـumbo معلم تثبيت مسح OCT/OCTA (TVST 2026)؛ صغره يمنع التقاطه في بروتوكولات OCT القياسية (Sci Rep 2020)؛ **foveal crack sign** = خط شديد الانعكاس رأسي في الـumbo يمدد من ellipsoid zone حتى ILM، ظهر مع traction وعقبته ثقب ماكولا كامل السماكة بعد 9 أشهر في الحالة المصورة — نذير ثقب في العين الشقيقة (Sci Rep 2020).
- علاقة جديدة: drives → ganglion_cell_layer. aliases/keywords: +foveal umbo، central plateau، foveal crack sign، Müller cell cone، OCT centration، أومبو.

### مراجع جديدة (60 → **67**)
`eye_2023_foveal_status` (PMID 35505112) · `natneuro_2025_fovea_synchronization` (PMID 40670685) · `scirep_2020_foveal_crack_sign` (PMID 33199791) · `frontcellneuro_2024_foveal_muller_glia` (PMID 38994326) · `tvst_2026_octa_umbo_landmark` (PMID 42878570) · `mehdiophthal_2025_macula_anatomy` (PMID 40787281) · `webvision_fovea_architecture` (Kolb et al., Webvision).

### ملفات المصادر المحفوظة (download/sources/)
pmc12330045_fulltext.xml · epmc_PMC9873750.xml · epmc_PMC12411267.xml · epmc_PMC7670431.xml · epmc_PMC11236602.xml · epmc_PMC13676230.xml · webvision_kolb_fovea_architecture.html + النصوص المستخرجة.

### المتبقي
- **RV-001 لسه واقفة**: صفحات الأوعية الشبكية (الأقواس/الشبكتان الشعريتان/CRA/CRV) لسه مطلوبة.

## I. جولة 2026-11-08 (سادسة): قفل الـ FAZ — lصاقات 396/465/467/663 + 5 مقالات خارجية

### السياق
- المستخدمة بعتت 4 لصاقات («ده اللي موجود في الكتاب عن Foveal Avascular Zone») وطلبت: شوفهم، ولو ناقص هات من مقالات موثوقة وخلّص الجزء ده.
- **تدقيق الصاقات أولًا**: ص465 (مجاميع العصويات/المخاريط + الموزاييك) متغطية كاملة من جولة 2026-11-07 — صفر إضافات. ص396 (بنية الشعيرات الدموية الجيبية + Bruch) ~90% متغطية في choriocapillaris.json — 4 تفاصيل دقيقة ناقصة. ص467 (توزيع العصويات) كلها متغطية إلا جملة واحدة. **ص663 (تطور الغدة الدمعية/ملحقات الجفن/العضلات خارج المقلة) خارج موضوع FAZ تمامًا** — اتسجلت كمصدر واقترحت لجولة تطوير ملحقات لاحقًا، مش داخلة في الكروت هنا.
- المصادر الخارجية: 5 أوراق مخصصة للـ FAZ (أوروپا PMC، نصوص كاملة محفوظة) — تحقق اقتباس حرفي **23/23 PASS** قبل الكتابة (منهم 5 اقتباسات كتاب من اللصاقات المحفوظة في sources/book_pastes/).

### الإثراء المنفذ
- **macula-fovea.json 1.3.0 → 1.4.0 (الـ FAZ مقفول)**:
  - location: تعريف «A region without vasculature around the fovea is called the foveal avascular zone (FAZ)» (Yoshimura TVST 2026) + norms سكانية: n=1004 من Gutenberg Health Study — متوسط **0.27 ± 0.12 mm²** ومدى الـ 5-95% **0.08-0.47 mm²** (Welzel TVST 2026)؛ 224 عين/112 متطوع — سطحية **0.27 ± 0.11** مقابل عميقة **0.35 ± 0.12 mm²** (P<0.001) (Ghassemi 2017)؛ 101 عين مسنة — **0.35 ± 0.12 mm²** (Hasegawa Sci Rep 2026)؛ **إزاحة مركز الـ FAZ عن مركز مستقبلات الفوفيا 41.6 ± 21.1 µm** (Hasegawa).
  - blood_supply: الـ FAZ موجود عند كل ضفيرة بحجم مختلف — سطحية 0.27 مقابل عميقة 0.35 mm² وترابط بينهما r=0.82 (Ghassemi)؛ تطابق قياس الـ FAZ بين total retina والـ ICP (ICC 0.98 — Welzel)؛ **الشعيرات المحيطية تنساب شعاعيًا نحو الداخل حول الـ FAZ** — نموذج الأستروسايت-الأوعية أعاد إنتاج الأقواس والـ FAZ والتدفق الشعاعي الداخلي (Yoshimura TVST 2026).
  - clinical: **OCTA يتفوق على الفلورسين في تمييز الـ FAZ** (تضخم/انقطاع/dropout) — Welzel؛ تغيرات FAZ في أمراض السكر والانسدادات الوريدية وكمؤشر محتمل في MS/Alzheimer/Parkinson/IBD (Welzel)؛ داخل الحدود الطبيعية لا ارتباط بالعمر/الضغط/السكر/التدخين (Gutenberg) وأكبر في الإناث والعيون الأقصر؛ **في السكري يتضخم قبل الـ DR المرئي**: control 0.278 → NDR 0.308 → NPDR 0.351 mm² وارتباط إيجابي بمدة السكري والـ BMI (Wei Clin Ophthalmol 2025).
- **photoreceptor-layer.json 1.2.0 → 1.3.0**: جملة التعادل 1:1 — «A one-to-one ratio of rods to cones is seen 0.5 mm nasal and temporal, and 0.4 mm superior and inferior, to the centre of the fovea (Curcio et al., 1990)» (ص467).
- **choriocapillaris.json 1.1.0 → 1.2.0**: حجاب الفتحات «thickened centrally (30 nm)» (Fig 11.19)؛ الأوجه الجانبية مائلة؛ تباين الوصلات بين الشريينات (occluding zonules نموذجية) والشعيرات/الفينولات (نوع خاص) — ص396؛ إطار داعم كولاجيني بفايبروسايتس داخل شبكات الشعيرات وفي الطبقة فوق الشعرية (Fig 11.15) — ص396.
- keywords macula-fovea +9: FAZ area، superficial/deep/intermediate capillary plexus، OCTA، perifoveal radial capillaries، Gutenberg Health Study، FAZ centre offset، foveal avascular zone area.

### مراجع جديدة (67 → **72**)
`tvst_2026_gutenberg_faz_normative` (PMID 42929705) · `jcoophthal_2017_faz_normative` (PMID 29270477) · `tvst_2026_faz_model_astrocytes` (PMID 41769944) · `scirep_2026_faz_elderly` (PMID 41667614) · `clinophthal_2025_faz_diabetes` (PMID 41019873).

### ملفات المصادر المحفوظة (download/sources/)
epmc_PMC13722972_faz.xml · epmc_PMC5735238_faz.xml · epmc_PMC12967130_faz.xml · epmc_PMC12960704_faz.xml · epmc_PMC12474716_faz.xml (+ PMC13422916/PMC13515158 للفحص) · book_pastes/book_printed{396,465,467,663}_*.txt · epmc_faz_search.json · epmc_faz_meta.json.

### المتبقي
- **RV-001 لسه واقفة**: صفحات الأوعية الشبكية (الأقواس/الشبكتان الشعريتان/CRA/CRV — وولف ص~489-494) لسه مطلوبة.
- **ص663**: كارت تطوير ملحقات (غدة دمعية 45 يوم/قنوات 3 شهور، Zeis الشهر 4، meibomian+Moll عند 80 mm، فتح الجفون 5-6 شهور + EGF، العضلات من preotic somites) — مقترحة كجولة مستقبلية.

## J. جولة 2026-11-08 (سابعة): تغطية المصطلحات الستة + إغلاق Henle's Fiber Layer

**السؤال:** المستخدمة راجعت قائمة: Macula Lutea / Fovea Centralis / Foveola / Umbo / Foveal Avascular Zone / Henle's Fiber Layer — «كدة جمعنا عن دول كلهم؟»

**نتيجة التدقيق (ضد الكروت الفعلية):**

| المصطلح | الحالة قبل الجولة | مكان التوثيق |
|---|---|---|
| Macula Lutea | مكتمل (تعريف + مناطق + صبغة صفراء xanthophyll/lutein/zeaxanthin + Haidinger/MPOD) | macula-fovea.json |
| Fovea Centralis | مكتمل (1.85 ملم، إزاحة الطبقات، التطور، الألبينزم) | macula-fovea.json |
| Foveola | مكتمل (0.35 ملم rod-free، 199k مخروط/مم²، fovea externa) | macula-fovea.json |
| Umbo | مكتمل جولة 5 (v1.3.0، 7 مصادر خارجية) | macula-fovea.json |
| Foveal Avascular Zone | مكتمل جولة 6 (v1.4.0، 5 مصادر خارجية) | macula-fovea.json |
| **Henle's Fiber Layer** | **ناقص** — ذكر عابر فقط (الجزء البقعي من OPL من وولف ص227/474: 51 ملم ألياف مائلة) بلا إثراء خارجي | outer-plexiform-layer.json |

**مصادر Henle (6 جديدة + 2 موجودة أعاد استخدامها):** نصوص كاملة محفوظة في download/sources/:
1. Koksaldi et al., Med Hypothesis Discov Innov Ophthalmol 2025 (PMID 40787281, PMC12330045 — الموجود من جولة 5): قسم HFL كامل — التركيب (ثلثا OPL البقعية ألياف مخروطية شعاعية + عمليات Müller)، المدى الشعاعي 5500/8500 ملم، موازاة ILM عند حافة الفوفولا، طول الأكسون 558 ملم وأول مشبك 350 ملم، أعلى تركيز للصبغة البقعية في HFL، النجمة البقعية/الوذمة الكيسية/النزوف البتالويدية، hyperreflective over drusen، ASHH.
2. Wong-Fortunato et al., IOVS 2026 (PMID 42610579, PMC13496266): AAV-EGFP في قرد الريسس يُظهر ألياف هنلي in vivo كنجمة بقعية؛ الحزم 30.0±2.2 خط قريب / 60.3±2.5 بعيد — متسقة بين الأفراد ومتقاربة نحو المركز؛ الدهن في النجمة البقعية يرسم حزم هنلي.
3. Lujan et al., IOVS 2011 (PMID 21071737، ملخص): الانعكاسية اتجاهية تزيد مع الابتعاد في الجهة المقابلة لدخول الحزمة؛ إدراج HFL يضخم قياس ONL بنسبة 52%.
4. Drasdo et al., Vision Res 2007 (PMID 17320143، ملخص): طول الألياف 406-675 ملم في المقاطع الشعاعية — أطول بكثير مما كان يُذكر.
5. Ramtohul et al., Prog Retin Eye Res 2023 (PMID 36333227، ملخص): حزم أكسونات غير متميلنة + عمليات Müller خارجية؛ مراجعة pathoanatomy إشارة ASHH.
6. Ruiz-Moreno et al., Diagnostics 2026 (PMID 42121989, PMC13163305): SNIFR = انشقاق عند HFL/OPL بنمط spoke–wheel؛ HFL نقطة ضعف بنيوية للقوى القصية.
7. Bringmann et al., PLoS One 2022 (PMID 35417487, PMC9007365): ألياف هنلي تعوض الإزاحة بين الطبقات الداخلية والخارجية؛ مناطق hyporeflective (فراغات كيسية محاطة بحزم هنلي) في foveal hypoplasia عالية الدرجة.
8. Kar et al., Front Cell Neurosci 2024 (PMID 38994326 — الموجود): Müller glia = 80% من حجم HFL (و95% من أرضية الفوفيا).

**التطبيق (scripts/enrich_henle_v120.py):**
- outer-plexiform-layer.json 1.1.0 → **1.2.0**: كتلة HFL مخصصة في definition/location/layers/histology_summary/clinical_importance (كل حقيقة باقتباسها) + aliases +3 + keywords +19 (EN+AR) + provenance ميداني لمصادر خارجية؛ 53 ذكرًا لـHenle (كانت 7).
- macula-fovea.json 1.4.0 → **1.5.0**: جملة ربط الصبغة البقعية بـHFL + keyword + provenance.
- references.json 72 → **78** (+6: lujan_2011_henle_oct، drasdo_2007_henle_length، iovs_2026_henle_bundles، preteyeres_2023_ashh، diagnostics_2026_snifr_hfl، plosone_2022_foveal_hypoplasia_hfl).
- تحقق اقتباس حرفي **29/29 PASS** قبل الكتابة.
- التراكر: صف 14 (RET-005) col13 ختم validate + col21 ملاحظة round 7؛ صف 72 (RV-002) col21 + جملة round 7.

**QA:** validate **72/72** + pytest **10+14 subtests**؛ كل reference_ids تُحل في references.json (78)؛ لا placeholders؛ الحزم: download/KB_full_round_2026-11-08_v3.zip.

**النتيجة للقائمة الستة: كلها مكتملة الآن** — خمسة في macula-fovea.json (v1.5.0) وسادسها (Henle) في outer-plexiform-layer.json (v1.2.0) مع 8 مصادر.

**المتبقي:** RV-001 (صفحات الأوعية الشبكية وولف ص~489-494) + مقترح كارت تطوير الملحقات (من ص663).
