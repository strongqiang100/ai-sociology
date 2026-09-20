# 07 · FAQ

[← Install](06-install.md) · [Documentation index](README.md) · [Next: Roadmap →](08-roadmap.md)

---

## About the project

<details>
<summary><b>Is this just another prompt collection?</b></summary>

<br>

No, and the difference is testable. A prompt collection optimises the output of one conversation. This
is a reasoning framework with stated axioms, derived conclusions, and an explicit rule that **any
forecast must carry a falsification condition**.

You can check it: pick any claim in [module 01](../experts/ai-sociology/skills/ai-sociology-framework/references/01_公理定理与推演链.md)
and trace it back to a premise. If you cannot, that is a bug worth reporting.
</details>

<details>
<summary><b>Why give away the whole framework if it is valuable?</b></summary>

<br>

Because its value is the **method**, and methods are not lost by being read. Someone can copy every
sentence here and still not be able to judge with it — that capacity is not in the text.

The alternative (holding it back) only reduces how many people can develop the capacity, without
making the holder's own capacity any sharper.
</details>

<details>
<summary><b>Why is the framework split into an expert <i>and</i> skills?</b></summary>

<br>

They are two delivery forms of the same content, and they behave differently:

- **An expert** is a role you summon. It has an identity, a scope and a knowledge library.
- **A skill** is procedure that the AI triggers automatically inside any conversation.

A skill answers "help me work through this". An expert answers "I want to think as this role". Both
have their place, so both ship.
</details>

<details>
<summary><b>Why do the sub-experts each handle only one question?</b></summary>

<br>

Because overlap is fatal. If two assets answer the same question, users cannot tell which to install,
and both lose. Each sub-expert therefore has a scope that does not intersect the others.

For questions that genuinely need several angles, there is the roundtable.
</details>

<details>
<summary><b>Why are the roundtable members' names so unusual?</b></summary>

<br>

Each is a surname plus a given name that conceals the function and reads as an ordinary person's name
without explanation. The platform's team specification requires this — it explicitly forbids single
characters, bare job titles, doubled syllables, phrases rather than names, and names that merely
repeat the profession field.

They also solve a real problem: seven seats all sharing one avatar are indistinguishable in a
marketplace. Distinctive names do the distinguishing instead.
</details>

---

## Using the assets

<details>
<summary><b>Can I change an expert's avatar after submitting?</b></summary>

<br>

Yes, but **with a caveat that catches people out**.

| | Expert | Skill |
| :--- | :--- | :--- |
| Avatar source | Parsed from the package | Uploaded in the UI |
| Editable on the confirmation page | **No** — read-only preview | **Yes** |

For an expert you must go back to **step 1 of the submission flow ("Configure expert")** and re-upload
the package. There is no upload button on the confirmation page because the avatar is not a form field
there — it is parsed.

**Do not create a new expert just to change an avatar.** That generates a new expert ID and may
collide with an identifier that is already taken.
</details>

<details>
<summary><b>Can I rename an expert?</b></summary>

<br>

Two different things are being called "the name":

| Layer | Field | Unique? | Changeable? |
| :--- | :--- | :--- | :--- |
| Expert identifier | `name` in `plugin.json` | **Yes, globally** | **No — locked at release** |
| Display name | `displayName` | **No requirement** | Yes |

**What is reserved is the identifier, not the display name.** Someone else can publish an expert with
the same display name as long as their identifier differs, and the platform will not intervene.

If you want exclusivity, there are only two routes: recognisability inside the platform (avatar, name
and introduction as one identity — this is a de facto brand, not an exclusive right), or a trademark.
Note that descriptive Chinese terms have weak distinctiveness and are commonly refused, so a coined
term is usually the better trademark.
</details>

<details>
<summary><b>How many experts or skills can one person publish?</b></summary>

<br>

There is no published limit on the number of experts, skills or connectors. **The real constraint is
human review**, not a quota.

What is limited is the **developer account**: one identity document can register one personal entity
platform-wide. A personal entity can publish experts, expert teams, skills and connectors — **Buddy
applications require corporate verification**.
</details>

<details>
<summary><b>Is there a way for creators to earn from this?</b></summary>

<br>

