import streamlit as st

st.title("Welcome")
st.write("This is a minimal multi-page Streamlit app. Use the sidebar to navigate between pages.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Account")
    st.write("View and manage your profile information.")
    if st.button("Go to Account", use_container_width=True):
        st.switch_page("pages/account.py")

with col2:
    st.subheader("📊 Graphs")
    st.write("Interactive charts powered by random data.")
    if st.button("Go to Graphs", use_container_width=True):
        st.switch_page("pages/graphs.py")

with col3:
    st.subheader("📝 Form")
    st.write("Submit a contact form with validation.")
    if st.button("Go to Form", use_container_width=True):
        st.switch_page("pages/form.py")
