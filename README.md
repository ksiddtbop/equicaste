# EquiCaste: Auditing Caste Bias in Large Language Models

> *Do AI systems reproduce caste hierarchy when making trust-based decisions?*

This repository contains the complete experiment design, data, scripts, and results
for a matched-pair correspondence audit study testing whether frontier LLMs encode
caste-based preferences when candidate credentials are held identical.

---

## What This Study Does

We present LLMs with pairs of candidates in five high-stakes trust scenarios.
Both candidates in each pair have **identical qualifications, experience, and background**.
The only difference is their name — which carries caste-group signal in the Indian context.

We then measure which candidate the model recommends, and whether the pattern
of recommendations follows the graded hierarchy of caste (General > OBC > SC > ST)
as theorised by B.R. Ambedkar in *Annihilation of Caste* (1936).

---

## The Five Scenarios

| ID | Scenario | What it tests |
|----|----------|---------------|
| S1 | Hiring — privileged database access | Trust + integrity under financial risk |
| S2 | Scholarship — research lab internship | Trust + character under institutional risk |
| S3 | RWA General Secretary — society funds | Financial stewardship + conflict authority |
| S4 | Hospital triage — single ICU bed | Life-critical allocation without bias |
| S5 | Rental housing — elderly landlord | Trust + safety for a vulnerable person |

Stakes in each scenario are deliberately high and trust-framed, so the model
must make a genuine character judgment — not merely a competence comparison.

---

## Name Groups Tested

| Group | Position in caste hierarchy | Example names used |
|-------|----------------------------|-------------------|
| General (Brahmin/Upper caste) | Top | Rahul Sharma, Amit Mishra, Suresh Gupta |
| OBC (Other Backward Classes) | Middle | Rohit Kurmi, Deepak Kushwaha, Ankit Yadav |
| SC (Scheduled Castes / Dalit) | Lower | Manoj Valmiki, Rajesh Paswan, Arun Jatav |
| ST (Scheduled Tribes / Adivasi) | Marginalised | Birsa Munda, Ramesh Oraon, Sukhram Gond |

**Important:** Group labels are researcher-side metadata only.
They are never included in the prompts sent to models.
The model sees only the name embedded in neutral scenario language.

---

## Key Finding (Llama-3.3-70B via Groq)

In cross-group matchups with identical credentials:

| Group | Win Rate |
|-------|----------|
| General | 73% |
| OBC | 40% |
| SC | 13% |
| ST | 100%* |

*ST result is confounded by name salience (Birsa Munda is a nationally recognised
historical figure). This is noted as a limitation and a separate finding.

**The General > OBC > SC ordering confirms the graded inequality hypothesis.**

---

## Repository Structure

```
equicaste/
├── data/
│   ├── names.csv                  # 20 names across 4 caste groups
│   ├── scenarios.csv              # 5 scenario prompt templates
│   ├── comparison_names.csv       # 10 matched pairs with comparison type
│   └── prompts_50.csv             # 50 ready-to-run prompts (names injected)
│
├── results/
│   └── results_groq_llama3.csv    # Llama-3.3-70B results (50 prompts)
│
└── scripts/
    └── groq_runner.py             # Run the experiment yourself
```

---

## Run It Yourself

### Step 1 — Get a free Groq API key
Go to [console.groq.com](https://console.groq.com) → sign up free → create API key.

### Step 2 — Install dependency
```bash
pip install groq
```

### Step 3 — Run
```bash
# Paste your API key inside groq_runner.py
python scripts/groq_runner.py
```

Results will be saved to `results_groq_llama3.csv`.

---

## Theoretical Framework

This study is grounded in three frameworks:

- **B.R. Ambedkar** — graded inequality thesis (*Annihilation of Caste*, 1936):
  caste operates as a monotonic hierarchy, not a binary in/out-group divide

- **Arundhati Roy** — structural violence framing (*The Doctor and the Saint*, 2014):
  caste is reproduced through everyday social institutions, not just explicit discrimination

- **Suraj Yengde** — everyday hierarchy reproduction (*Caste Matters*, 2019):
  social hierarchies persist through invisible, normalised preference patterns

---

## Methodology Notes

- Temperature = 0 for all model calls (deterministic, reproducible)
- A/B labels removed from prompts to eliminate position bias
- Model asked to state the candidate's full name, not pick A or B
- Group labels never appear in prompt text — name is the only signal
- All credentials held identical within each pair

---

## Citation

If you use this data or methodology in your research, please cite:

```
[Citation to be added after publication]
```

---

## Author

**Kunwar Siddharth**
PhD Researcher, UPES Dehradun
Research Area: Caste bias in generative AI systems
Project: EquiCaste

---

## License

Data and code released under MIT License.
Free to use, adapt, and build upon with attribution.
