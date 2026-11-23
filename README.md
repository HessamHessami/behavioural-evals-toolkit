# behavioural-evals-toolkit

A small, open toolkit for testing how AI agents behave under
pressure. An actor model runs a scenario; a separate judge model
scores the behaviour against a hidden rubric the actor never sees.

Status: early prototype (v0.0). Not a benchmark. Not an ethics
score. Results are evidence per scenario, not a safety guarantee.

## What it does
- Runs the same scenario in neutral, bias, pressure and
  perspective-flip variants
- Separates actor-visible and judge-only information
- Reports a shift rate against the neutral control

## Quickstart
Coming in v0.1.

## Limitations
See LIMITATIONS.md.
