import streamlit as st
import json
import random
import os


# Load capitals data from JSON file
def load_capitals():
    try:
        with open("resources/Capitals.json", "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        st.error(f"Error loading capitals data: {e}")
        return None


# Select a random capital from the data
# Flatten the structure to get all countries
def get_random_capital(data):
    all_countries = []
    for continent in data["continents"]:
        all_countries.extend(continent["countries"])
    return random.choice(all_countries)


# Generate hints for the selected capital
def generate_hints(country_data):
    hints = [
        f"This city is the capital of a country in {get_continent_for_capital(data, country_data['capital'])}",
        f"The main language spoken here is {country_data['attributes']['language']}",
        f"This is the capital of {country_data['country']}",
    ]
    random.shuffle(hints)  # Randomize hint order
    return hints


# Find the continent for a given capital
def get_continent_for_capital(data, capital):
    for continent in data["continents"]:
        for country in continent["countries"]:
            if country["capital"] == capital:
                return continent["name"]
    return "Unknown"


# Initialize game state.
def initialize_game_state():
    if "current_capital" not in st.session_state:
        data = load_capitals()
        if data:
            country_data = get_random_capital(data)
            st.session_state.current_capital = country_data
            st.session_state.hints = generate_hints(country_data)
            st.session_state.hints_shown = 1
            st.session_state.game_active = True
            st.session_state.total_score = st.session_state.get("total_score", 0)


def clear_input():
    st.session_state.guess_input = ""


def play_game():
    st.title(":blue[Guess The Capital]")

    initialize_game_state()

    # TODO: FIX score vizualisation
    # Display current score
    st.sidebar.markdown(f"**Total Score**: {st.session_state.total_score}")

    # Display score in ui with separators
    # col1, col2 = st.columns([3, 1])
    # with col2:
    #    st.markdown("### Score")
    #    st.markdown(f"<h2 style='text-align: center; color: #1f77b4;'>{st.session_state.total_score}</h2>", unsafe_allow_html=True)

    # Display 1st hint
    st.markdown("### Current Hint:")
    st.info(st.session_state.hints[0])

    # Additional hint button
    if st.session_state.hints_shown == 1 and st.session_state.game_active:
        if st.button("Get Additional Hint"):
            st.session_state.hints_shown = 2
            st.markdown("### Additional Hint:")
            st.warning(st.session_state.hints[1])
    elif st.session_state.hints_shown == 2 and st.session_state.game_active:
        st.markdown("### Additional Hint:")
        st.warning(st.session_state.hints[1])

    # Get user guess
    user_guess = st.text_input("Enter your guess:", key="guess_input")

    if st.button("Submit Guess"):
        if user_guess.lower() == st.session_state.current_capital["capital"].lower():
            # Calculate points based on hints used
            points = 2 if st.session_state.hints_shown == 1 else 1
            st.session_state.total_score += points
            st.success(f"Correct! You earned {points} points!")
            st.session_state.game_active = False
        else:
            if st.session_state.hints_shown == 2:
                st.error("Sorry, that's incorrect. No points awarded.")
                st.session_state.game_active = False
            else:
                st.error("Sorry, that's incorrect. Try getting another hint!")

    if not st.session_state.game_active:
        st.markdown(
            f"The correct answer was: **{st.session_state.current_capital['capital']}**"
        )
        if st.button("Next Round", on_click=clear_input):
            # clear guess text_input
            # st.session_state.guess_input = ""

            # Reset game state for next round
            del st.session_state.current_capital
            del st.session_state.hints
            del st.session_state.hints_shown
            del st.session_state.game_active
            st.rerun()

    # Back button
    if st.button("Back to Main Menu"):
        st.switch_page("app.py")


# Verify if the page can be accessed
def can_access_play_page():
    if "game_started" not in st.session_state:
        st.error("Unauthorized access. Please start the game from the main page.")
        st.stop()
    st.session_state["game_started"] = False


data = load_capitals()
if data:
    can_access_play_page()
    play_game()
