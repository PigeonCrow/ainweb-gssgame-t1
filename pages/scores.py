import streamlit as st

st.title("Score Table")


def show_scores():
    st.title("Capital Guessing Game")
    st.markdown("## Scores")

    # logic here

    if st.button("Back to Welcome"):
        st.experimental_rerun()
