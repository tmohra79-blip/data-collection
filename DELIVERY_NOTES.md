# Conjunctiva Enrichment Delivery — CONJ-002 v1.1.0 + CONJ-003 v1.1.0 (2026-10-19)

## 1. What this package contains

| File | Purpose |
|---|---|
| `Knowledge_Base/Conjunctiva/palpebral-conjunctiva.json` | CONJ-002 **v1.0.0 → v1.1.0** (1,428 → **2,417 words**) |
| `Knowledge_Base/Conjunctiva/conjunctival-fornix.json` | CONJ-003 **v1.0.0 → v1.1.0** (1,062 → **1,766 words**) |
| `schemas/common/references.json` | 9 → **12 sources** (cumulative, append-only) |
| `Anatomy_Extraction_Master_Tracker_v2.xlsx` | Rows 8/9 (CONJ-002/003) updated — pages, status, notes |
| `DELIVERY_NOTES.md` | This note |

Bulbar conjunctiva (CONJ-001 v1.3.0) and the corneal cards are NOT touched.

## 2. Sources read in full this session (evidence chain)

1. **Wolff printed 150 (PDF 160)** — `3333.pdf`, visual read. The previously missing page: completion of
   *SUSPENSORY LIGAMENTS OF THE FORNICES* (superior suspensory ligament — cut in ptosis surgery →
   conjunctival prolapse, Collin 1983; inferior suspensory ligament — involutional retractor laxity →
   lower fornix shallowed) + §4.21 smooth muscle of the orbit (Müller's 15–20 mm × 10 mm, pretrasal-space
   limitation, lacrimal-gland slip) + start of INFERIOR PALPEBRAL MUSCLE (continues on printed 151).
2. **statpearls_conjunctiva** NBK519502 (2023-08-28) — re-read with focus on palpebral/fornix content
   (lid layering, 3–5 strata, substantia propria uniqueness, goblet-cell gradient, CALT/suppressor T-cells,
   regional innervation, arcade supply, staining/grading).
3. **statpearls_muller_muscle** NBK540964 (2024-10-05) — NEW registry entry. Function (+2 mm sympathetic
   elevation), embryology (weeks 12/14), insertion patterns 1/2M/2L/3, sympathetic route, TED/Horner, MMCR.
4. **statpearls_gfs** NBK582141 (2023-07-18) — NEW registry entry. Normal fornix depths 15.3/10.9 mm
   (Khan 2014), GFS mechanism/pathogens/management incl. povidone-iodine fornix swabs and MMCR-based resection.
5. **statpearls_conjunctivitis** NBK541034 (2026-09-08) — NEW registry entry. Papillary vs follicular
   histopathology, GPC/FES/VKC/AKC/trachoma tarsal geography, double lid eversion, fornix reconstruction,
   cicatricial fornix shortening (MMP/AKC).

The four StatPearls texts were fetched verbatim from NCBI Bookshelf (via the `/sites/books/` path; the
classic path is captcha-gated from this environment) and are archived in the project
`download/sources/` — every added fact was verified against these saved copies by exact-quote checking
(**48/48 passed**) before writing.

## 3. Cross-source concordances worth knowing

- Müller's muscle size: Wolff **15–20 mm × 10 mm** vs StatPearls **~15 mm × 10 mm** (both recorded).
- Fornix depth: Whitnall/Wolff from-margin 13/9/5 mm vs Khan 2014 **15.3/10.9 mm** — different measuring
  conventions; both kept with attribution and an explicit do-not-mix caveat.
- GFS aetiology (levator aponeurosis degradation → deep fornix) independently corroborates Wolff's
  suspensory apparatus — recorded as a synthesis note with per-fact sourcing.
- Marginal tarsal arcades supply palpebral conjunctiva + fornices: Wolff and StatPearls agree.

## 4. Mechanical QA after enrichment

- `validate.py` → **8 passed, 0 failed, 0 skipped** (5 corneal + 3 conjunctival cards).
- `tests/test_validate.py` → **10 passed + 14 subtests**.
- `references.json` → 12 entries; every new `reference_id` cited in the cards resolves in the registry.

## 5. Suggested PR steps

1. Copy both JSON files into `Knowledge_Base/Conjunctiva/` (replacing the v1.0.0 files).
2. Copy `schemas/common/references.json` (12 sources).
3. Commit the updated tracker xlsx (rows 8/9 only; all other rows untouched).
4. Run: `python validate.py schemas Knowledge_Base` → expect `8 passed, 0 failed, 0 skipped`.
5. Run: `python -m pytest tests/ -q` → expect `10 passed, 14 subtests passed`.
6. Open the PR and reference this note.

## 6. Known follow-ups (no invention)

- Printed 151 (continuation of INFERIOR PALPEBRAL MUSCLE text) — flagged for a future v1.2.x sharpening.
- Conjunctivitis as the first **disease** card (Disease.schema.json) remains the next planned entity;
  NBK541034/NBK582141 give it a strong head start.


