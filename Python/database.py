import mysql.connector
from config import DB_CONFIG
from ip_intelligence import get_ip_details
from alert_engine import send_desktop_alert

# --------------------------------------------
# Get attack frequency for a source IP
# --------------------------------------------
def get_attack_frequency(ip):

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
        SELECT COUNT(*)
        FROM ThreatLogs
        WHERE source_ip = %s
        """

        cursor.execute(query, (ip,))

        count = cursor.fetchone()[0]

        return count + 1

    except Exception as e:
        print("Frequency Error:", e)
        return 1

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# --------------------------------------------
# Save Threat
# --------------------------------------------
def save_threat(ip, attack_type, severity, asset, description):

    try:

        # Calculate attack frequency
        frequency = get_attack_frequency(ip)

        # Dynamic Risk Score
        risk_score = severity * asset * frequency
        send_desktop_alert(
            ip,
            attack_type,
            risk_score
        )

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """

        INSERT INTO ThreatLogs
        (
        source_ip,
        event_type,
        severity_level,
        asset_criticality,
        description,
        risk_score,
        country,
        city,
        isp,
        organization
        )

        VALUES
        (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )

        """
        ip_info = get_ip_details(ip)

        country = ip_info["country"]
        city = ip_info["city"]
        isp = ip_info["isp"]
        organization = ip_info["organization"]

        cursor.execute(

        query,

        (
        ip,
        attack_type,
        severity,
        asset,
        description,
        risk_score,
        country,
        city,
        isp,
        organization
        )

        )

        conn.commit()

        print("=" * 45)
        print(" Threat Saved Successfully")
        print("=" * 45)
        print(f"Source IP        : {ip}")
        print(f"Attack Type      : {attack_type}")
        print(f"Severity         : {severity}")
        print(f"Asset Criticality: {asset}")
        print(f"Frequency        : {frequency}")
        print(f"Risk Score       : {risk_score}")
        print(f"Country          : {country}")
        print(f"City             : {city}")
        print(f"ISP              : {isp}")
        print(f"Organization     : {organization}")
        print("=" * 45)

    except Exception as e:

        print("Database Error:", e)

    finally:

        try:
            cursor.close()
            conn.close()
        except:
            pass
