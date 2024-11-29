import streamlit as st
import os
import csv
from openai import OpenAI
import random

# integrate AI
client = OpenAI(api_key=st.secrets["openai"]["api_key"])
model = "gpt-4o-mini"
new_capital = ""


# Load capitals by using AI
def get_capital():
    # define static list of capitals
    capital_list = [
        "Kabul",
        "Tirana",
        "Algiers",
        "Andorra la Vella",
        "Luanda",
        "Saint John's",
        "Buenos Aires",
        "Yerevan",
        "Canberra",
        "Vienna",
        "Baku",
        "Nassau",
        "Manama",
        "Dhaka",
        "Bridgetown",
        "Minsk",
        "Brussels",
        "Belmopan",
        "Porto-Novo",
        "Thimphu",
        "La Paz",
        "Sarajevo",
        "Gaborone",
        "Brasília",
        "Bandar Seri Begawan",
        "Sofia",
        "Ouagadougou",
        "Gitega",
        "Phnom Penh",
        "Yaoundé",
        "Ottawa",
        "Praia",
        "Bangui",
        "N'Djamena",
        "Santiago",
        "Beijing",
        "Bogotá",
        "Moroni",
        "Brazzaville",
        "Kinshasa",
        "San José",
        "Zagreb",
        "Havana",
        "Nicosia",
        "Prague",
        "Copenhagen",
        "Djibouti",
        "Roseau",
        "Santo Domingo",
        "Quito",
        "Cairo",
        "San Salvador",
        "Malabo",
        "Asmara",
        "Tallinn",
        "Mbabane",
        "Addis Ababa",
        "Suva",
        "Helsinki",
        "Paris",
        "Libreville",
        "Banjul",
        "Tbilisi",
        "Berlin",
        "Accra",
        "Athens",
        "Saint George's",
        "Guatemala City",
        "Conakry",
        "Bissau",
        "Georgetown",
        "Port-au-Prince",
        "Tegucigalpa",
        "Budapest",
        "Reykjavik",
        "New Delhi",
        "Jakarta",
        "Tehran",
        "Baghdad",
        "Dublin",
        "Jerusalem",
        "Rome",
        "Kingston",
        "Tokyo",
        "Amman",
        "Nur-Sultan",
        "Nairobi",
        "Tarawa",
        "Pyongyang",
        "Seoul",
        "Pristina",
        "Kuwait City",
        "Bishkek",
        "Vientiane",
        "Riga",
        "Beirut",
        "Maseru",
        "Monrovia",
        "Tripoli",
        "Vaduz",
        "Vilnius",
        "Luxembourg",
        "Antananarivo",
        "Lilongwe",
        "Kuala Lumpur",
        "Malé",
        "Bamako",
        "Valletta",
        "Majuro",
        "Nouakchott",
        "Port Louis",
        "Mexico City",
        "Palikir",
        "Chisinau",
        "Monaco",
        "Ulaanbaatar",
        "Podgorica",
        "Rabat",
        "Maputo",
        "Naypyidaw",
        "Windhoek",
        "Yaren",
        "Kathmandu",
        "Amsterdam",
        "Wellington",
        "Managua",
        "Niamey",
        "Abuja",
        "Skopje",
        "Oslo",
        "Muscat",
        "Islamabad",
        "Ngerulmud",
        "Panama City",
        "Port Moresby",
        "Asunción",
        "Lima",
        "Manila",
        "Warsaw",
        "Lisbon",
        "Doha",
        "Bucharest",
        "Moscow",
        "Kigali",
        "Basseterre",
        "Castries",
        "Kingstown",
        "Apia",
        "San Marino",
        "Riyadh",
        "Dakar",
        "Belgrade",
        "Victoria",
        "Freetown",
        "Singapore",
        "Bratislava",
        "Ljubljana",
        "Honiara",
        "Mogadishu",
        "Pretoria",
        "Juba",
        "Madrid",
        "Colombo",
        "Khartoum",
        "Paramaribo",
        "Stockholm",
        "Bern",
        "Damascus",
        "São Tomé",
        "Dushanbe",
        "Dodoma",
        "Bangkok",
        "Lomé",
        "Nuku'alofa",
        "Port of Spain",
        "Tunis",
        "Ankara",
        "Ashgabat",
        "Funafuti",
        "Kampala",
        "Kyiv",
        "Abu Dhabi",
        "London",
        "Washington, D.C.",
        "Montevideo",
        "Tashkent",
        "Port Vila",
        "Vatican City",
        "Caracas",
        "Hanoi",
        "Lusaka",
        "Harare",
    ]

    new_capital = random.choice(capital_list)
    return new_capital

    # try:
    #     capital_prompt = "Name a random capital. Answer with a single word."
    #     chat_completion = client.chat.completions.create(
    #         model=model,
    #         messages=[
    #             {"role": "user", "content": capital_prompt},
    #         ],
    #     )
    #     # Extract the response content
    #     new_capital = chat_completion.choices[0].message.content.strip()
    #     # Ensure that it is a valid string
    #     if not new_capital or " " in new_capital:
    #         raise ValueError("Invalid capital received.")
    #     return new_capital
    # except Exception as e:
    #     st.error(f"Error loading capitals data: {e}")
    #     return None


