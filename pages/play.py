import streamlit as st
import json
import random
import os
from openai import OpenAI

#integrate AI
client = OpenAI(api_key="sk-svcacct-p5tbqGD9kG5T8cOTLFf6i-LusTXw9X4OBDRQnd4u02D9tBHoL364BkZS890Ne6ZT3BlbkFJdTeNdVE1t3jqwQ-kKZ4NQ66-F_8I8hcmZ-HJHWYeNCJtRDr7-pz1AvdTQlJziAA")
model = "gpt-4o-mini"
new_capital = ""

# Load capitals by using AI
def get_capital():
    try:
        capital_prompt = "Name a random capital. Answer with a single word."
        chat_completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "user", "content": capital_prompt},
        ],
        )
        #Extract the response content
        new_capital = chat_completion.choices[0].message.content.strip()
        #Ensure that it is a valid string
        if not new_capital or " " in new_capital:
            raise ValueError("Invalid capital received.")
        return new_capital
    except Exception as e:
        st.error(f"Error loading capitals data: {e}")
        return None


# Generate hints for the selected capital by using AI
# differentiating between difficulty levels of 3 generated hints
def generate_hints(new_capital):
    hint1_prompt = "We are playing a guessing game. The capital " +  new_capital + " needs to be guessed. We want to give hints from difficulty levels 1(very hard), 2 (still tricky) and 3(easy). Give a short one sentence hint of the difficulty 1"
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "user", "content": hint1_prompt},
        ],
        )
    hint1 = chat_completion.choices[0].message.content
    hint2_prompt = "We are playing a guessing game. The capital " +  new_capital + " needs to be guessed. We want to give hints from difficulty levels 1(very hard), 2 (still tricky) and 3(easy). Give a short one sentence hint of the difficulty 2"
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "user", "content": hint2_prompt},
        ],
        )
    hint2 = chat_completion.choices[0].message.content
    hint3_prompt = "We are playing a guessing game. The capital " +  new_capital + " needs to be guessed. We want to give hints from difficulty levels 1(very hard), 2 (still tricky) and 3(easy). Give a short one sentence hint of the difficulty 3"
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "user", "content": hint3_prompt},
        ],
        )
    hint3 = chat_completion.choices[0].message.content
    hints = [hint1, hint2, hint3] 
    return hints


# Initialize game state.
def initialize_game_state():
    if "current_capital" not in st.session_state:
        new_capital = get_capital() #Get the capital as a string
        if new_capital: #If valid capital is received
            st.session_state.current_capital = {"capital": new_capital}
            st.session_state.hints = generate_hints(new_capital)
            st.session_state.hints_shown = 1
            st.session_state.game_active = True
            st.session_state.total_score = st.session_state.get("total_score", 0)
        else:
            st.error("Failed to start the game. No valid capital.")
            st.session_state.game_active = False


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
        # Show second hint
        if st.button("Get Additional Hint"):
            st.session_state.hints_shown = 2
            st.markdown("### Additional Hint:")
            st.warning(st.session_state.hints[1])
    elif st.session_state.hints_shown == 2 and st.session_state.game_active:
        # Show third hint
        if st.button("Get Additional Hint"):
            st.markdown("### Third Hint:")
            st.error(st.session_state.hints[2])
            st.session_state.hints_shown = 3

    # Get user guess
    user_guess = st.text_input("Enter your guess:", key="guess_input")

    if st.button("Submit Guess"):
        if user_guess.lower() == st.session_state.current_capital["capital"].lower(): # User had correct guess
            # Calculate points based on hints used
            if (st.session_state.hints_shown == 1):
                points = 3  
            elif (st.session_state.hints_shown == 2):
                points = 2
            else:
                points = 1
            st.session_state.total_score += points
            st.success(f"Correct! You earned {points} points!")
            st.session_state.game_active = False
        else: # User did not guess correctly
            if st.session_state.hints_shown == 1: # User had only one hint -> might to get another hint
                st.error("Sorry, that's incorrect. Try getting another hint.")
            elif st.session_state.hints_shown == 2: # User saw two hints -> might see a last, third hint
                st.error("Sorry, that's incorrect. Try getting another hint.")
            else: # User saw three hints and guess was incorrect -> game over
                st.error("Sorry, that's incorrect. No points awarded!")
                st.session_state.game_active = False

    if not st.session_state.game_active:
        st.markdown(
            f"The correct answer was: **{st.session_state.current_capital['capital']}**"
        )
        if st.button("Next Round"):
            # Reset game state for next round
            del st.session_state.current_capital
            del st.session_state.hints
            del st.session_state.hints_shown
            del st.session_state.game_active
            st.rerun()

    # Back button
    if st.button("Back to Main Menu"):
        st.switch_page("apptest.py")


# Verify if the page can be accessed
def can_access_play_page():
    if "game_started" not in st.session_state:
        st.error("Unauthorized access. Please start the game from the main page.")
        st.stop()
    st.session_state["game_started"] = False


data = get_capital()
if data:
    can_access_play_page()
    play_game()
