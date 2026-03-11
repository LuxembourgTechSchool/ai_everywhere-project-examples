import streamlit as st

st.title("Account")

st.subheader("Profile")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://api.dicebear.com/9.x/initials/svg?seed=JD", width=120)

with col2:
    st.markdown("**Name:** Jane Doe")
    st.markdown("**Email:** jane.doe@example.com")
    st.markdown("**Role:** Administrator")

st.divider()

st.subheader("Preferences")
theme = st.selectbox("Theme", ["Light", "Dark", "System"])
notifications = st.toggle("Email notifications", value=True)
st.write(f"Theme: **{theme}** | Notifications: **{'on' if notifications else 'off'}**")
