import streamlit as st
import mysql.connector
import bcrypt


# ================= DATABASE CONNECTION =================

def get_connection():

    return mysql.connector.connect(

        host="localhost",
        user="root",
        password="Prajakta@567.",
        database="cyber_security_db"

    )



# ================= CHECK USER =================

def authenticate(username, password):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)


    query = """
    SELECT *
    FROM Users
    WHERE username=%s
    """


    cursor.execute(
        query,
        (username,)
    )


    user = cursor.fetchone()


    cursor.close()

    conn.close()



    if user:


        stored_password = user["password"]


        # Check password

        if isinstance(stored_password, str):

            stored_password = stored_password.encode()


        if bcrypt.checkpw(

            password.encode(),

            stored_password

        ):

            return user



    return None




# ================= LOGIN PAGE =================


import streamlit as st
import mysql.connector
import bcrypt
from datetime import datetime

# ---------------- DATABASE ---------------- #

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prajakta@567.",
        database="cyber_security_db"
    )


# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#050816,#0B1120,#111827);
}

/* Hide Streamlit Header */
header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* Main Title */

.title{

text-align:center;

font-size:58px;

font-weight:bold;

color:white;

margin-top:20px;

}

.subtitle{

text-align:center;

font-size:22px;

color:#00D4FF;

margin-bottom:5px;

}

.tagline{

text-align:center;

font-size:16px;

color:#9CA3AF;

margin-bottom:30px;

}


/* Login Card */

.login-card{

background:#161B22;

padding:40px;

border-radius:18px;

border:1px solid #30363D;

box-shadow:
0px 0px 15px rgba(0,212,255,.15),
0px 0px 40px rgba(0,212,255,.05);

}


/* Footer */

.footer{

text-align:center;

color:#9CA3AF;

margin-top:30px;

font-size:14px;

}

.status{

text-align:center;

color:#22C55E;

font-size:18px;

margin-bottom:15px;

}

hr{

border:1px solid #30363D;

}

</style>

""", unsafe_allow_html=True)


# ---------------- LOGIN FUNCTION ---------------- #

def login_page():

    st.markdown(
        "<div class='title'>🛡 CyberShield Analytics</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Enterprise Security Operations Center</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='tagline'>Real-Time Threat Detection • Risk Intelligence • Incident Response</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='status'>🟢 SOC STATUS : ONLINE</div>",
        unsafe_allow_html=True
    )

    left,center,right = st.columns([1.5,2,1.5])

    with center:

        st.markdown("<div class='login-card'>",unsafe_allow_html=True)

        st.markdown("## 🔐 Secure Login")

        username = st.text_input(
            "Username",
            placeholder="Enter Username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter Password"
        )

        remember = st.checkbox("Remember Me")

        login = st.button(
            " ACCESS SOC",
            use_container_width=True
        )

        st.markdown("</div>",unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    c1.success("🛡 Threat Engine Active")

    c2.info("🗄 Database Connected")

    c3.success("🕒 "+datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    st.markdown("<hr>",unsafe_allow_html=True)

    st.markdown(
        "<div class='footer'>CyberShield Analytics v2.0 | Enterprise SOC Platform</div>",
        unsafe_allow_html=True
    )

    if login:

        try:

            conn = get_connection()

            cursor = conn.cursor()

            cursor.execute(
                "SELECT password, role FROM Users WHERE username=%s",
                (username,)
            )

            user = cursor.fetchone()

            cursor.close()
            conn.close()

            if user:

                stored_password = user[0]
                role = user[1]

                if bcrypt.checkpw(
                    password.encode(),
                    stored_password.encode()
                ):

                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.role = role

                    st.success(f"Welcome {username}")

                    st.toast("Login Successful")

                    st.rerun()

                else:

                    st.error("❌ Invalid Password")

            else:

                st.error("❌ User Not Found")

        except Exception as e:

            st.error(e)

            # ================= ROLE CONTROL =================

def check_role():

    role = st.session_state.get("role")


    if role == "Admin":

        st.sidebar.success("👑 Admin Access")

        st.sidebar.write(
            """
            Permissions:

            ✅ View Dashboard
            ✅ Manage Users
            ✅ Delete Incidents
            ✅ Export Reports
            """
        )


    elif role == "SOC Analyst":

        st.sidebar.success("🕵️ SOC Analyst Access")

        st.sidebar.write(
            """
            Permissions:

            ✅ View Threats
            ✅ Investigate Attacks
            ✅ View IP Intelligence
            ✅ Analyze Risk

            ❌ User Management
            """
        )


    elif role == "Viewer":

        st.sidebar.info("👁 Viewer Access")

        st.sidebar.write(
            """
            Permissions:

            ✅ View Dashboard
            ✅ View Charts

            ❌ Modify Data
            ❌ Delete Incidents
            """
        )


    else:

        st.sidebar.warning(
            "Unknown Role"
        )