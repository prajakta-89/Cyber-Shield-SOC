import random
import time
from datetime import datetime

LOG_FILE = "network_traffic.log"

ips = [
    "192.168.1.10",
    "192.168.1.15",
    "45.77.12.5",
    "103.21.45.11",
    "10.0.0.25"
]

destinations = [
    "10.0.0.2",
    "10.0.0.5",
    "10.0.0.10"
]

protocols = ["TCP", "UDP"]

ports = [22, 21, 23, 80, 443, 445, 3389, 1433]

actions = ["ALLOW", "DENY"]


print("Generating network traffic...\n")

while True:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = (
        f"{timestamp},"
        f"{random.choice(ips)},"
        f"{random.choice(destinations)},"
        f"{random.choice(protocols)},"
        f"{random.choice(ports)},"
        f"{random.choice(actions)}"
    )

    with open(LOG_FILE, "a") as file:
        file.write(line + "\n")

    print(line)

    time.sleep(3)