"""
File: fuel_usage.py
Author: Tim Illguth
Professor: Christian Eisinger

"""
# List of statements for the program to reference. 
STATEMENTS = [
    "I feel that I am a person of worth, at least on an equal plane with others.",
    "I feel that I have a number of good qualities.",
    "All in all, I am inclined to feel that I am a failure.",
    "I am able to do things as well as most other people.",
    "I feel I do not have much to be proud of.",
    "I take a positive attitude toward myself.",
    "On the whole, I am satisfied with myself.",
    "I wish I could have more respect for myself.",
    "I certainly feel useless at times.",
    "At times I think I am no good at all."
]

def print_intro():
    # Print the introductory text.
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print("")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print("")


def get_user_response(statement_number):
    # Gets the user's responses for the agree and disagree questions. 
    response = input(f"{statement_number}. {STATEMENTS[statement_number-1]} Enter D, d, a, or A: ")
    return response


def compute_score(response):
    # If statement to take the responses and return a corrisponding number to calculate a result
    if response == 'D':
        return 0
    elif response == 'd':
        return 1
    elif response == 'a':
        return 2
    elif response == 'A':
        return 3
    else:
        # Returns a reeminder for what are valid responses
        print("Invalid response. Please enter D, d, a, or A.")
        return 0


def main():
    # Main function to execute the program.
    print_intro()

    total_score = 0

    for i in range(1, 11):
        user_response = get_user_response(i)
        statement_score = compute_score(user_response)
        total_score += statement_score

    print(f"Your score is {total_score}.")
    if total_score < 15:
        print("A score below 15 may indicate problematic low self-esteem.")
    else:
        print("Which means your self-esteem is about average. Self-discipline and accomplishment will raise your score")


main()
