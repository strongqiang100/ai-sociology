## Summary

<!-- One paragraph. What changes, and why. -->

## Type of change

- [ ] New knowledge module
- [ ] Edit to an existing module
- [ ] New or updated expert / expert team package
- [ ] New or updated skill package
- [ ] Tooling, validation or CI
- [ ] Documentation
- [ ] Other (describe below)

## Related issues

<!-- Closes #, refs # -->

## Checklist

**Content**

- [ ] New modules open with a "relation to the main conclusion" section
- [ ] The module answers *what has this changed for ordinary people?*
- [ ] Operational tools are criteria-based, not checklists
- [ ] Facts, mechanisms, quotations and assumptions are clearly separated
- [ ] Any forecast carries a criterion, a time horizon and a falsification condition
- [ ] Every number has a source and a year, or is marked "to be verified"
- [ ] Relevant boundaries are carried along (investment / psychological / medical / political / none)
- [ ] No structural problem is reduced to personal effort

**Registration** (the step most often forgotten)

- [ ] Registered in `experts/ai-sociology/skills/ai-sociology-framework/SKILL.md`
- [ ] Registered in `experts/ai-sociology/agents/ai-sociology.md`
- [ ] Registered in `experts/ai-sociology/README.md`
- [ ] Registered in `docs/02-framework.md`

> A module that is not in the navigation table will never be read by the AI. The work is wasted.

**Packages**

- [ ] `python3 scripts/validate.py` passes with no problems
- [ ] `version` bumped in any package that is uploaded to the platform
- [ ] `CHANGELOG.md` updated

**De-identification**

- [ ] No real names or company names
- [ ] No employment history or employer names
- [ ] No local absolute paths
- [ ] No internal document names or private links
- [ ] No client, channel or pricing information

## How this was tested

<!-- Paste the validation output. -->

```text
$ python3 scripts/validate.py
```

## Notes for reviewers

<!-- Anything you are unsure about, or a decision you would like a second opinion on. -->
