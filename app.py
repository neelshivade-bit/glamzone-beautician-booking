import streamlit as st

# Dummy user, beautician, and admin lists for demonstration
users = {"client": [], "beautician": [], "admin": []}
services = [
    {"name": "Facial Glow", "category": "Skin", "price": 500, "expertise": "Anita Sharma"},
    {"name": "Bridal Makeup", "category": "Makeup", "price": 1500, "expertise": "Priya Verma"}
]
appointments = []
reviews = []
queries = []

st.title("GlamZone Beautician Booking & Management")

menu = st.sidebar.selectbox("Main Menu", [
    "User Registration & Login", "Browse Services", "Book Appointment", "Beautician Portfolio",
    "Payment Integration (Demo)", "Rate/Review", "Admin Dashboard", "Notifications", "Customer Support"
])

if menu == "User Registration & Login":
    st.header("Register/Login")
    role = st.selectbox("Role", ["client", "beautician", "admin"])
    username = st.text_input("Username")
    action = st.radio("Action", ["Register", "Login"])
    if st.button("Submit"):
        if action == "Register":
            users[role].append(username)
            st.success(f"Registered {username} as {role}. (Demo mode)")
        else:
            if username in users[role]:
                st.success(f"Welcome back, {username}! (Demo mode)")
            else:
                st.error("User not found. Please register.")

if menu == "Browse Services":
    st.header("Service Browsing")
    cat = st.selectbox("Category", ["All"] + list(set([s["category"] for s in services])))
    for s in services:
        if cat == "All" or s["category"] == cat:
            st.subheader(s["name"])
            st.write(f"Category: {s['category']} | Price: ₹{s['price']} | Expert: {s['expertise']}")

if menu == "Book Appointment":
    st.header("Appointment Booking")
    client = st.text_input("Client Name")
    service = st.selectbox("Service", [s["name"] for s in services])
    date = st.date_input("Date")
    time = st.time_input("Time")
    if st.button("Book Now"):
        appointments.append({"client": client, "service": service, "date": date, "time": time})
        st.success("Appointment booked! Notification sent. (Demo mode)")

if menu == "Beautician Portfolio":
    st.header("Beautician Profile Management")
    beautician = st.selectbox("Beautician", [s["expertise"] for s in services])
    portfolio = [s for s in services if s["expertise"] == beautician]
    st.write(f"Portfolio for {beautician}:")
    for p in portfolio:
        st.write(f"- {p['name']} ({p['category']}, ₹{p['price']})")

if menu == "Payment Integration (Demo)":
    st.header("Payment Integration")
    st.info("Integration with Razorpay/PayPal can be added using payment API (demo only)")

if menu == "Rate/Review":
    st.header("Rate & Review")
    reviewer = st.text_input("Reviewer Name")
    service = st.selectbox("Service to Review", [s["name"] for s in services])
    rating = st.slider("Rating (stars)", 1, 5)
    text = st.text_area("Review Text")
    if st.button("Post Review"):
        reviews.append({"reviewer": reviewer, "service": service, "rating": rating, "text": text})
        st.success("Review posted! (Demo mode)")
    st.subheader("Recent Reviews")
    for r in reviews:
        st.markdown(f"**{r['reviewer']}** rated {r['service']} {r['rating']} stars: {r['text']}")

if menu == "Admin Dashboard":
    st.header("Admin Dashboard")
    st.write(f"Total Registered Users: {sum(len(v) for v in users.values())}")
    st.write(f"Appointments: {len(appointments)}, Reviews: {len(reviews)}, Support Queries: {len(queries)}")

if menu == "Notifications":
    st.header("Notifications & Reminders")
    st.info("Email/SMS notifications can be sent using Streamlit's email module or external API (not implemented in demo).")

if menu == "Customer Support":
    st.header("Support & Feedback")
    name = st.text_input("Your Name (Support)")
    query = st.text_area("Type your query or complaint")
    if st.button("Submit Query"):
        queries.append({"name": name, "query": query})
        st.success("Query submitted! Support will respond soon. (Demo mode)")
    st.subheader("Recent Support Queries")
    for q in queries:
        st.markdown(f"**{q['name']}** asked: {q['query']}")

st.sidebar.write("Demo app based on your PDF synopsis[file:1].")
