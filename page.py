import streamlit as st

# Header
st.header("About: Ali FAKHAR")

# Image "photo_2024-02-22_20-13-17.jpg"
# st.image(None, width=300)

# Sections
st.subheader("Bio")
st.write("This is a test!!!\n page under construction!!!")

st.subheader("Publications")
# Display publications dynamically
publications = ["Paper 1", "Paper 2"]
for i in publications:
    st.write(f"- {i}")

st.subheader("Contact")
st.write("Email: {First name}{Last name}2013{at}yahoo.com")
st.write("Address: Grenoble, France")
