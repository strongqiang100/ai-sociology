# 08 · Roadmap

[← FAQ](07-faq.md) · [Documentation index](README.md) · [Next: Market notes →](09-market-notes.md)

---

## Where the project is

**v1.0.0** — shipped 2026-09-20.

| Layer | Delivered |
| :--- | :--- |
| Method | 16 modules (5 core + 11 extension) and 5 templates |
| Role | 8 assets: 1 main expert, 1 expert team of 7 agents, 6 sub-experts |
| Tool | 6 skills |
| Engineering | Validation script, CI, issue and PR templates, packaged archives |

---

## Next: modules 17–20

All four are **situation-oriented**, following the direction set out in
[02 · The framework](02-framework.md): as the project matures it moves from "how to use things"
toward "what has changed for people".

### 17 · Work sites and AI

Applies the accountability loop to concrete roles: who signs, who re-checks, who is held responsible.
This is where the employment thread settles — the longest-running line in the framework, and the one
closest to real questions.

**Core tool**: an accountability map per role, and a check for where the loop is broken.
**Hooks back to**: axiom three · accountability cannot transfer.

### 18 · City and daily life

Where AI cannot reach the physical scene: delivery, housing, public services, medical care. Everyday
situations where "slow" is mistaken for "safe".

**Core tool**: a distinction between tasks that touch the scene and tasks that do not, with the
misreading each one invites.
**Hooks back to**: axiom four · intelligence needs a substrate.

### 19 · Language and expression

Once generation costs approach zero, what happens to *who is speaking*? Tone, identity, translation and
the trust problem underneath all three.

**Core tool**: a three-way split of the speaker (author, generator, publisher) and the accountability
gap that opens between them.
**Hooks back to**: A2 · "it understands me" is not "it acts for me".

### 20 · Institutions and rules

Platform rules, labelling requirements and the allocation of responsibility — **the layer ordinary
people actually collide with**, not a policy analysis.

**Core tool**: a reading of who absorbs the risk when a new one appears and no rule has caught it yet.
**Hooks back to**: axiom three, via the risk-moves-downward mechanism.

> **Module 20 carries a hard boundary**: it describes structures and does not evaluate any country,
> institution or policy. That boundary is non-negotiable.

---

## Also planned

| Item | Notes |
| :--- | :--- |
| **Full English translation of the 16 modules** | `README.en.md` and `docs/` are already in English; the modules themselves are Chinese |
| **A `verify.sh` one-liner** | Wrapper so contributors can validate without knowing the Python path |
| **Archive build script** | Generate `dist/` reproducibly instead of committing the archives |
| **Release automation** | Tag → build → attach archives to a GitHub Release |
| **More data anchors** | Replace remaining "to be verified" placeholders with sourced figures |
| **Evaluation harness** | A small set of questions with expected reasoning shape, to catch regressions |

---

## How directions get chosen

Two tests, in order:

1. **Does it hook back to the main conclusion?** A module that cannot answer "what has this changed for
   ordinary people?" is not a module here.
2. **Does it age?** Tool-oriented modules are superseded by product changes; situation-oriented modules
   are not. **Where the answer is ambiguous, take the one that does not expire.**

---

## What is explicitly not planned

Being clear about this matters as much as the roadmap itself.

| Not planned | Why |
| :--- | :--- |
| **Investment recommendations** | Out of scope by design. The industry material is a research frame only |
| **Psychological diagnosis or therapy** | Out of scope. The anxiety material is structural, and refers to professional help |
| **Political forecasting** | Out of scope |
| **Growth-hacking tactics** | The content material explains why something gets remembered, not how to game distribution |
| **A general-purpose knowledge base** | The single biggest failure mode. Every module must stay hooked to the main line |

---

## Versioning

[Semantic versioning](https://semver.org/spec/v2.0.0.html):

| Change | Version bump |
| :--- | :--- |
| New module or asset | minor |
| Edits to existing content, corrections | patch |
| Restructuring, breaking changes to package layout | major |

Package `version` fields are separate from the repository version: bump the package version whenever
you upload a change to the platform, so it does not collide with an existing release.

---

## Proposing a direction

Open a [feature request](https://github.com/strongqiang100/ai-sociology/issues/new/choose). The template
asks for the relation to the main conclusion, the operational tools it would carry, and its boundaries
— because those are the three things that decide whether it fits.

---

[← FAQ](07-faq.md) · [Documentation index](README.md) · [Next: Market notes →](09-market-notes.md)
