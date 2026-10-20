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
