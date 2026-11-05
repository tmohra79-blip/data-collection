# IRIS & CILIARY BODY — Staging Extracts (الفصلان 9 و10 — اكتمل الاستخلاص)

> بنك استخراج لمكوّنات القزحية (Iris) والجسم الهدبي (Ciliary body). **الحالة: مغلقة** — الفصلان البدائيان وصلوا كاملين 2026-11-05 وبُنيت منهم 6 كروت v1.0.0.
> **تصحيح ترقيم مهم:** القزحية = **الفصل 9** (المطبوع 308-334، عنوانه 9.1 Gross / 9.2 Macroscopic / 9.3 Structure / 9.4 Movement of fluid and solute across the iris) والجسم الهدبي = **الفصل 10 "The posterior chamber and ciliary body"** (المطبوع 335-370، أقسامه: 10.1 posterior chamber ص335 · 10.2 ciliary body ص336 · 10.3 accommodation ص367 · 10.4 presbyopia ص369 · 10.5 ammetropia ص370 · 10.6 aqueous secretion ص370). التقدير السابق "ch10 للاثنين" اتزحزح فصلًا واحدًا.
> قاعدة الحصاد: quotes حرفية + رقم الصفحة المطبوعة + الملف المصدر. كل قيمة مشكوك فيها معلَّمة [OCR-unverified].

المصادر:
- `Pasted Content_1793890234270.txt` (دفعة 2026-11-05) — المطبوع **303-370** كاملة (68 صفحة): ذيل ch8 (303-307) + ch9 كامل (308-334) + ch10 كامل (335-370)
- ملفات جانبية محلية (حُصدت قبل وصول الدفعة): uvea overview ص167-230 · ch8 الزاوية ص272-302 · ch11 ص371-406 · ch16/ch17 ص570-672

---

## A. نتائج البناء النهائية (6 كروت v1.0.0 — 2026-11-05)

| ID | الكارت | كلمات | مصادر المقالات |
|---|---|---|---|
| IR-001 | `Knowledge_Base/Iris/iris.json` | 1,622 | — |
| IR-002 | `Knowledge_Base/Iris/iris-vessels-innervation.json` | 950 | song_2009_iris_vessels |
| CB-001 | `Knowledge_Base/CiliaryBody/ciliary-body.json` | 1,149 | — |
| CB-002 | `Knowledge_Base/CiliaryBody/ciliary-epithelium-aqueous.json` | 1,191 | civan_2004_secretion, sunderland_2023_ah_circulation |
| CB-003 | `Knowledge_Base/CiliaryBody/ciliary-muscle-accommodation.json` | 1,436 | strenk_1999_mri, sheppard_2011_ageing, tabernero_2016_accommodative, zuo_2024_ageing_cm |
| CB-004 | `Knowledge_Base/CiliaryBody/ciliary-body-vessels-nerves.json` | 1,127 | song_2009_iris_vessels |

الإجمالي: **7,475 كلمة** · references.json: 49 → **56 مصدرًا** (+7) · التراكر: 64 → **70 صفًا** · validate **69/69** · pytest خضرا (10+14).

## B. المقالات الداعمة السبع المتحقق منها (Europe PMC REST 2026-11-05 — `scripts/icb_articles_verified.json`)

1. **civan_2004_secretion** — Civan MM, Macknight ADC. The ins and outs of aqueous humour secretion. Exp Eye Res 2004;78(3):625-631. PMID 15106942, DOI 10.1016/j.exer.2003.09.021
2. **sunderland_2023_ah_circulation** — Sunderland DK, Sapra A. Physiology, Aqueous Humor Circulation. StatPearls NBK553209, 2023. PMID 31985990
3. **strenk_1999_mri** — Strenk SA, Semmlow JL, Strenk LM, Munoz P, Gronlund-Jacob J, DeMarco J. Age-related changes in human ciliary muscle and lens: an MRI study. IOVS 1999;40(6):1162-1169. PMID 10235549
4. **sheppard_2011_ageing** — Sheppard AL, Davies LN. The effect of ageing on in vivo human ciliary muscle morphology and contractility. IOVS 2011;52(3):1809-1816. PMID 21071738, DOI 10.1167/iovs.10-6447
5. **tabernero_2016_accommodative** — Tabernero J, Chirre E, Hervella L, Prieto P, Artal P. The accommodative ciliary muscle function is preserved in older humans. Sci Rep 2016;6:25551. PMID 27151778, PMC4858807
6. **song_2009_iris_vessels** — Song Y, Song YJ, Ko MK. A study of the vascular network of the iris using flat preparation. Korean J Ophthalmol 2009;23(4):296-300. PMID 20046692, PMC2789956
7. **zuo_2024_ageing_cm** — Zuo H, et al. The effect of aging on the ciliary muscle and its potential relationship with presbyopia: a literature review. PeerJ 2024;12:e18437. PMID 39735562, PMC11674140

## C. الحصاد الجانبي (من الملفات المحلية قبل وصول الدفعة — حُقن في الكروت)

