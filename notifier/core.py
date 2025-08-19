import os

class Notifier:
    """
    Very small demo component. Currently only emails by printing.
    JSON logging coming soon.
    """

    def __init__(self):
        self.mode = os.getenv("MODE", "email")

    def send_alert(self, message: str) -> None:
        print(f"EMAIL: {message}")