Yes. The platform has a **revenue** section: after opening a payout account, you can publish skills or
experts to the marketplace at your own price, and withdraw after settlement. Platform fees are
currently waived during the beta period, with a 0.6% payment processing fee.

Three constraints matter:

- **Payment model is locked at release** — one-off, monthly, or free. Decide before you publish
- Price range: **1–999** (per unit or per month, integer)
- To open a payout account you need: completed developer verification, no account violations, and
  **at least one asset that has passed review**

> **Earlier versions of this document said the platform offered no revenue mechanism. That was wrong.**
> The conclusion came from reading only the public documentation. The mechanism is visible in the
> platform's own interface. **Lesson: to check what a platform can do, read the interface, not only the
> docs.**
</details>

<details>
<summary><b>Why does the framework say judgement-type assets will not get traffic from search?</b></summary>

<br>

Because **nobody wakes up wanting to install a skill that judges where humans stand.**

They install a PDF skill because they have a PDF today. A judgement need has no "needed today"
trigger — it lives inside a state of confusion, not on a to-do list.

So the honest position is: this project's value is **trust, attribution and being a companion to
content**, not a traffic channel. See [09 · Market notes](09-market-notes.md).
</details>

---

## Content and boundaries

<details>
<summary><b>Can I use this commercially?</b></summary>

<br>

Yes. [MIT](../LICENSE) permits commercial use, modification and redistribution; the only requirement
is retaining the copyright notice.

**One thing that is not covered**: the avatar image. It is a person's likeness and is not licensed
with the project. Replace it if you fork.

**One request that is not a licence term**: the value here is the method. Using it to reach better
judgements is its purpose. Repackaging it as a certain answer and selling it runs the other way.
</details>

<details>
<summary><b>Is this investment advice?</b></summary>

<br>

**No.** Module 12 covers industry and supply-chain structure as a research frame only. It makes no
judgement on any instrument, and the boundary is carried on every output.

On money decisions, consult a licensed professional.
</details>

<details>
<summary><b>I am genuinely struggling. Can this help?</b></summary>

<br>

This is the one question worth answering plainly.

The anxiety material here is a **structural** tool: it separates four different anxieties and replaces
an unanswerable question with a trackable list. That can genuinely reduce the sense of being out of
control.

**It is not therapy and it does not diagnose anything.** If you have persistent insomnia, impaired
functioning, or any thought of harming yourself or others — **please seek professional help.** That
takes precedence over everything in this repository.
</details>

<details>
<summary><b>Why does the framework refuse to say whether AI is good or bad?</b></summary>

<br>

Because that question cannot be answered as phrased. The framework replaces it with a sequence of
answerable ones.

Underneath is a specific reason. Optimism and pessimism are both positions, and positions end
discussions. **Variables continue them.** A forecast with a criterion, a horizon and a falsification
condition can be checked later; "AI will change everything" cannot.
</details>

<details>
<summary><b>What does "late is not never - only delayed" actually mean?</b></summary>

<br>

It is a counter to the most common false comfort.

When someone points out that on-site work (manufacturing, care, installation) is slower to automate,
the tempting conclusion is "so those jobs are safe". That is the error: the physical chain changes the
**pace**, not the **direction**. Every link gets solved, and when one is resolved the pressure moves
to the next.

So the correct reading is: **you have time — use it.** Not: **you do not need to worry.**
</details>

---

## Contributing

<details>
<summary><b>I disagree with a judgement. Where does that go?</b></summary>

<br>

A [content discussion issue](https://github.com/strongqiang100/ai-sociology/issues/new/choose).
Disagreement is the point of a reasoning framework.

The most useful objections do one of three things: identify a variable the framework ignores, point out
a claim stated as a law that is actually an assumption, or supply a data anchor with a source and a
year to replace a "to be verified" placeholder.
</details>

<details>
<summary><b>What is the most common contribution mistake?</b></summary>

<br>

**Writing a module into `references/` without registering it in the navigation tables.**

A module that is not in a navigation table is never read by the AI during a conversation. The file
exists, the work is correct, and it has no effect.

Registration means four places: the framework `SKILL.md`, the main expert's agent file, the expert's
`README.md`, and [`02-framework.md`](02-framework.md).
</details>

---

[← Install](06-install.md) · [Documentation index](README.md) · [Next: Roadmap →](08-roadmap.md)
