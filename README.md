# Graded Algorithmic Inequality

Caste is a graded hierarchy that operates predominantly in the Global South where each group holds relative privilege over those ranked below it. Dalits, positioned at the bottom, face discrimination and violence that is cumulative across the system rather than attributable to a single dominant group. As predictive and generative models move from chat interfaces into the infrastructure of hiring, education, banking, and welfare, the key concern is not occasional biased outputs but the reproduction of graded inequality at computational scale.

---

## The Problem

Existing scholarship on AI and caste overlooks the mechanisms that keep caste durable. Endogamy reproduces caste across generations, yet it is rarely treated as an auditable factor. Caste is carried forward when it is shielded in the name of culture and tradition, while the practice of untouchability is passed over in silence. Caste-pride networks and platform governance shape what content propagates online, whose speech is amplified, and which anti-caste claims are suppressed.

As B. R. Ambedkar wrote in *Annihilation of Caste*:

> "Caste is not a physical object like a wall of bricks or a line of barbed wire. Caste is a notion, it is a state of the mind."

AI systems trained on historical texts, images, and institutional records inherit this notion, encoding it as an implicit decision rule.

---

## The Argument

This work proposes a cumulative-impact lens: small caste-correlated decisions that appear tolerable in isolation can compound into durable disadvantage when aggregated across millions of automated decisions.

**The central question:** Do AI agents and language models encode caste-correlated proxies into consequential decisions — shortlisting applicants, credit and welfare allocation, criminal records, triage and referrals, eligibility screening?

---

## The Study

To investigate, this study builds a dataset of caste-marked surnames, casteist language, and recorded incidents of caste-based violence, annotated for caste content and severity. Language models and AI agents are then probed under simulated social settings that mirror how caste reproduces itself — including marriage and partnership recommendations, resource distribution, and access to opportunity — allowing latent caste-correlated behaviour to surface in their responses.

---

## Scenarios Tested

| ID | Scenario |
|----|----------|
| S1 | Hiring — privileged database access |
| S2 | Scholarship — research lab internship |
| S3 | RWA General Secretary — society funds |
| S4 | Hospital triage — single ICU bed |
| S5 | Rental housing — elderly landlord |

---

## Results (Llama-3.3-70B via Groq)

| Group | Win Rate |
|-------|----------|
| General | 73% |
| OBC | 40% |
| SC | 13% |
| ST | 100%* |

*The ST result is confounded — Birsa Munda is a nationally recognised historical figure, which inflates name salience independent of caste. This is noted as a separate finding.

The General > OBC > SC ordering confirms the graded inequality hypothesis.

---

## Repository
equicaste/
├── data/
│ ├── names.csv
│ ├── scenarios.csv
│ ├── comparison_names.csv
│ └── prompts_50.csv
├── results/
│ └── results_groq_llama3.csv
└── scripts/
└── groq_runner.py

---
## Run the Experiment
Get a free API key at console.groq.com, then:
pip install groq
python scripts/groq_runner.py
---
## Keywords
caste bias · graded inequality · endogamy · algorithmic auditing · fairness in NLP · agentic AI · matched-pair audit · Dalit · Ambedkar · AI governance
---
## Author
Kunwar Siddharth  
PhD Researcher, UPES Dehradun 
