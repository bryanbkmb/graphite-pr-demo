from notifier.core import Notifier

def test_send_alert_prints_email(capfd):
    n = Notifier()
    n.send_alert("hello")
    out, _ = capfd.readouterr()
    assert "EMAIL: hello" in out
