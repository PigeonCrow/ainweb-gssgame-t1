import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Capital Guessing Game",
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="🌍",
)


# load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url = "https://lottie.host/9ff7a123-ddc0-4686-91af-4918728c225a/1aZEVCy5Fn.json"
lottie_animation = load_lottieurl(lottie_url)


st.title(":blue[Guess The Capital]", anchor=False)

# show animation
st_lottie(lottie_animation, height=300, key="welcome_globe")


# init session state to controll navigation
if "game_started" not in st.session_state:
    st.session_state["game_started"] = False


left, middle, right = st.columns(3)
if middle.button("Play", icon="🌎", type="primary", use_container_width=True):
    st.session_state["game_started"] = True
    st.switch_page("pages/play.py")
