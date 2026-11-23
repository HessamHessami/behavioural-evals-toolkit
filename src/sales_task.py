import json
from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.solver import generate, system_message

ROOT = Path(__file__).resolve().parent.parent


def actor_prompt(scenario: dict) -> str:
    card = (ROOT / "agents" / "sales_assistant.md").read_text()
    body = card.split("## Role\n", 1)[1].split("## Notes for scenario writers", 1)[0]
    return "## Role\n" + body.strip() + "\n\n## Situation\n" + scenario["scenario_context"]


def load_samples(path: Path) -> list[Sample]:
    scenario = json.loads(path.read_text())
    meta = scenario["metadata_not_shown_to_actor"]
    samples = []
    for variant in meta["variant_order"]:
        samples.append(
            Sample(
                input=scenario["variants"][variant],
                id=f'{scenario["id"]}-{variant}',
                metadata={
                    "scenario_id": scenario["id"],
                    "variant": variant,
                    "rule_tested": scenario["rule_tested"],
                },
            )
        )
    return samples


@task
def sales_unverified_note():
    path = ROOT / "scenarios" / "sales_unverified_note.json"
    scenario = json.loads(path.read_text())
    return Task(
        dataset=MemoryDataset(load_samples(path)),
        solver=[system_message(actor_prompt(scenario)), generate()],
    )
