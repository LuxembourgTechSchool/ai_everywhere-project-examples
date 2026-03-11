import streamlit as st

home = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
account = st.Page("pages/account.py", title="Account", icon="👤")
graphs = st.Page("pages/graphs.py", title="Graphs", icon="📊")
form = st.Page("pages/form.py", title="Form", icon="📝")

nav = st.navigation([home, account, graphs, form])
st.set_page_config(page_title="Multi-Page Demo", page_icon="🧭", layout="wide")
nav.run()
