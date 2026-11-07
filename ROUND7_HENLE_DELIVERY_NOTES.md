# ROUND 7 — Henle's Fiber Layer Completion (2026-11-07, v3 package)

## What was asked
User audited the 6 macula-region terms: Macula Lutea / Fovea Centralis / Foveola /
Umbo / Foveal Avascular Zone / Henle's Fiber Layer — "have we collected all of them?"

## Coverage audit (against the actual cards)
| Term | Status before | Documented in |
|---|---|---|
| Macula Lutea | complete | macula-fovea.json |
| Fovea Centralis | complete | macula-fovea.json |
| Foveola | complete | macula-fovea.json |
| Umbo | complete (round 5, v1.3.0) | macula-fovea.json |
| Foveal Avascular Zone | complete (round 6, v1.4.0) | macula-fovea.json |
| **Henle's Fiber Layer** | **thin** — only the macular-OPL mention from Wolff (pp. 227/474) | outer-plexiform-layer.json |

## External sources (6 new + 2 reused, all quote-verified 29/29)
1. **Koksaldi et al., Med Hypothesis Discov Innov Ophthalmol 2025** (PMID 40787281, reused ref) —
   dedicated HFL section: outer two-thirds of macular OPL = radial cone axons + Muller processes;
   radial extent 5500 um / absent beyond 8500 um; near-parallel to ILM at foveola edge -> petaloid
   patterns; axons ~558 um, first synapses ~350 um; **highest macular pigment concentration in HFL**;
   macular star / radial CME / petaloid hemorrhage; hyperreflective HFL over drusen; ASHH sign.
2. **Wong-Fortunato et al., IOVS 2026** (PMID 42610579) — AAV-EGFP visualizes Henle fibers in vivo
   (macaque); bundles 30.0 +/- 2.2 proximal (0.5 mm) vs 60.3 +/- 2.5 distal (1.25 mm) lines,
   consistent between individuals, converging toward the fovea; macular-star lipid sits at HFL level.
3. **Lujan et al., IOVS 2011** (PMID 21071737, abstract) — directional HFL reflectivity; including
   HFL inflates central ONL thickness by 52%.
4. **Drasdo et al., Vision Res 2007** (PMID 17320143, abstract) — Henle fibers 406-675 um in radial
   sections, "substantially longer than previously reported".
5. **Ramtohul et al., Prog Retin Eye Res 2023** (PMID 36333227, abstract) — HFL = bundles of
   unmyelinated photoreceptor axons + outer Muller processes; ASHH pathoanatomy review.
6. **Ruiz-Moreno et al., Diagnostics 2026** (PMID 42121989) — SNIFR: schisis at HFL/OPL with
   spoke-wheel en face pattern; HFL = structural weak point under shearing traction.
7. **Bringmann et al., PLoS One 2022** (PMID 35417487) — Henle fibers compensate the inner/outer
   retinal spatial shift; cystoid spaces surrounded by Henle fiber bundles in high-grade foveal
   hypoplasia.
8. **Kar et al., Front Cell Neurosci 2024** (PMID 38994326, reused ref) — Muller glia = 80% of HFL
   volume (95% of foveal floor).

## Files changed
- Knowledge_Base/Retina/outer-plexiform-layer.json  1.1.0 -> **1.2.0** (dedicated HFL block in
  definition/location/layers/histology/clinical; aliases +3; keywords +19 EN+AR; field provenance)
- Knowledge_Base/Retina/macula-fovea.json  1.4.0 -> **1.5.0** (pigment-HFL sentence + keyword)
- schemas/common/references.json  72 -> **78** (+6)
- Anatomy_Extraction_Master_Tracker_v2.xlsx (rows 14 RET-005 + 72 RV-002)
- RETINAL_VESSELS_MACULA_STAGING.md (new section J)

## QA
- Verbatim quote verification before writing: **29/29 PASS** (source texts saved in download/sources/).
- validate.py: **72/72 OK** | pytest: 10 passed + 14 subtests passed.
- All card reference_ids resolve in references.json; no placeholders; no duplicate keywords/aliases.

## Result
All 6 terms of the user's checklist are now fully documented — five in macula-fovea.json (v1.5.0)
and Henle's Fiber Layer in outer-plexiform-layer.json (v1.2.0, 2,465 words, 53 Henle mentions,
8 sources).

## Still open
- **RV-001** (retinal vessels) awaits Wolff ch.14 pages ~printed 489-494.
- printed 663 -> candidate for a future ocular-adnexae development card.
