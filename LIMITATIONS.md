# Limitations

This document states what the toolkit does not show. It will be
updated as validation work is done. Last updated: 23 November 2026.

## Current status

- No runnable code is released yet (v0.0).
- No judge validation has been run. A protocol is planned (see
  below).
- Earlier private prototyping covered a single scenario. That shows
  a pipeline can run end to end. It is not a benchmark claim, and no
  comparative claim is made until a reviewed set of about 30
  scenarios exists.

## What results mean

Results are evidence for a specific scenario, run with a specific
actor, judge and settings. They are not an overall ethics or safety
score for a model, and they do not show that a system is safe to
deploy.

## Threats to validity

| Threat | Mitigation | Status |
|---|---|---|
| Generated scenarios inherit the generator's blind spots or are unrealistic | Fixed method per category, facts limited to the supplied context, human review before any run, varied contexts | Planned for v0.1 |
| Judge bias or self-preference (position, verbosity, self-enhancement) | Single-answer grading, different actor and judge models, judge at least as capable as actor, explicit criteria, human calibration set | Partly design; calibration not run |
| Run-to-run variation in the actor | Repeat trials per scenario, report spread, store settings and model versions | Planned for v0.2 |
| Actor detects it is being tested | Keep judge criteria and variant labels out of the actor's input | One known leak (variant label) must be fixed before release |
| Proxy task does not transfer to deployment | Treat as per-scenario evidence; validate on real transcripts later | Open problem |
| Small sample | Scale to a reviewed set of about 30 before any comparative claim; report confidence intervals | Planned |
| Judge is narrow and rubric-bound | Does not decide what is ethical in general; checks against a standard written before the run | By design |
| Public scenarios may enter training data | Treat public scenarios as examples, not held-out tests; keep any held-out set private | Ongoing |

## Planned judge validation

1. Collect 30-50 gold-labelled transcripts.
2. Have at least two independent human raters label them, blind to
   the judge's verdicts.
3. Report Cohen's kappa for human pairs and for judge versus
   humans, and compare the two.
4. Revise the rubric if kappa falls below about 0.6.
5. Report confidence intervals on all rates.

## Out of scope

- Reading or interpreting a model's internal reasoning.
- Certifying compliance with any law or standard.
- Replacing human review, red-teaming or real-world monitoring.

## Reporting problems

If you find a flaw in a scenario, rubric or method, please open an
issue. Critique is part of how this gets better.
