import streamlit as st

st.title("Contact Form")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    category = st.selectbox("Category", ["General", "Bug Report", "Feature Request"])
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not name or not email or not message:
        st.error("Please fill in all fields.")
    else:
        st.success(f"Thanks, **{name}**! Your message was received.")
        with st.expander("Submitted data"):
            st.json({"name": name, "email": email, "category": category, "message": message})
