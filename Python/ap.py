import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from user_management import admin_panel
from login import login_page, check_role

# --- PAGE SETUP ---
st.set_page_config(page_title="CyberShield SOC", layout="wide")

# Custom CSS for the "Dark Security" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True) # FIXED THIS LINE

# ================= AUTHENTICATION =================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False



if not st.session_state.logged_in:

    login_page()

    st.stop()



check_role()

if st.session_state.role == "Admin":

    admin_panel()


# ================= DASHBOARD =================



st.sidebar.write(
    f"User: {st.session_state.username}"
)


st.sidebar.write(
    f"Role: {st.session_state.role}"
)


if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in=False

    st.rerun()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="cyber_security_db"
    )

# --- HEADER ---
st.title("🛰️ CyberShield: SOC Dashboard")
st.write(f"System Time: {datetime.now().strftime('%H:%M:%S')} | Status: ✅ Active")

try:
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM ThreatLogs ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:

        c1,c2,c3,c4,c5 = st.columns(5)


        c1.metric(
            "Total Alerts",
            len(df)
        )


        c2.metric(
            "👤 Unique Attackers",
            df["source_ip"].nunique()
        )



        if "risk_score" in df.columns:


            c3.metric(

                "Critical Threats",

                len(
                    df[
                        df["risk_score"] >= 100
                    ]
                )

            )


            c5.metric(

                "Average Risk",

                round(
                    df["risk_score"].mean(),
                    2
                )

            )

        else:


            c3.metric(
                "Critical Threats",
                "N/A"
            )


            c5.metric(
                "Average Risk",
                "N/A"
            )



        if "country" in df.columns:


            c4.metric(

                "Countries",

                df["country"].nunique()

            )

        else:


            c4.metric(
                "Countries",
                "N/A"
            )



        # Charts Row
        c1, c2 = st.columns(2)
        with c1:
            fig_pie = px.pie(df, names='event_type', title="Threat Types", template="plotly_dark")
            st.plotly_chart(fig_pie)
        with c2:
            top_ips = df['source_ip'].value_counts().head(5).reset_index()
            fig_bar = px.bar(top_ips, x='source_ip', y='count', title="Top Attackers", template="plotly_dark")
            st.plotly_chart(fig_bar)

        # Data Table

        # ================= ROLE BASED DATA ACCESS =================


    role = st.session_state.role



    # ADMIN

    if role == "Admin":

        st.subheader(" Admin: Full Incident Access")

        st.dataframe(
            df,
            use_container_width=True
        )



    # SOC ANALYST

    elif role == "SOC Analyst":

        st.subheader(" Analyst Investigation View")


        analyst_df = df[
            [
                "source_ip",
                "event_type",
                "severity_level",
                "risk_score",
                "description"
            ]
        ]


        st.dataframe(
            analyst_df,
            use_container_width=True
        )



        st.subheader(" High Risk Threats")


        high_risk = df[
            df["risk_score"] >= 100
        ]


        st.dataframe(
            high_risk,
            use_container_width=True
        )



    # VIEWER

    elif role == "Viewer":

        st.subheader(" Viewer Dashboard")


        viewer_df = df[
            [
                "source_ip",
                "event_type",
                "severity_level",
                "risk_score"
            ]
        ]


        st.dataframe(
            viewer_df,
            use_container_width=True
        )
        st.subheader("Live Incident Logs")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("System standby. No threats detected in logs.")

except Exception as e:
    st.error(f"Database Error: {e}")

if st.button("Refresh Dashboard"):
    st.rerun()
