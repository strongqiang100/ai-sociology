# Security Policy

## Supported Versions

| Version | Supported |
| :--- | :--- |
| 1.0.x | Yes |

## What this repository is

This repository contains documentation, knowledge modules and installable asset packages. **It runs no
server-side code.** `scripts/validate.py` is a local, read-only validator: it opens files inside the
repository and writes nothing except its own output to stdout.

The practical security surface is therefore not classic code execution but the following.

## Reporting a Vulnerability

Please **do not open a public issue** for a security problem. Use one of these private channels:

1. **[GitHub Security Advisories](https://github.com/strongqiang100/ai-sociology/security/advisories/new)** — preferred
2. Direct message to the maintainer [@strongqiang100](https://github.com/strongqiang100)

Please include:

- What the issue is and where it is (file path, asset id)
- Why it matters, and what an attacker could achieve
- Reproduction steps, if applicable
- Any suggested fix

We aim to acknowledge within a few days and to keep you updated on the fix.

## In scope

| Category | Example |
| :--- | :--- |
| **Instruction-level risks** | Content inside `references/` or a `SKILL.md` that could steer an AI agent into unsafe behaviour, exfiltration, or disregarding its own safety rules |
| **Prompt injection vectors** | Text crafted so that a model consuming the module starts following embedded instructions rather than its operator's |
| **Validator flaws** | `scripts/validate.py` passing a package that is actually malformed, or a path-traversal / symlink issue when scanning |
| **CI workflow risks** | Anything in `.github/workflows/` that could execute untrusted code with broader permissions than needed |
| **Dependency risk** | Issues in the optional `pyyaml` dependency as used here |
| **De-identification failure** | Any personal, client or channel information that has leaked into a public package |

## Out of scope

| Category | Why |
| :--- | :--- |
| Disagreement with a judgement in the framework | That is a content discussion — open a normal issue |
| Requests for investment, medical or legal advice | Explicitly out of scope for this project |
| Vulnerabilities in the AI client or the platform used to install these assets | Report to that vendor |
| Psychological or emotional distress | **This is not a security matter. If you are in distress, please seek professional help.** |

## Handling of assets you install

These packages contain instructions that an AI agent will read and follow. Two precautions are
recommended when installing any third-party asset, including ours:

- **Read before installing.** `SKILL.md` and `agents/*.md` are plain text; skim them.
- **Check the scope.** A skill's `allowed-tools` field, where present, declares what it may reach.

## Disclosure Policy

We follow coordinated disclosure: we will work with you on a fix and a timeline, and credit you in the
release notes unless you prefer otherwise.
