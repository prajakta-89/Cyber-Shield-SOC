import streamlit as st
import mysql.connector
import bcrypt


def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prajakta@567.",
        database="cyber_security_db"
    )


# ================= VIEW USERS =================

def show_users():

    conn = get_connection()

    df = None

    import pandas as pd

    df = pd.read_sql(
        "SELECT id, username, role FROM Users",
        conn
    )

    conn.close()

    st.subheader("👥 System Users")

    st.dataframe(
        df,
        use_container_width=True
    )



# ================= ADD USER =================

def add_user():

    st.subheader("➕ Add New User")


    username = st.text_input(
        "Username"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    role = st.selectbox(
        "Role",
        [
            "Admin",
            "SOC Analyst",
            "Viewer"
        ]
    )


    if st.button("Create User"):


        hashed_password = bcrypt.hashpw(

            password.encode(),

            bcrypt.gensalt()

        )


        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO Users
            (username,password,role)

            VALUES(%s,%s,%s)
            """,

            (
                username,
                hashed_password.decode(),
                role
            )
        )


        conn.commit()

        cursor.close()

        conn.close()


        st.success(
            "User Created Successfully"
        )



# ================= DELETE USER =================

def delete_user():

    st.subheader("🗑 Delete User")


    username = st.text_input(
        "Username to delete"
    )


    if st.button("Delete"):


        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(

            """
            DELETE FROM Users
            WHERE username=%s
            """,

            (username,)

        )


        conn.commit()


        cursor.close()

        conn.close()


        st.success(
            "User Deleted"
        )



# ================= MAIN ADMIN PANEL =================

def admin_panel():

    st.sidebar.header(
        "⚙️ Admin Panel"
    )


    option = st.sidebar.selectbox(

        "Management",

        [
            "View Users",
            "Add User",
            "Delete User"
        ]

    )


    if option=="View Users":

        show_users()


    elif option=="Add User":

        add_user()


    elif option=="Delete User":

        delete_user()