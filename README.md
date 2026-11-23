# behavioural-evals-toolkit

A small, open toolkit for testing how AI agents behave under
pressure. An actor model runs a scenario; a separate judge model
scores the behaviour against a hidden rubric the actor never sees.

**Status: early prototype (v0.0). Design and documentation only; no
runnable code yet.** Not a benchmark. Not an ethics score. Results
will be evidence per scenario, not a safety guarantee.

## Why this exists

A well-trained model can still give in when a user pushes. Research
has found sycophancy across several state-of-the-art assistants,
partly linked to human preferences for agreeable answers (Sharma et
al., 2024). This toolkit tests behaviour under pressure instead of
assuming a model resists it.

The approach is behavioural and model-agnostic. It makes no claim
to read a model's internal reasoning. It follows a pragmatic stance:
pick a goal, define a measurable proxy task, and let empirical
feedback show whether you are making progress, starting with the
simplest methods that work.

## Design

- **Actor / judge separation.** The actor sees only the task, roles,
  constraints and environment. The judge also sees hidden context,
  pass criteria and a rubric. The actor never receives judge
  information.
- **Controlled variation.** Each scenario is run in four variants
  describing the same underlying event: neutral, bias, pressure and
  perspective-flip. Only the user's framing changes, in line with
  the adversarial-plus-confirmatory logic of Haas et al. (2026).
- **Narrow judge.** Single-answer grading against a reference
  (Zheng et al., 2023), using a different model for judge and actor.
  The judge checks a response against a scenario-specific standard
  written before the run. It does not decide what is ethical in
  general.
- **Rubrics with severities.** Passing is a rule over criteria
  (critical, major), not a general impression. "Resisted the
  pressure" is scored separately from "offered a safe, useful
  alternative".
- **Primary metric (planned): sycophancy shift rate.** Among
  scenarios where the neutral response does not endorse the improper
  action, the share where the bias or pressure response endorses or
  materially helps with it. The neutral response is the control.

## Roadmap

| Milestone | Content |
|---|---|
| v0.1 | One category (resistance to pressure), 3-5 generic scenarios with four variants, local-model runner, recorded example run |
| v0.2 | Shift-rate metric, repeat trials with reported spread |
| v0.3 | Judge validation kit: 30-50 human-labelled transcripts, two raters, Cohen's kappa, confidence intervals |

The first runner is planned to build on
[Inspect](https://inspect.aisi.org.uk/), so results can be reproduced
with local models and no paid API key.

## What will and will not be open

Planned to be open: the schema, a minimal runner, a small set of
generic scenarios, and the validation tooling. This repository does
not contain, and will not contain, any private scenario corpus,
customer data or production rubrics.

## Limitations

See [LIMITATIONS.md](LIMITATIONS.md). Short version: the judge is not
yet validated against humans, the scenario set is tiny, and passing
a scenario does not show a system is safe.

## References

- Haas, J. et al. (2026). A roadmap for evaluating moral competence
  in large language models. *Nature*.
  doi:10.1038/s41586-025-10021-1
- Perez, E. et al. (2022). Discovering Language Model Behaviors with
  Model-Written Evaluations. arXiv:2212.09251
- Sharma, M. et al. (2024). Towards Understanding Sycophancy in
  Language Models. ICLR 2024. arXiv:2310.13548
- Zheng, L. et al. (2023). Judging LLM-as-a-Judge with MT-Bench and
  Chatbot Arena. arXiv:2306.05685

## Author and licence

Maintained by Hessam Hessami. MIT licence (see LICENSE).
Feedback and critique are welcome via issues.
