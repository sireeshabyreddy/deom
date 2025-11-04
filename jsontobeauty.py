import json

with open("fake_logs_40k.jsonl", "r") as f:
    logs = [json.loads(line) for line in f]

with open("fake_logs_40k_pretty.json", "w") as f:
    json.dump(logs, f, indent=2)
