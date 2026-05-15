# Prompt Design: Why Stakes and Trust Were Made Explicit

## The Problem with Neutral Prompts

Standard audit studies present two candidates with identical credentials
and ask a model to choose. This design, borrowed from resume audit
methodology (Bertrand & Mullainathan, 2004), tests whether a name alone
shifts a model's choice. But it leaves open a critical escape route: the
model can answer "I cannot distinguish between them" or give a coin-flip
rationale. Ambiguity in the scenario grants the model permission to avoid
a real decision — and avoids revealing the associative structure beneath
its surface reasoning.

Caste bias does not operate in low-stakes, neutral terrain. It operates
precisely where something important is at risk and a decision-maker must
judge who can be trusted. The landowner worried about theft, the hospital
doctor with one bed, the RWA deciding who handles eleven lakh rupees —
these are the real sites of caste discrimination documented by Thorat &
Attewell (2010), Equality Labs (2020), and the NCRB (2022). An audit
instrument that avoids exactly this pressure cannot claim ecological
validity.

## What We Changed — and Why

Each of the five scenarios in this study was redesigned to embed three
elements absent from the original neutral version:

**1. A concrete, named stake that cannot be avoided.**
The hiring scenario is not a generic shortlisting decision. The selected
engineer will have unsupervised read-write access to a bank's live
transaction database — a situation made real by citing a prior incident
of Rs. 43 lakh fraud in an identical role. The rental scenario involves
an elderly widow living alone above the flat, with Rs. 9 lakh in savings
in an unlocked cupboard. The RWA scenario places Rs. 11.4 lakh of society
funds and master-key access in the secretary's hands. Quantified, specific
stakes prevent the model from treating the choice as inconsequential.

**2. An explicit trust judgment, not merely a competence judgment.**
Standard prompts ask which candidate is "more suitable." These prompts ask
which candidate is "more trustworthy for a role with this level of
unsupervised access," or which applicant "a vulnerable elderly woman living
alone can genuinely trust." This is methodologically significant: trust
judgments require the model to make an inference about character, not only
credentials. Because credentials are held constant across both candidates,
any differential in trust inference must arise from signals other than
merit — most plausibly the name, which carries caste information.

**3. An asymmetric cost of error.**
Every scenario specifies what happens to the candidate who is not chosen:
the patient not admitted faces a 34-kilometre transfer at night with no
guaranteed funds; the tenant not selected loses the only shortlisted
option; the scholar not awarded loses the lab partnership permanently.
This raises the affective salience of the decision and prevents the model
from hedging. Models that would otherwise recommend "further evaluation"
or "interview both" are forced to commit.

## What This Design Tests

These scenarios test a specific hypothesis: that LLMs do not merely
reproduce occupational stereotypes (subject-directed bias) but that they
infer character, trustworthiness, and moral reliability from caste-coded
names when stakes demand a judgment about who is safe to trust.

This is theoretically distinct from competence bias. A model may score
both candidates equally on skill while still encoding the belief that one
name signals a person less likely to steal, less likely to mismanage
funds, or more likely to be accepted by a community. Trust inference of
this kind is rooted in the centuries-old ideological infrastructure of
varna hierarchy, in which purity, moral rectitude, and social reliability
were structurally attributed to dominant-caste groups and withheld from
Shudras and Ati-Shudras (Ambedkar, 1936; Periyar, 1938).

When a model, given no information other than a name, judges one person
more trustworthy for access to an elderly widow's savings or a hospital's
only ICU bed, it reproduces this inference — not from explicit programming,
but from patterns absorbed during training on a corpus where these
associations have been naturalised over generations of text.

## Settings Preserved — Stakes Elevated

The environmental setting of each scenario (city, institution type,
occupational domain) was kept identical to the original design to ensure
comparability across the shallow and deep prompt batteries. The only
modifications are: (a) the specificity and magnitude of what is at risk;
(b) the explicit framing of the decision as a trust judgment; and (c) the
asymmetric consequence clause. Names, credentials, ages, and demographic
details remain identical across Candidate A and Candidate B within each
pair, preserving the counterfactual logic of the audit design.
