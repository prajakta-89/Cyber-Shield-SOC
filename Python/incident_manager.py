import mysql.connector
from datetime import datetime


def get_connection():

    return mysql.connector.connect(

        host="localhost",
        user="root",
        password="Prajakta@567.",
        database="cyber_security_db"

    )



# ================= CREATE INCIDENT =================

def create_incident(
        threat_id,
        source_ip,
        attack_type,
        severity,
        risk_score
):

    conn = get_connection()

    cursor = conn.cursor()


    query = """

    INSERT INTO Incidents

    (
    threat_id,
    source_ip,
    attack_type,
    severity,
    risk_score
    )

    VALUES(%s,%s,%s,%s,%s)

    """


    cursor.execute(

        query,

        (
            threat_id,
            source_ip,
            attack_type,
            severity,
            risk_score
        )

    )


    conn.commit()


    cursor.close()

    conn.close()


    print(
        "Incident Created Successfully"
    )



# ================= UPDATE STATUS =================


def update_incident_status(
        incident_id,
        status
):

    conn=get_connection()

    cursor=conn.cursor()



    if status=="RESOLVED":

        query="""

        UPDATE Incidents

        SET status=%s,
        resolved_time=%s

        WHERE incident_id=%s

        """


        cursor.execute(

            query,

            (
                status,
                datetime.now(),
                incident_id
            )

        )


    else:


        query="""

        UPDATE Incidents

        SET status=%s

        WHERE incident_id=%s

        """


        cursor.execute(

            query,

            (
                status,
                incident_id
            )

        )



    conn.commit()


    cursor.close()

    conn.close()


    print(
        "Incident Updated"
    )