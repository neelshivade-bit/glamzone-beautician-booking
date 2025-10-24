import streamlit as st

# Add image URLs or local paths here
beauticians = [
    {
        "name": "Anita Sharma",
        "expertise": "Hair stylist",
        "price": 500,
        "image_url": "https://images.unsplash.com/photo-1517841905240-472988babdf9"  # Replace with your own image
    },
    {
        "name": "Priya Verma",
        "expertise": "Makeup artist",
        "price": 700,
        "image_url": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"  # Replace with your own image
    }
]
services = [
    {
        "name": "Facial Glow",
        "category": "Skin",
        "price": 500,
        "expertise": "Anita Sharma",
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"   # Replace with your own image
    },
    {
        "name": "Bridal Makeup",
        "category": "Makeup",
        "price": 1500,
        "expertise": "Priya Verma",
        "image_url": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2"  # Replace with your own image
    }
]
appointments = []
reviews = []
queries = []

st.title("GlamZone Beautician Booking & Management")

menu = st.sidebar.selectbox("Main Menu", [
    "User Registration & Login", "Browse Services", "Book Appointment", "Beautician Portfolio",
    "Payment Integration (Demo)", "Rate/Review", "Admin Dashboard", "Notifications", "Customer Support"
])

if menu == "Browse Services":
    st.header("Service Browsing")
    cat = st.selectbox("Category", ["All"] + list(set([s["category"] for s in services])))
    for s in services:
        if cat == "All" or s["category"] == cat:
            st.subheader(s["name"])
            st.image(s["image_url"], width=200)
            st.write(f"Category: {s['category']} | Price: ₹{s['price']} | Expert: {s['expertise']}")

if menu == "Beautician Portfolio":
    st.header("Beautician Profile Management")
    beautician = st.selectbox("Beautician", [b["name"] for b in beauticians])
    b = next(b for b in beauticians if b["name"] == beautician)
    st.image(b["image_url"], width=200)
    st.write(f"Name: {b['name']}")
    st.write(f"Expertise: {b['expertise']}")
    st.write(f"Service Price: ₹{b['price']}")
    st.write("---")

# The rest of your booking, review, admin, and support code can remain as before
