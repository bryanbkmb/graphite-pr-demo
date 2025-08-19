import json
from pathlib import Path
from datetime import datetime

class JsonLogger:
    """
    Writes one JSON object per line to logs/events.jsonl.
    """
    def __init__(self, path: str = "logs/events.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, message: str) -> None:
        rec = {"ts": datetime.utcnow().isoformat() + "Z", "message": message}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
