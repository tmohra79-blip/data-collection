# ROUND 6 — FAZ Completion (2026-11-07, v2 package)

## What was asked
User sent 4 book pastes (printed 396, 465, 467, 663) as "what's in the book about
the Foveal Avascular Zone" and asked to finish the FAZ part, taking anything
missing from reliable articles.

## Audit of the pastes (before any writing)
| Paste | Content | Verdict |
|---|---|---|
| printed 396 | choriocapillaris ultrastructure + Bruch's membrane intro | ~90% already in choriocapillaris.json from earlier rounds → 4 micro-details added |
| printed 465 | rod/cone totals (92M / 4.6M), mosaic variability | already 100% covered in photoreceptor-layer.json (round 4) — nothing added |
| printed 467 | rod density & distribution | all covered except one sentence: 1:1 rod:cone ratio distances → added |
| printed 663 | lacrimal gland / lid appendages / EOM development | **NOT FAZ-related** — flagged for a future adnexae-development round, not applied |

## External sources fetched (5 papers, full texts saved)
1. **Welzel et al., TVST 2026** (Gutenberg Health Study, PMID 42929705) — normative FAZ
   area 0.27 ± 0.12 mm2 (n=1004), 5th–95th percentile 0.08–0.47 mm2; larger in females
   and shorter axial length; no association with age/BMI/BP/diabetes/smoking/CKD;
   OCTA superior to fluorescein for FAZ discrimination; FAZ changes in diabetic eye
   disease, vascular occlusions; biomarker in MS / Alzheimer / Parkinson / IBD.
2. **Ghassemi et al., J Curr Ophthalmol 2017** (PMID 29270477) — superficial FAZ 0.27 mm2
   vs deep FAZ 0.35 mm2 (P < 0.001), r = 0.82; 224 eyes of 112 volunteers.
3. **Yoshimura et al., TVST 2026** (PMID 41769944) — FAZ definition sentence; astrocyte-
   coupling model recapitulating arcades, FAZ formation and radially inward perifoveal
   vascular pattern.
4. **Hasegawa et al., Sci Rep 2026** (PMID 41667614) — elderly normative 0.35 ± 0.12 mm2;
   FAZ centre lies 41.6 ± 21.1 µm from the foveal photoreceptor (foveal bulge) centre.
5. **Wei et al., Clin Ophthalmol 2025** (PMID 41019873) — FAZ enlarges before visible DR:
   control 0.278 → NDR 0.308 → NPDR 0.351 mm2; positive correlation with diabetes
   duration and BMI.

## Files changed
- Knowledge_Base/Retina/macula-fovea.json  1.3.0 → **1.4.0** (location/blood_supply/clinical: FAZ block; keywords +9)
- Knowledge_Base/Retina/photoreceptor-layer.json  1.2.0 → **1.3.0** (1:1 ratio sentence, p. 467)
- Knowledge_Base/Choroid/choriocapillaris.json  1.1.0 → **1.2.0** (p. 396 micro-details: 30 nm diaphragm, sloping interfaces, arteriole-vs-net junction contrast, collagenous framework + supracapillary layer)
- schemas/common/references.json  67 → **72** (+5)
- Anatomy_Extraction_Master_Tracker_v2.xlsx (rows 12 / 43 / 72)
- RETINAL_VESSELS_MACULA_STAGING.md (new section I)

## QA
- Verbatim quote verification before writing: **23/23 PASS** (5 of them from the book pastes, saved in download/sources/book_pastes/).
- validate.py: **72/72 OK** · pytest: 10 passed + 14 subtests passed.

## Still open
- **RV-001** (retinal vessels: arcades / two capillary networks / CRA / CRV) awaits Wolff ch.14 pages ~printed 489–494.
- printed 663 → candidate for a future **ocular-adnexae development** card.
