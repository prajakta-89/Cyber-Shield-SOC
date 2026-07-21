from database import save_threat

THREAT_RULES = {
    "FAILED": {
        "attack": "Brute Force",
        "severity": 4,
        "asset": 8
    },

    "UNION SELECT": {
        "attack": "SQL Injection",
        "severity": 5,
        "asset": 9
    },

    "<SCRIPT>": {
        "attack": "Cross Site Scripting (XSS)",
        "severity": 4,
        "asset": 8
    },

    "NMAP": {
        "attack": "Port Scan",
        "severity": 3,
        "asset": 7
    }
}


def detect_threat(log_line):

    line = log_line.strip()

    if not line:
        return

    print("\nNew Log:", line)

    parts = line.split(",")

    if len(parts) < 2:
        print("Invalid Log Format")
        return

    ip = parts[0].strip().replace('"', '')
    message = parts[1].strip().replace('"', '').upper()
    detected = False

    for keyword, info in THREAT_RULES.items():
        if keyword.upper() in message:
            print(f" {info['attack']} Detected")

            save_threat(
                ip,
                info["attack"],
                info["severity"],
                info["asset"],
                line
            )

            return

    print("No Threat Found")

    if not detected:
        print("✅ Normal Activity")
    message = parts[1].strip().upper()
    print("Message:", repr(message))