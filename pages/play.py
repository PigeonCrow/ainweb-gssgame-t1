import streamlit as st


# Verify if the page can be accessed
def can_access_play_page():
    # You can implement your custom logic here
    # For now, we'll use a simple session state check
    if "game_started" not in st.session_state:
        st.error("Unauthorized access. Please start the game from the main page.")
        st.stop()

    # Clear the flag after accessing
    st.session_state["game_started"] = False


# Check access before rendering the page
can_access_play_page()


st.title("PLAY THE GAME !!")


def play_game():
    st.title(":blue[Guess The Capital]")

    # Your game logic here
    st.markdown("```GAME ``` ")

    if st.button("Back"):
        st.switch_page("app.py")


# Call the play_game function
play_game()
