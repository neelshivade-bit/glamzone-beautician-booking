import streamlit as st
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="glamzone"
)
cursor = conn.cursor()

# Sidebar navigation
st.sidebar.title("GlamZone")
page = st.sidebar.radio("Go to", ["Home", "Register", "Login", "Book Appointment"])

# Home Page
if page == "Home":
    st.title("Welcome to GlamZone 💄")
    st.image("homepage_image.jpg", use_column_width=True)
    st.write("Your one-stop destination for beauty services.")

# Registration Page
elif page == "Register":
    st.subheader("Register")
    role = st.selectbox("Role", ["Client", "Beautician", "Admin"])
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                       (name, email, password, role))
        conn.commit()
        st.success("Registration successful!")

# Login Page
elif page == "Login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        if user:
            st.success(f"Welcome back, {user[1]}!")
        else:
            st.error("Invalid credentials.")

# Booking Page
elif page == "Book Appointment":
    st.subheader("Book an Appointment")
    beautician_id = st.number_input("Beautician ID", min_value=1)
    date = st.date_input("Date")
    time = st.time_input("Time")
    if st.button("Book"):
        cursor.execute("INSERT INTO appointments (beautician_id, date, time) VALUES (%s, %s, %s)",
                       (beautician_id, date, time))
        conn.commit()
        st.success("Appointment booked!")
