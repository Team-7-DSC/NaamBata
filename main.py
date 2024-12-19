import pandas as pd

def akinator_game():
    # Load the dataset
    file_path = '/content/Seniors.csv'  # Update the path if needed
    data = pd.read_csv(file_path)

    # Clean column names (strip spaces)
    data.columns = data.columns.str.strip()

    # Print dataset preview for debugging
    # print("Dataset preview:")
    # print(data.head())
    # print("\nUnique values for relevant columns:")
    # print(data.nunique())  # Print unique values for insight

    # Copy dataset into candidates
    candidates = data.copy()

    # Helper function to ask a question and filter candidates
    def ask_question(column, question, positive_response, negative_response):
        nonlocal candidates  # Ensure we're modifying the global candidates variable

        if candidates.shape[0] <= 1:  # Stop asking questions if there's only one candidate left
            return True

        response = input(f"{question} (yes/no): ").strip().lower()

        if response == "yes":
            candidates = candidates[
                candidates[column].astype(str).str.strip().str.lower() == positive_response.lower()
            ]
        elif response == "no":
            candidates = candidates[
                candidates[column].astype(str).str.strip().str.lower() == negative_response.lower()
            ]
        else:
            print("Invalid input! Please answer 'yes' or 'no'.")
            return ask_question(column, question, positive_response, negative_response)  # Retry if invalid input

        # Print remaining candidates after filtering
        # print(f"Candidates remaining after filtering for {question}:")
        # print(candidates[['name']])
        return False  # Continue to the next question

    # Define the list of questions
    questions = [
        ("fav_ser_modernfamily", "Is the person's favorite series Modern Family?", "yes", "no"),
        ("cooking", "Does the person have a special skill of cooking?", "yes", "no"),
        ("curly_hair", "Does the person have curly hair?", "yes", "no"),
        ("iron_man", "Is the person's favorite movie Iron Man?", "yes", "no"),
        ("fav_ser_houseofnight", "Is the person's favorite series House of Night?", "yes", "no"),
        ("fav_ser_breakingbad", "Is the person's favorite series Breaking Bad?", "yes", "no"),
        ("interstellar", "Is the person's favorite movie Interstellar?", "yes", "no"),
        ("fav_col_green", "Is the person's favorite color lime green?", "yes", "no"),
        ("fav_ser_lucifer", "Is the person's favorite series Lucifer?", "yes", "no"),
        ("fav_col_blue", "Is the person's favorite color blue?", "blue", "no"),
        ("fav_ser_brooklyn99", "Is the person's favorite series Brooklyn 99?", "yes", "no"),
        ("i_want_to_eat_your_pancreas", "Is the person's favorite movie I Want To Eat Your Pancreas?", "yes", "no"),
        ("fav_col_purple", "Is the person's favorite color purple?", "yes", "no"),
        ("fav_ser_mentalist", "Is the person's favorite series The Mentalist?", "yes", "no"),
        ("straight_hair", "Does the person have straight hair?", "yes", "no"),
        ("ambivert", "Is the person an ambivert?", "yes", "no"),
        ("3_idiots", "Is the person's favorite movie 3 Idiots?", "yes", "no"),
        ("fav_col_black", "Is the person's favorite color black?", "yes", "no"),
        ("ring", "Does the person wear a ring?", "yes", "no"),
        ("introvert", "Is the person an introvert?", "yes", "no"),
        ("one_of_us_is_lying", "Is the person's favorite book One of Us is Lying?", "yes", "no"),
        ("57_seconds", "Is the person's favorite movie 57 Seconds?", "yes", "no"),
        ("cracking_the_coding_interview", "Is the person's favorite book Cracking the Coding Interview?", "yes", "no"),
        ("wavy_hair", "Does the person have wavy hair?", "yes", "no"),
        ("fav_ser_drhouse", "Is the person's favorite series Doctor House?", "yes", "no"),
        ("midnight_library", "Is the person's favorite book Midnight Library?", "yes", "no"),
        ("extrovert", "Is the person an extrovert?", "yes", "no"),
        ("travel", "Has the person visited/wants to visit Niagara Falls?", "niagara falls", "no"),
        ("steve_jobs_biography", "Is the person's favorite book Steve Jobs biography?", "yes", "no"),
        ("basketball", "Did the person play basketball?", "yes", "no"),
        ("mission_impossible", "Is the person's favorite movie Mission Impossible?", "yes", "no"),
        ("percy_jackson_book", "Is the person's favorite book Percy Jackson series?", "yes", "no"),
        ("harry_potter_book", "Is the person's favorite book Harry Potter series?", "yes", "no"),
        ("percy_jackson_movie", "Is the person's favorite movie Percy Jackson?", "yes", "no"),
        ("harry_potter_movie", "Is the person's favorite movie Harry Potter?", "yes", "no"),
        ("i_am_legend", "Is the person's favorite movie I Am Legend?", "yes", "no")
    ]


    # Ask questions in order
    for column, question_text, positive_response, negative_response in questions:
        print(f"\nAsking: {question_text}")

        # Check if we already have only one candidate before asking the next question
        if candidates.shape[0] == 1:
            person = candidates.iloc[0]
            print("\nI think the person is:")
            print(f"Name: {person['name']}")
            break

        stop = ask_question(column, question_text, positive_response, negative_response)

        # If we have narrowed down to one candidate, stop further questioning
        if candidates.shape[0] == 1:
            person = candidates.iloc[0]
            print("\nI think the person is:")
            print(f"Name: {person['name']}")
            break

        # If no candidates match, stop the game
        elif candidates.shape[0] == 0:
            print("\nI couldn't guess the person! No matches found.")
            break

    # If multiple candidates remain, list them
    if candidates.shape[0] > 1:
        print("\nI couldn't narrow it down to one person. Remaining possibilities:")
        # print(candidates["name"].tolist())

# Run the game
akinator_game()
