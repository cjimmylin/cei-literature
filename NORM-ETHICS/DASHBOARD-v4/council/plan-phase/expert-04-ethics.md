# Expert 04 — Normative Ethics / Moral Philosophy

**Council Role:** Verify accuracy of framework descriptions; draft glossary for Tab 0; flag undefined tradition names in existing dashboard.

---

## 1. Assessment of the Five Traditions as Described in the Paper

The introduction (Section 2.3) describes the five traditions accurately and with appropriate philosophical sourcing. Three small issues merit attention:

**a. Consequentialism vs. Utilitarianism.** The paper uses "consequentialism" and "utilitarianism" somewhat interchangeably. Utilitarianism is a *species* of consequentialism (specifically, welfare-maximizing consequentialism). The dashboard field name is `utilitarian_ethics`, but several interpretive panels refer to "consequentialist reasoning" or "consequentialist bias." For a non-philosopher audience the conflation is mostly harmless, but the glossary should note that utilitarianism is the most common form of the broader consequentialist family.

**b. Contractarianism vs. Contractualism.** The paper correctly cites both Rawls and Scanlon under "contractarianism," but strictly speaking Rawls's position is contractarian (self-interested rational choice behind the veil) while Scanlon's is contractualist (reasonable rejectability). The dashboard labels everything "contractarian." This is a defensible simplification for a general audience, but the glossary should acknowledge the dual lineage.

**c. Care Ethics framing.** The paper foregrounds Gilligan's origin story (challenging Kohlberg's justice-centered model). This is historically accurate but risks giving the impression that care ethics is primarily a feminist critique rather than a freestanding moral theory. The glossary should present it as an independent tradition with its own positive claims about relationships and responsiveness.

Overall verdict: **Accurate enough for a scholarly dashboard. No philosophical errors that would mislead readers.**

---

## 2. Drafted Glossary: "Five Ethical Traditions" (for Tab 0)

> **Five Ethical Traditions**
>
> This dashboard evaluates AI ethics benchmarks against five major traditions in moral philosophy. Each tradition answers the question "What makes an action right or wrong?" differently.
>
> **Virtue Ethics** asks what a person of good character would do. Rather than applying rules or calculating outcomes, it focuses on cultivating qualities like courage, honesty, and practical wisdom. A benchmark grounded in virtue ethics would test whether a model can identify what a thoughtful, experienced person would do in a morally complex situation.
>
> **Deontological Ethics** holds that certain actions are right or wrong regardless of their consequences. It centers on duties, rules, and respect for persons. The most famous version, from Immanuel Kant, says you should never treat people merely as tools for your own goals. A deontological benchmark tests whether a model can recognize binding moral rules even when breaking them would produce a better outcome.
>
> **Utilitarian Ethics** judges actions by their results: the right choice is whichever produces the most overall well-being. It requires weighing costs and benefits across everyone affected. A utilitarian benchmark tests whether a model can identify the option that maximizes total welfare, even when that option is emotionally uncomfortable.
>
> **Care Ethics** starts from the observation that human life is built on relationships of dependency and mutual responsibility. It asks what a caring, attentive person would do for someone who depends on them, emphasizing context, empathy, and particular bonds over abstract principles. A care ethics benchmark would test whether a model can attend to relational needs rather than defaulting to impersonal rules.
>
> **Contractarian Ethics** grounds morality in agreement: an action is right if it follows principles that all reasonable people could accept. Drawing on the work of John Rawls and T.M. Scanlon, it asks what rules people would choose if they did not know which position in society they would occupy. A contractarian benchmark tests whether a model can reason about fairness from a position of impartiality.

Word count: ~260. Each entry is 2-3 sentences of definition plus one sentence connecting to benchmark design.

---

## 3. Locations Where Tradition Names Appear Without Definition

I audited the existing v2 dashboard (`index.html`, `data.js`, `data_cross_vendor.js`, `charts.js`, `style.css`). The following locations use tradition names without any inline definition or tooltip:

| Location | Element | Issue |
|----------|---------|-------|
| `index.html` line ~107-111 | Tradition filter dropdown (`<option value="virtue">Virtue</option>`, etc.) | Five bare labels with no tooltip or help text. A first-time user unfamiliar with moral philosophy will not know what these filters mean. |
| `index.html` line ~248 | Tradition Coverage tab intro | Names all five traditions in a list but only describes what the *chart* shows, not what each tradition *is*. |
| `index.html` line ~486 | Trials tab, "framework difficulty hierarchy" | States "Utilitarian reasoning (77% accuracy) is easiest for LLMs; deontological reasoning (50%) is hardest" without explaining why these are distinct or what each involves. |
| `index.html` line ~606 | Cross-Vendor tab, "dose-response hypothesis" | Uses "deontological constraints" and "consequentialist posture" without definition. |
| `index.html` line ~748-752 | Cross-Vendor tab, IH/IB discussion | References "utilitarian philosopher norm" and contrasts IH (instrumental harm) with IB (impartial beneficence) but never explains these are two *components* of utilitarian reasoning. |
| `data_cross_vendor.js` line ~509 | Model profile subtitle | "strongest deontological constraints" used without context. |

**Recommendation for v4:** The glossary above should be placed in Tab 0 ("How to Read This Dashboard") as a reference section. Additionally, the tradition filter dropdown (carried over from v2 into v4) should include a small help icon or `title` attribute with one-line definitions. The Trials and Cross-Vendor tabs should each include a one-sentence parenthetical the first time they use a tradition name, or link back to Tab 0.

---

## 4. Additional Recommendations

1. **Consistency of color-coding.** The v2 CSS assigns specific colors to each tradition (virtue = purple, deontological = blue, utilitarian = orange, contractarian = cyan). Care ethics is conspicuously absent from the `.tradition-dot.active-*` rules in `style.css`. v4 should add `.tradition-dot.active-care` and use the same color vocabulary in the glossary, charts, and filter UI.

2. **"Western" qualifier.** The introduction and one dashboard panel correctly note these are "five Western normative ethics traditions." The glossary should carry this qualifier in its header to preempt any implication of universality. Suggested header: "Five Ethical Traditions (Western Normative Philosophy)."

3. **Avoid "consequentialist bias" without elaboration.** The phrase appears repeatedly in the paper and dashboard as a shorthand for Claim 2. For non-philosophers, "bias" connotes unfairness. The glossary or Tab 0 should clarify that this is a *coverage asymmetry* in the benchmark landscape, not a moral failing of the models themselves.

---

**Word count:** ~1,080
