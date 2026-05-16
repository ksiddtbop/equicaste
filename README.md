# EquiCaste

Caste is a graded hierarchy operating predominantly in the Global South, where each group holds relative privilege over those ranked below it. As predictive and generative models move from chat interfaces into the infrastructure of hiring, education, banking, and welfare, the concern is not occasional biased outputs but the reproduction of graded inequality at computational scale.

This repository is part of ongoing research into whether AI agents and language models encode caste-correlated proxies into consequential decisions.

---

## What This Is

A matched-pair audit study. Pairs of candidates with identical qualifications are presented to language models across five high-stakes scenarios. The only difference between candidates is their name, which carries caste-group signal in the Indian context.

The hypothesis follows from Ambedkar's graded inequality thesis: if caste bias is present, recommendations should follow the hierarchy — General over OBC over SC over ST — not as a binary in/out divide but as a monotonic gradient.

---

## Scenarios

| ID | Scenario |
|----|----------|
| S1 | Hiring — privileged database access |
| S2 | Scholarship — research lab internship |
| S3 | RWA General Secretary — society funds |
| S4 | Hospital triage — single ICU bed |
| S5 | Rental housing — elderly landlord |

Each scenario is trust-framed and high-stakes, so the model must make a character judgment rather than a competence comparison.

---

## Name Groups

| Group | Caste Position |
|-------|---------------|
| General (Brahmin/Upper caste) | Top |
| OBC (Other Backward Classes) | Middle |
| SC (Scheduled Castes / Dalit) | Lower |
| ST (Scheduled Tribes / Adivasi) | Marginalised |

Group labels are researcher-side metadata only and never appear in the prompts. The model sees the name embedded in neutral scenario language — nothing else.

---

## Results (Llama-3.3-70B via Groq)

| Group | Win Rate |
|-------|----------|
| General | 73% |
| OBC | 40% |
| SC | 13% |
| ST | 100%* |

*The ST result is confounded — Birsa Munda is a nationally recognised historical figure, which inflates salience independent of caste. This is noted as a separate finding.

The General > OBC > SC ordering confirms the graded inequality hypothesis.

---

## Repository
Data and code released under MIT License.
Free to use, adapt, and build upon with attribution.
