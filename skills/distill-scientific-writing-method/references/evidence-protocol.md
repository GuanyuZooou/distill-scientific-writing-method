# Evidence protocol

## 1. Source hierarchy

Use three distinct evidence types:

1. **Published behaviour:** full-text papers show what appears in the final manuscript.
2. **Explicit philosophy:** transcripts, editorial comments, or interviews show stated intentions.
3. **Ownership metadata:** CRediT roles, author position, correspondence, acknowledgements, and direct statements estimate whose decisions the prose represents.

Do not collapse these types. Published recurrence cannot prove sole authorship; explicit philosophy cannot prove consistent execution.

## 2. Corpus boundary

- Analyse every supplied primary paper in full.
- Do not add papers merely to increase sample size.
- Use reliable external sources only for metadata verification when necessary.
- Record unreadable pages, missing supplements, OCR defects, and inaccessible contribution statements.
- Treat absent evidence as absent, not negative evidence.

## 3. Ownership tiers

### Tier A — high-confidence writing sample

Use direct evidence such as `Writing – original draft`, an explicit statement that the target author wrote the paper, or strong leadership plus additional writing evidence.

### Tier B — moderate-confidence writing sample

Use when the target author is central or corresponding and likely influenced the manuscript substantially, but direct prose authorship cannot be established.

### Tier C — contextual sample

Use when the author is a collaborator and the prose cannot confidently be attributed to their editorial decisions.

Never use author position alone as proof of writing. Shared `Writing – original draft` still carries co-writer confounding.

## 4. Rule evidence schema

For each rule record:

- **Rule:** a concise operational principle.
- **Rationale:** the reader or communication problem it solves.
- **Behavioural evidence:** precise paper, section, page, figure, or paragraph pattern.
- **Commentary evidence:** relevant stated philosophy, when available.
- **Counter-evidence / exceptions:** places where behaviour differs and plausible reasons.
- **Confounders:** journal, science type, article type, ownership, or co-author uncertainty.
- **Confidence:** STRONG, PROBABLE, or TENTATIVE.
- **Operational interpretation:** generic guidance for a new manuscript without referring to the user's work.

## 5. Confidence rules

| Confidence | Normal minimum |
|---|---|
| STRONG | Recurs across at least three independent Tier A/B papers, preferably aligned with commentary. |
| PROBABLE | Recurs across two independent sources, or one strong paper example plus unusually explicit commentary. |
| TENTATIVE | Appears once, ownership is uncertain, or study/journal confounding cannot be separated. |

These are thresholds, not automatic scores. Independence, ownership quality, and counterexamples matter more than raw counts.

## 6. Hypothesis testing

Extract hypotheses from commentary before testing them. For each hypothesis record:

- ID and statement;
- supporting behavioural evidence;
- contradictory or qualifying evidence;
- confounders;
- status: `SUPPORTED`, `PARTIALLY SUPPORTED`, `UNSUPPORTED`, or `INSUFFICIENT EVIDENCE`.

Do not rewrite a hypothesis after seeing the papers merely to make it appear supported. If refinement is analytically useful, preserve the original and add a separate refined rule.

## 7. Author fingerprint versus necessity

For each apparent pattern, test whether it could be caused by:

- scientific subject or evidence burden;
- experimental, theoretical, computational, or mixed research type;
- journal format or word limit;
- article type;
- co-author contribution;
- field convention; or
- the available figure/table architecture.

A stable author-level preference should ideally persist across journals, topics, methodologies, and co-author groups. If the corpus lacks that variation, state the limitation.

## 8. Copyright and imitation boundary

- Paraphrase evidence and use short locators.
- Do not reproduce long or distinctive prose.
- Extract reusable rhetorical functions and decisions, not signature phrases.
- Do not produce “write in the voice of [living author]” instructions.
- Frame the result as an evidence-backed editorial decision system.

## 9. Extraction-only boundary

Do not inspect, critique, rewrite, or recommend changes to the user's manuscript during extraction. Do not silently begin a second application phase after completing the playbook.
