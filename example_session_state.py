import streamlit as st

st.title("Counter Example")

# Add a variable to session_state
# This variable will be persistent during the session
# If you do not save the variable in the session_state, 
# it will be reset every time the script is run!
if "count" not in st.session_state:
    st.session_state.count = 0

increment = st.button("Increment")

if increment:
    st.session_state.count += 1

st.write(f"Current count: {st.session_state.count}")

# If you use a variable that is not in session_state (here: some_key), it will raise an error
# Try it by uncommenting the following line:
# st.write(f"Current count: {st.session_state.some_key}")

# Solution: You need to initialize the variable before using it
# Try it by uncommenting the following lines:

# if "some_key" not in st.session_state:
#     st.session_state.some_key = "I am some key"
# st.write(f"Current count: {st.session_state.some_key}")