---

## Choroid Knowledge Base — 7 new cards (v1.0.0, 2026-10-27)

Built from the complete Chapter 11 (The choroid and uveal vessels, printed pp. 371-410) plus cross-chapter harvest
(ch2 topography 212-228; ch3 orbital vessels 88/101; ch7 sclera relations 274-277; ch8 angle 302; ch14 RPE/foveola
454-464; ch15 optic nerve head 500-535; ch16 autonomic innervation 606-619; ch17 development 637-640). Every fact is
traceable to printed pages; verbatim quotes preserved in `CHOROID_STAGING_EXTRACTS.md` (sections A-K).

| ID | JSON | Fields documented | Content words |
|---|---|---|---|
| CHO-001 | choroid.json | 8/8 | 1,343 |
| CHO-002 | choroid-layers.json | 8/8 | 1,047 |
| CHO-003 | choriocapillaris.json | 7/8 | 892 |
| CHO-004 | choroid-blood-supply.json | 8/8 | 1,028 |
| CHO-005 | vortex-veins.json | 7/8 | 780 |
| CHO-006 | suprachoroidal-space.json | 8/8 | 731 |
| CHO-007 | choroid-innervation.json | 5/8 | 839 |

**Total: 6,660 words across 7 cards. QA: validate.py 46/46 passed; pytest 10 + 14 subtests green (2026-10-27).**

Notes for reviewers:
- **component_ids**: the eye model component registry contains no choroid component; all 7 cards therefore use
  `["comp_sclera", "comp_retina"]` (the choroid is the intermediate coat bounded by both). If a `comp_choroid` is ever
  added to the mapping document, switch the cards to it.
- **Versioning**: all cards start at 1.0.0 with priority 1 (High). Reference registry unchanged — all content cites
  `wolff_anatomy` with chapter/page-level sources.
- **Highlights**: innervation card documents the triple coexpression (muscarinic + VIPergic + nitrergic) and the
  rami oculares quantitative account (ch16 p. 606-607); choriocapillaris card carries the Hayreh-vs-Fryczkowski
  lobule geometry dispute and the 15 mmHg osmotic anchoring of the retina; vortex veins card carries the full
  Rutnin 1967 numbers and the Maltese-cross watershed; the blood-supply card integrates the optic-nerve-head
  data (10%/30% prelaminar contribution, Zinn-Haller branches).
- **Remaining gaps (documented, non-blocking)**: full journal citations for Rutnin 1967 / Weiter & Ernest 1974 /
  Ring & Fujino 1967 await the book's reference pages after letter H; the tracker rows for these cards mark
  Medical Review and downstream pipeline stages as pending, consistent with all existing cards.

---

## Choroid article enrichment — 7 cards v1.0.0 → v1.1.0 (2026-10-27)

External journal-article support added on top of the Wolff-only v1.0.0 build. All 13 articles were
verified on 2026-10-27 (PubMed was captcha-gated from this environment; citations/abstracts were read
on Europe PMC, PMC full texts, Nature, BJO and Johns Hopkins Pure). Every added fact carries its
citation inside the card text plus a `section`-level source entry, and the enrichment is
guard-protected against double-application.

| Card | Words | Sources registered per card |
|---|---|---|
| choroid.json | 1,343 → 1,567 | nickla_2010_choroid, margolis_2009_edi_oct |
| choroid-layers.json | 1,047 → 1,188 | ramrattan_1994_aging, nivison_smith_2020_aging_angio |
| choriocapillaris.json | 892 → 1,106 | fryczkowski_1991_lobular, zouache_2016_segmented, ramrattan_1994_aging, nickla_2010_choroid |
| choroid-blood-supply.json | 1,028 → 1,138 | alm_bill_1973_flow, reiner_2018_neural_control, nickla_2010_choroid |
| vortex-veins.json | 780 → 943 | verma_2021_vortex_imaging, lim_1995_exit_sites, hayreh_baines_1973_vortex |
| suprachoroidal-space.json | 731 → 840 | chiang_2018_scs |
| choroid-innervation.json | 839 → 1,005 | reiner_2018_neural_control |

**Totals: 6,660 → 7,787 words; references.json 36 → 49 entries; QA: validate.py 46/46 passed,
pytest 10 + 14 subtests green (2026-10-27). Tracker rows 41-47: Notes column only.**

Gap-closure note: the previously documented "remaining gaps" for full journal citations of
Rutnin 1967 / Hayreh & Baines 1973 / Fryczkowski 1991 are now closed with exact citations
(Am J Ophthalmol 1967;64:821-839; BJO 1973;57(4):217; Int Ophthalmol 1991;15(2):109-120).
Weiter & Ernest 1974 and Ring & Fujino 1967 still await the book's reference pages after letter H.

Package: `choroid-kb-enrichment-v110-delivery.zip` — 7 cards + references.json (49) + tracker (47 rows)
+ this note.