### C1. uvea overview ص212-230 — للكروت IR-001/CB-001
- ص212: "It consists from behind forwards of the choroid and ciliary body, and the iris, which is perforated by the pupil." · "The iris, located in the plane of the limbus, separates the anterior chamber in front from the lens and its suspensory ligament behind."
- ص225: الزونيول ينشأ "from the epithelium of the pars plana and lateral walls and valleys of the pars plicata"
- ص229: "The anterior margin of the ciliary body corresponds precisely to the tip of the scleral spur, and is therefore 2 mm behind the corneal limbus in the vertical meridian and 1.5 mm in the horizontal." · ora: 6.5-7.0 mm نسيًا / 7.5-8.0 mm صدًا
- ص219: جدول — ciliaris width avg 2.0 mm · pars plana width 3.5-4.5 mm · processes 70-80 [OCR]
- ص230: تحذير الـ pars plana approach الجراحي

### C2. ch8 الزاوية ص274-302 — للكروت IR-002/CB-003/CB-004
- ص274: تشكل MAC + عروة Axenfeld 12% (Stevenson, 1963)
- ص281: ciliary band = anterior face of ciliary body + insertion into spur
- ص284: وتر العضلة الطولية في الـ spur (Schwalbe, 1870) + "Contraction of the ciliary muscle pulls the spur posteriorly and opens up the trabecular spaces."
- ص302: مسار uveoscleral عبر الجسم الهدبي

### C3. ch11 ص371-406 (أقسام 11.1 و11.5-11.11) — للكروت IR-002/CB-003/CB-004
- ص371: تعريف uveal tract + تقسيم التروية (ACA/LPCA → iris+CB؛ SPCA → choroid)
- ص374: MAC أمام الجزء الدائري للعضلة + IMC من ACA + الدائرتان قد تكونان غير مكتملتين
- ص376: ciliary flush + anterior segment ischaemia (بتر المستقيمات + الحزام المحيط)
- ص398: "The circulus iridis major is really located in the ciliary body"
- ص403: تروية العضلة (داخلي/أمامي MAC ↔ خارجي/خلفي IMC) + أوعية العمليات من MAC
- ص404-406: شرايين القزحية + plexus العضلتين + Weibel-Palade-like + تعصيب القزحية + أوردة uvea + Hayreh & Baines 1973

### C4. ch16 ص602-619 — للكروت IR-001/IR-002/CB-003
- ص603: "oculomotor stimulation contracts the sphincter and inhibits the dilator, and likewise the sympathetic is motor to the dilator and inhibitor to the sphincter."
- ص612: مركز EW + 95-97% ألياف للعضلة الهدبية و3-5% pupillomotor (Warwick, 1954)
- ص616: Adie (Loewenfeld & Thompson 1967) + Horner
- ص618-619: تعصيب القزحية (Ehinger 1966؛ Laties 1974؛ Nishida & Sears 1969) + الجسم الهدبي (Ruskell 1973: 1% ودي) + العضلة muscarinic غنية + CGRP/SP/VIP/NPY

### C5. ch17 ص632-646 — للكروت CB-001/CB-003
- ص632: spur عند ~4 شهور + إدخال الألياف الطولية منتصف الشهر السابع
- ص637: "The uveal tract ... is derived embryonically from vascular channels, neural crest cells and neuroectoderm."
- ص639: MAC يتشكل ويصل الجسم الهدبي بحلول الشهر السادس (Heimann, 1972)
- ص640-644: تطور طلاء الجسم الهدبي + العضلة (اشتباه من الأسبوع 10؛ شكل مثلثي بالشهر الخامس؛ أوتار مميزة منتصف الشهر السابع — Ozanics & Jakobiec 1982؛ الدائرية غير ناضجة حتى +سنة)
- ص644: "Unlike the fenestrated capillaries of the ciliary processes, adjacent endothelial cells that line the vessels of the ciliary muscle form a continuous lining and are joined by tight junctions."
- ص644-646: تطور القزحية (الموجة الثانية من neural crest؛ الدائرتان الشريانيتان بنهاية الشهر الرابع؛ dilator من الشهر السادس عند von Michel's spur؛ الـ collarette والدائرة الصغرى)

## D. مادة ch8 المتبقية (303-307) — مخزنة لكروت الزاوية المستقبلية

ذيل فصل ch8 (outflow apparatus): المقاومة 3 mmHg/µl/min (Grant, 1958) · uveoscleral ≈ 10% من التدفق · توزيع المقاومة (Peterson 1971: 60-65% meshwork+Schlemm) · تنظيم IOP · شيخوخة الشبكة (سمك 2-3×، curly collagen، hyalinization، فقد خلايا) · تغيرات Schlemm في POAG. **لم تُستخدم في كروت القزحية/الجسم الهدبي — محفوظة لكروت الزاوية وتصريف السائل لما نوصلها.**

## E. قيم تحتاج تأكيد من المراجعة الطبية

| القيمة | الموضع | الملاحظة |
|---|---|---|
| قطر الجيب الهدبي 11.25 mm (SD ±0.38) | ص336 | OCR "1 I .2.5" — [OCR-unverified] |
| عرض clump cell حتى ~100 µm | ص326 | OCR "10~" — [OCR-unverified] |
| مساحتا pars plicata/plana 60.08 / 24.58 mm² | ص219 | أرقام مدموجة بالجدول — [OCR-unverified] |
| انتشار iris processes في الزاوية | ص315 | OCR "i7'X," غالبًا 17% (Lichter, 1969) — [OCR-unverified] |
