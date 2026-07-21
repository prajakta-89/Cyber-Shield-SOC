from database import save_threat

SUSPICIOUS_PORTS = {

    21: ("FTP Access", 2, 5),

    22: ("SSH Login", 3, 7),

    23: ("Telnet Access", 5, 10),

    445: ("SMB Attack", 5, 10),

    3389: ("RDP Attack", 4, 9),

    1433: ("SQL Server Attack", 5, 10)
}


def detect_network_threat(log):

    data = log.strip().split(",")

    if len(data) != 6:
        return

    timestamp, src_ip, dst_ip, protocol, port, action = data

    port = int(port)

    print("\nNetwork Event")
    print("-" * 40)
    print("Source :", src_ip)
    print("Destination :", dst_ip)
    print("Protocol :", protocol)
    print("Port :", port)
    print("Action :", action)

    if port in SUSPICIOUS_PORTS:

        attack, severity, asset = SUSPICIOUS_PORTS[port]

        print("🚨 Threat:", attack)

        save_threat(
            src_ip,
            attack,
            severity,
            asset,
            log.strip()
        )

    else:

        print("✅ Normal Traffic")