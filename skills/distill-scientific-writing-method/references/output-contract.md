# Output contract

Create one extraction directory containing:

| Path | Required content |
|---|---|
| `00_SOURCE_INVENTORY.md` | Corpus, tier assignments, authorship evidence, research types, constraints, confidence, and uncertainties. |
| `01_AUTHOR_READER_MODEL.md` | Reader assumptions and explanation boundaries. |
| `02_NAMING_AND_VOCABULARY.md` | Terminology, labels, abbreviations, variables, and plain-description policy. |
| `03_INFORMATION_SELECTION.md` | Foregrounding, omission, compression, relocation, and information thresholds. |
| `04_DETAIL_AND_DEFENCE_POLICY.md` | Quantification, caveats, validation, claim strength, and minimum sufficient defence. |
| `05_NARRATIVE_ARCHITECTURE.md` | Whole-paper, section, paragraph, and rhetorical sequencing. |
| `06_SENTENCE_PARAGRAPH_PATTERNS.md` | Reusable functional structures without distinctive wording. |
| `07_FIGURE_STORYTELLING.md` | Figure/table order, roles, density, captions, and recall. |
| `08_ANTI_PATTERNS.md` | Evidence-backed criticized or avoided practices. |
| `09_RULE_EVIDENCE_MATRIX.csv` | One row per candidate rule using the schema below. |
| `10_AUTHOR_WRITING_PLAYBOOK.md` | Concise portable decision system plus hypothesis-status appendix. |
| `evidence/` | One Markdown dossier per paper and one per commentary source. |

## Rule matrix schema

Required columns:

```text
rule_id,rule,category,rationale,behavioural_evidence,commentary_evidence,counter_evidence,confounders,tier_quality,confidence,hypothesis_link,operational_interpretation
```

Use compact evidence strings with precise source identifiers. When per-paper columns are useful, add them without removing the required normalized fields.

## Evidence dossier template

```markdown
# Source identity

## Authorship and tier

## Research and publication constraints

## Rhetorical architecture

## Evidence by analysis dimension

## Candidate editorial decisions

## Counterexamples and exceptions

## Confounders and uncertainty
```

## Playbook structure

Organize approximately as:

1. inferred reader model;
2. core editorial philosophy;
3. naming and terminology rules;
4. information-selection rules;
5. detail and quantification rules;
6. minimum-sufficient-defence rules;
7. abstract architecture;
8. introduction architecture;
9. methods or theory architecture;
10. Results and Discussion architecture;
11. figure-led storytelling;
12. sentence and paragraph construction;
13. anti-patterns;
14. “Does the reader need this?” decision framework;
15. “When is enough enough?” stopping rules;
16. quick self-check; and
17. hypothesis-test appendix.

Prioritize conditional decisions over adjectives. Distinguish evidence-backed criteria from synthesis.

## Completion report

Report:

- supplied and successfully parsed paper counts;
- Tier A/B/C counts;
- STRONG/PROBABLE/TENTATIVE rule counts;
- status of every commentary-derived hypothesis;
- five strongest author-level principles;
- three strongest counterexamples or qualifications;
- major remaining uncertainties; and
- what additional source type would most improve confidence.
