from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import includes
from inspect_ai.solver import generate

@task
def smoke_test():
    return Task(
        dataset=[Sample(input="What is the capital of France?", target="Paris")],
        solver=generate(),
        scorer=includes(),
    )
