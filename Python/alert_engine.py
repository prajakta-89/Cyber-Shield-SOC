from plyer import notification
import datetime


RISK_THRESHOLD = 100


def send_desktop_alert(
        ip,
        attack,
        risk_score
):

    if risk_score >= RISK_THRESHOLD:

        title = " CyberShield Critical Alert"

        message = f"""
Attack: {attack}
Source IP: {ip}
Risk Score: {risk_score}
Time: {datetime.datetime.now()}
"""

        notification.notify(
            title=title,
            message=message,
            timeout=10
        )

        print(" Desktop Alert Sent!")