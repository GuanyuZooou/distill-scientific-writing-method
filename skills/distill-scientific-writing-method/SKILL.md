---
name: distill-scientific-writing-method
description: Distill an evidence-backed scientific writing and editorial decision method from a bounded corpus of an author's full-text papers plus optional supervision transcripts, editorial comments, interviews, or contribution metadata. Use when Codex must reverse-engineer how an author selects information, models readers, names concepts, calibrates claims, structures sections and figures, or stops defending a point; audit writing ownership; test stated philosophy against published behaviour; produce per-source dossiers, a rule-evidence matrix, confidence labels, counterexamples, and a portable playbook without imitating distinctive prose.
---

# Distill Scientific Writing Method

Reverse-engineer editorial judgement, not surface mannerisms. Treat the supplied corpus as bounded evidence and produce a portable decision system without copying the target author's voice.

Before analysis, read:

- [references/evidence-protocol.md](references/evidence-protocol.md) for corpus, ownership, confidence, and anti-bias rules;
- [references/analysis-dimensions.md](references/analysis-dimensions.md) for the nine required analytical dimensions; and
- [references/output-contract.md](references/output-contract.md) for deliverables and schemas.

## Establish scope

1. Identify the target author, paper-corpus directory, optional commentary sources, output directory, and requested language.
2. Treat supplied full-text papers as the complete primary corpus unless the user explicitly authorizes expansion.
3. Use external metadata only to verify authorship, CRediT roles, article type, or journal constraints. Never substitute web abstracts or summaries for full-text analysis.
4. Exclude the user's manuscripts and unrelated workspace files unless explicitly placed in the comparison scope.
5. Keep extraction separate from manuscript rewriting. Do not apply the resulting method to a manuscript in the same phase unless explicitly requested.

If a PDF is unreadable, a paper cannot be identified, a critical source is missing, or progress would require invented evidence, stop and report the exact gate.

## Create the extraction workspace

Run:

```text
python scripts/scaffold_extraction.py <output-directory>
```

Do not overwrite a non-empty extraction directory without explicit permission.

## Audit writing ownership first

Inventory every paper before proposing rules. Record citation, year, journal, article and research type, author position, corresponding status, explicit writing contribution, journal constraints, and uncertainty.

Assign:

- **Tier A:** direct evidence of original drafting or substantial prose leadership;
- **Tier B:** central or corresponding involvement with likely influence, but no direct proof of prose authorship;
- **Tier C:** collaboration without enough evidence that the prose reflects the target author's decisions.

Do not equate co-authorship with writing. Let Tier A and B dominate author-level inference. Use Tier C only to support, challenge, or contextualize a pattern.

## Separate behaviour from commentary

Treat papers as evidence of what the author does and transcripts or editorial commentary as evidence of what the author says they intend.

1. Extract commentary-derived candidate hypotheses.
2. Assign stable IDs such as H1, H2, and H3.
3. Test each hypothesis against the papers.
4. Classify it as `SUPPORTED`, `PARTIALLY SUPPORTED`, `UNSUPPORTED`, or `INSUFFICIENT EVIDENCE`.
5. Identify recurring paper behaviours absent from the commentary.

Never promote commentary directly into a rule.

## Analyse every source rhetorically

Read each paper in full, including figures, captions, tables, conclusions, and Supplementary Information references. Understand enough science to identify the communication decision.

Use rhetorical labels selectively: `BACKGROUND`, `PROBLEM`, `GAP`, `OBJECTIVE`, `DEFINITION`, `METHOD`, `DESIGN CHOICE`, `OBSERVATION`, `QUANTIFICATION`, `MECHANISM`, `INTERPRETATION`, `COMPARISON`, `VALIDATION`, `LIMITATION`, `QUALIFICATION`, `IMPLICATION`, `TRANSITION`, and `RECALL`.

Do not mechanically annotate every sentence. Use labels only when they reveal information flow.

## Build source dossiers before cross-source rules

For every paper and commentary source, create one file under `evidence/`. Record:

- source identity and ownership tier;
- section- and page-level behavioural evidence;
- candidate editorial decisions;
- counterexamples and exceptions;
- scientific, journal, article-type, and co-author confounders; and
- provisional confidence.

Prefer compact paraphrases and precise locators. Do not copy long or distinctive passages.

## Infer rules across nine dimensions

Analyse reader model, naming and vocabulary, information selection, detail budget, defensive writing, narrative architecture, sentence and paragraph functions, figure-led storytelling, and anti-patterns.

For every candidate rule, ask:

1. Does it recur across independent Tier A/B papers?
2. Does explicit commentary support or contradict it?
3. What is the strongest counterexample?
4. Could the science, journal, article type, or co-author explain it?
5. Does it describe an editorial decision rather than a generic virtue?

Express rules conditionally and operationally. Prefer “If X, do Y unless Z” to labels such as “clear,” “concise,” or “elegant.”

## Apply confidence thresholds

- Assign **STRONG** normally only after recurrence in at least three independent Tier A/B papers, preferably with commentary support.
- Assign **PROBABLE** after recurrence across at least two independent sources, or one strong paper example plus unusually explicit commentary.
- Assign **TENTATIVE** when observed once, ownership is uncertain, or confounders cannot be separated.

Do not convert isolated observations into rules. Do not promote tentative patterns into hard recommendations.

## Run anti-confirmation-bias checks

Before finalizing:

1. identify at least three mismatches between stated philosophy and paper behaviour when the corpus permits;
2. search for counterexamples to every strongest rule;
3. reconsider transcript-dominated and single-paper rules;
4. check whether Tier C evidence is exerting disproportionate influence;
5. test journal and scientific necessity as alternative explanations; and
6. reject any “simplicity” rule that would remove necessary scientific information.

Do not make the author more internally consistent than the evidence supports.

## Distill the playbook

Write `10_AUTHOR_WRITING_PLAYBOOK.md` as a concise, active-use decision system. Preserve evidence qualifications, but do not concatenate the dossiers. Include the hypothesis-status table as an appendix.

The playbook must help a scientifically competent writer make similar editorial decisions without imitating wording. Do not present a fingerprint as unique unless comparison evidence supports uniqueness.

## Validate completion

Run:

```text
python scripts/validate_extraction.py <output-directory>
```

Resolve all validation errors. Then report corpus size, Tier A/B/C counts, parsing status, rule-confidence counts, hypothesis statuses, five strongest principles, three key counterexamples, uncertainties, and the most informative next corpus additions.

Do not proceed to manuscript rewriting unless the user starts that phase explicitly.
