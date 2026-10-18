# Eye Anatomy Knowledge Base Construction Manual

> **Project:** AI-Powered Ophthalmology Educational System (RAG)

> **Version:** 0.1 (Living Document)

> **Purpose:** This document is the single reference that will be updated throughout the project.

---

# Table of Contents

- Chapter 1 – Project Overview
- Chapter 2 – Knowledge Base Workflow
- Chapter 3 – Anatomy Schema
- Chapter 4 – Extraction Rules
- Chapter 5 – Extraction Map
- Chapter 6 –Progress Log

---

# Chapter 1 – Project Overview

## Goal

Build a reliable medical knowledge base that powers the AI tutor.

The AI should:
- Explain any anatomical structure selected in the 3D eye model.
- Answer students' questions using RAG.
- Rely only on trusted medical references.

---

# Chapter 2 – Knowledge Base Workflow

```text
Medical Book
      ↓
Choose Anatomical Entity
      ↓
Extract Information
      ↓
Review
      ↓
Create JSON
      ↓
Preprocessing
      ↓
Chunking
      ↓
Embedding
      ↓
RAG
```

---

# Chapter 3 – Anatomy Schema

For every anatomical entity we will extract:

- Definition
- Location
- Boundaries
- Relations
- Histology
- Blood Supply (if applicable)
- Venous Drainage (if applicable)
- Innervation (if applicable)
- Clinical Importance

> Function will be documented later under the Physiology section.

---

# Chapter 4 – Extraction Rules

1. Use trusted medical references only.
2. Never invent missing information.
3. One entity = One JSON file.
4. Avoid duplicate information.
5. Keep medical terminology consistent.
6. Review every JSON before approval.
7. Describe the anatomical entity itself, not the parent structure.

---

# Chapter 5 – Extraction Map

| Main Structure | Example Substructures |
|----------------|----------------------|
| Cornea | Epithelium, Bowman's Layer, Stroma, Descemet's Membrane, Endothelium |
| Retina | RPE, Photoreceptor Layer, Nuclear Layers, Ganglion Cell Layer |
| Lens | Lens Capsule, Cortex, Nucleus |
| Iris | Stroma, Sphincter Muscle, Dilator Muscle |

---

# Chapter 6 – Progress Log

This section will be updated after every completed entity.

## Cornea (5/5 complete — validated)

- [x] Corneal Epithelium
- [x] Bowman's Layer
- [x] Stroma
- [x] Descemet's Membrane
- [x] Corneal Endothelium

## Retina (10/10 complete — validated)

Source: Wolff's Anatomy of the Eye and Orbit, 8th edition — Chapter 14, The Retina (pp. 454–487).

- [x] RET-001 Retinal Pigment Epithelium (RPE)
- [x] RET-002 Photoreceptor Layer (Layer of Rods and Cones)
- [x] RET-003 External Limiting Membrane (ELM)
- [x] RET-004 Outer Nuclear Layer (ONL)
- [x] RET-005 Outer Plexiform Layer (OPL)
- [x] RET-006 Inner Nuclear Layer (INL) — v1.1.0
- [x] RET-007 Inner Plexiform Layer (IPL) — v1.1.0
- [x] RET-008 Ganglion Cell Layer (GCL) — v1.1.0
- [x] RET-009 Nerve Fibre Layer (NFL) — v1.1.0
- [x] RET-010 Internal Limiting Membrane (ILM)

> **Enrichment note:** The four inner layers (INL, IPL, GCL, NFL) were enriched to v1.1.0 with documented venous drainage — central retinal vein → superior/inferior ophthalmic veins → cavernous sinus — sourced from Wolff Ch.3 (pp. 98–102) and Ch.15 (pp. 489–492). The ILM card additionally incorporates the inner limiting membrane of Elschnig (1901) from Ch.15 (p. 490).

> **Validation:** `python validate.py schemas Knowledge_Base` → 15 passed, 0 failed.

---

**End of Version 0.1**
