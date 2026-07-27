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
- Chapter 6 – Entity Documentation *(Coming Soon)*

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

---

# Chapter 5 – Extraction Map

| Main Structure | Example Substructures |
|----------------|----------------------|
| Cornea | Epithelium, Bowman's Layer, Stroma, Descemet's Membrane, Endothelium |
| Retina | RPE, Photoreceptor Layer, Nuclear Layers, Ganglion Cell Layer |
| Lens | Lens Capsule, Cortex, Nucleus |
| Iris | Stroma, Sphincter Muscle, Dilator Muscle |

---

# Progress Log

This section will be updated after every completed entity.

- [ ] Corneal Epithelium
- [ ] Bowman's Layer
- [ ] Stroma
- [ ] Descemet's Membrane
- [ ] Corneal Endothelium

---

**End of Version 0.1**
