import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load Lottie animation
lottie_url = "https://lottie.host/9ff7a123-ddc0-4686-91af-4918728c225a/1aZEVCy5Fn.json"
lottie_animation = load_lottieurl(lottie_url)

st.set_page_config(page_title="Capital Guessing Game")

st.title("Capital Guessing Game")
st.markdown("## Welcome to the Capital Guessing Game!")

# Display the Lottie animation
st_lottie(lottie_animation, height=300, key="welcome")

if st.button("Start Game"):
    # Navigate to the game page
    st.experimental_set_query_params(page="game")
    st.experimental_rerun()
