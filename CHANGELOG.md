# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Module 17 · Work sites and AI (accountability closure applied to concrete roles)
- Module 18 · City and daily life (where AI cannot reach the physical scene)
- Module 19 · Language and expression (who is speaking, once generation is free)
- Module 20 · Institutions and rules (the layer ordinary people actually collide with)
- English translation of all 16 modules

See [docs/08-roadmap.md](docs/08-roadmap.md) for details.

## [1.0.0] - 2026-09-20

First public release. Fourteen installable assets across three layers, plus the full 16-module
knowledge base.

### Added

**Method layer — 16 knowledge modules**

- Core library (5): axioms, theorems and the reasoning chain · the eight-question variable checklist ·
  expression and topic standards · evidence grading and citation boundaries · practitioner profile
- Tool-oriented extensions (7): tools and workflows · content and copy · video production ·
  cross-border and industry · growth and training · diagnosis and knowledge management ·
  industry and investment observation
- Situation-oriented extensions (4): education and learning · relationships and reality ·
  attention and judgement · evidence and facts
- 5 fill-in templates: trend briefing · variable checklist · topic and script card ·
  claim verification sheet · learning diagnosis card

**Role layer — 8 experts and expert teams**

- `ai-sociology` — the main expert, carrying all 16 modules
- `ai-sociology-roundtable` — a 7-agent expert team: one lead plus six disciplinary seats
  (philosophy, human nature, occupation, society, anxiety, physical limits), staged deliberation,
  five preset workflows
- `ai-sociology-variables` — The Variable Bureau
- `ai-sociology-jobs` — The Job Splitter
- `ai-sociology-learn` — The Right Question
- `ai-sociology-verify` — The Verifier
- `ai-sociology-forecast` — Two Years Out
- `ai-sociology-attention` — The Rememberer

**Tool layer — 6 skills**

- `ai-sociology-variable-audit` — Variable Audit
- `ai-sociology-human-position` — Where Humans Stand
- `ai-sociology-human-nature` — Human Constants
- `ai-sociology-social-strata` — Social Stratification
- `ai-sociology-anxiety-decomp` — Anxiety Decomposition
- `ai-sociology-role-scan` — Role Scan

**Engineering**

- `scripts/validate.py` — validates package structure, required fields, YAML parseability, naming
  rules, directory depth, filename encoding and archive integrity
- GitHub Actions workflow running validation on every push and pull request
- Issue and pull request templates
- `dist/` with packaged archives ready to install

### Notes

- The public builds are de-identified: no real names, company information, employment history, local
  paths, internal document names, private links, or client and channel information.
