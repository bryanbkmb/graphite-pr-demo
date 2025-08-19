import os
from .json_logger import JsonLogger  # new import

class Notifier:
    """
    Now prepares a JsonLogger when JSON_LOG_ENABLED=1,
    but still only prints email. Not wired on purpose.
    """

    def __init__(self):
        self.mode = os.getenv("MODE", "email")
        self.json_log_enabled = os.getenv("JSON_LOG_ENABLED", "0") == "1"
        self.json_logger = JsonLogger() if self.json_log_enabled else None

    def send_alert(self, message: str) -> None:
        # BUG for the demo: even if JSON logging is enabled, we never write to it
        print(f"EMAIL: {message}")