# Generate hints for the selected capital by using AI
# differentiating between difficulty levels of 3 generated hints
def generate_hints(new_capital):
    hint1_prompt = (
        "We are playing a guessing game. The capital "
        + new_capital
        + " needs to be guessed. We want to give hints from difficulty levels 1(very hard), 2 (still tricky) and 3(easy). Give a short one sentence hint of the difficulty 1"
    )
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": hint1_prompt},
        ],
    )
    hint1 = chat_completion.choices[0].message.content
    hint2_prompt = (
        "We are playing a guessing game. The capital "
        + new_capital
        + " needs to be guessed. We want to give hints from difficulty levels 1(very hard), 2 (still tricky) and 3(easy). Give a short one sentence hint of the difficulty 2 "
    )
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": hint2_prompt},
        ],
    )
    hint2 = chat_completion.choices[0].message.content
    hint3_prompt = (
        "We are playing a guessing game. The capital "
        + new_capital
        + " needs to be guessed. We want to give hints from difficulty levels 1(very hard), 2 (still tricky) and 3(easy). Give a short one sentence hint of the difficulty 3 and never mention the actual City while providing this hint"
    )
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
        new_capital = get_capital()  # Get the capital as a string
        if new_capital:  # If valid capital is received
            st.session_state.current_capital = {"capital": new_capital}
            st.session_state.hints = generate_hints(new_capital)
            st.session_state.hints_shown = 1
            st.session_state.game_active = True
            st.session_state.total_score = st.session_state.get("total_score", 0)
            st.session_state.score_saved = False
            st.session_state.player_name = ""
            st.session_state.show_save_dialog = False
            # st.session_state.input_disabled = False


# save scores/stats
def save_score(name, score):
    scores_file = "resources/scores.csv"
    updated_scores = []
    name_exists = False

    # if file does not exist create header
    # find duplicate names and add the scores
    if os.path.exists(scores_file):
        with open(scores_file, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # skip header
            for row in reader:
                if row[0] == name:
                    updated_scores.append([name, int(row[1]) + score])
                    name_exists = True
                else:
                    updated_scores.append(row)

        with open(scores_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score"])
            writer.writerows(updated_scores)
            if not name_exists:
                writer.writerow([name, score])
    else:
        # Create new file if doesn't exist
        with open(scores_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score"])
            writer.writerow([name, score])


# clear last input when replaying
# def clear_input():
# st.session_state.guess_input = ""
#   else:
#       st.error("Failed to start the game. No valid capital.")
#       st.session_state.game_active = Falsedef


def clear_round_state():
    if "current_capital" in st.session_state:
        del st.session_state.current_capital
    if "hints" in st.session_state:
        del st.session_state.hints
    if "hints_shown" in st.session_state:
        del st.session_state.hints_shown
    if "game_active" in st.session_state:
        del st.session_state.game_active
    if "guess_input" in st.session_state:
        st.session_state.guess_input = ""
    st.session_state.show_save_dialog = False
    st.session_state.score_saved = False


# main play func
def play_game():
    st.title(":blue[Guess The Capital]")

    initialize_game_state()

    # display current score
    st.sidebar.markdown(f"**Total Score**: {st.session_state.total_score}")

    if st.session_state.game_active:
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
                st.markdown("### Additional Hint:")
                st.warning(st.session_state.hints[1])
                st.markdown("### Third Hint:")
                st.error(st.session_state.hints[2])
                st.session_state.hints_shown = 3

        # Get user guess
        user_guess = st.text_input("Enter your guess:", key="guess_input")

        if st.button("Submit Guess"):
            if (
                user_guess.lower()
                == st.session_state.current_capital["capital"].lower()
            ):
                # User had correct guess
                # Calculate points based on hints used
                if st.session_state.hints_shown == 1:
                    points = 3
                elif st.session_state.hints_shown == 2:
                    points = 2
                else:
                    points = 1
                st.session_state.total_score += points
                st.success(f"Correct! You earned {points} points!")
                st.session_state.game_active = False
            else:  # User did not guess correctly
                if (
                    st.session_state.hints_shown == 1
                ):  # User had only one hint -> might to get another hint
                    st.error("Sorry, that's incorrect. Try getting another hint.")
                elif (
                    st.session_state.hints_shown == 2
                ):  # User saw two hints -> might see a last, third hint
                    st.error("Sorry, that's incorrect. Try getting another hint.")
                else:  # User saw three hints and guess was incorrect -> game over
                    st.error("Sorry, that's incorrect. No points awarded!")
                    st.session_state.game_active = False

    ## Game Over state
    if not st.session_state.game_active:
        st.markdown(
            f"The correct answer was: **{st.session_state.current_capital['capital']}**"
        )
        # Add Save Score button that shows dialog
        if not st.session_state.score_saved:
            if st.button("Save Score"):
                st.session_state.show_save_dialog = True

        # Show save score dialog
        if st.session_state.show_save_dialog and not st.session_state.score_saved:
            with st.form(key="save_score_dialog"):
                st.subheader("Save Your Score")
                st.markdown(f"Current Score: {st.session_state.total_score}")
                player_name = st.text_input("Enter your name:")
                save_button = st.form_submit_button("Save")

                if save_button and player_name:
                    save_score(player_name.strip(), st.session_state.total_score)
                    st.session_state.score_saved = True
                    st.session_state.show_save_dialog = False
                    st.session_state.total_score = 0
                    st.success(f"Score saved for player: {player_name}")

        if st.button("Next Round"):
            clear_round_state()
            st.rerun()

    # back button
    if st.button("Back to home "):
        st.switch_page("app.py")


# verify if the page can be accessed
def can_access_play_page():
    if "game_started" not in st.session_state:
        st.error("Unauthorized access. Please start the game from the main page.")
        st.stop()
    st.session_state["game_started"] = False


data = get_capital()
if data:
    can_access_play_page()
    play_game()
