from collections import defaultdict
from inspect_ai.log import list_eval_logs, read_eval_log

log = read_eval_log(list_eval_logs("logs")[0])
tally = defaultdict(lambda: [0, 0])
for s in log.samples:
    v = s.metadata["variant"]
    ok = s.scores["no_unsupported_label"].value == "C"
    tally[v][0] += ok
    tally[v][1] += 1
for v, (ok, n) in tally.items():
    print(f"{v:18s} {ok}/{n}")
