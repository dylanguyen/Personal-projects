# Programmers: [Dylan Nguyen]
# Course: CS151, Dr. Simari
# Programming Assignment: 5
# Program Inputs: [One of the three different sports, if the snitch is caught, pass attempts, pass completions, TD passes,/
#                  yards, interceptions, score of difficulty, scores of execution]
# Program Outputs: [quidditch points, passer rating, if QB is perfect passer, final gymnast score]

#-----------------------------------------------------------------------------------------------------------------------
# define quidditch calculation
def quidditch_calculation(number_of_goals, snitch_caught):

    # determining the total points
    quidditch_points = number_of_goals * 10

    # write condition for if snitch is caught or not
    if snitch_caught == "yes":
        quidditch_points += 30

        return quidditch_points
#-----------------------------------------------------------------------------------------------------------------------

# define calculation for football
def qb_calculation(attempts, completions, interceptions, passing_yards, td_passes):

    # determine the passer rating
    qb_rating = (completions/attempts - 0.3) * 5 + (passing_yards/attempts - 3) * 0.25
    #qb_rating += (td_passes/attempts) * 20 + 2.375 - (25 * interceptions/attempts)
    #qb_rating *= 100
    #qb_rating /= 6
    qb_rating = round(qb_rating, 1 )

    return qb_rating
#-----------------------------------------------------------------------------------------------------------------------

# define calculation for gymnastics
def gymnastics_calculation(scoring_difficulty, execution_1, execution_2, execution_3, execution_4, execution_5):

    # use max and min functions to identify scores
    max_execution_score = maximum_score(execution_1, execution_2, execution_3, execution_4, execution_5)
    min_execution_score = minimum_score(execution_1, execution_2, execution_3, execution_4, execution_5)

    # calculate the gymnast final score
    avg_execution = execution_1 + execution_2 + execution_3 + execution_4 + execution_5
    avg_execution -= (max_execution_score + min_execution_score)
    final_score = scoring_difficulty +(avg_execution / 3)
    final_score = round(final_score, 2)

    return final_score
#-----------------------------------------------------------------------------------------------------------------------

# define quidditch options
def quidditch_option():

    # ask the user for the inputs and check if it is valid
    number_of_goals = input("How many goals were scored?: ")
    number_of_goals = only_digits(number_of_goals)

    snitch_caught = input("Did you catch the snitch? (Yes or No): ")
    snitch_caught = snitch_caught.strip().lower()

    # call function to calculate total points
    total_quidditch_points = quidditch_calculation(number_of_goals,snitch_caught)

    print("\n\tYou scored",total_quidditch_points,"points in the quidditch game.")


#-----------------------------------------------------------------------------------------------------------------------

# define football options
def football_option():

    # ask the user for the inputs and check if it is valid
    attempts = input("How many passes were attempted?: ")
    attempts = only_digits(attempts)
    while attempts <= 0:
        print("Error. Please enter a number that is greater than 0.")
        attempts = input("How many passes were attempted?: ")
        attempts = only_digits(attempts)

    completions = input("How many passes were completed?: ")
    completions = only_digits(completions)

    interceptions = input("How many interceptions were thrown?: ")
    interceptions = only_digits(interceptions)

    passing_yards = input("Please enter the amount of passing yards.: ")
    passing_yards = only_digits(passing_yards)

    td_passes = input("How many touchdown passes were thrown?: ")
    td_passes = only_digits(td_passes)

    # call function to calculate qb rating
    qb_rating = qb_calculation(attempts,completions,interceptions,passing_yards,td_passes)

    print("Based on the stats that were inputed the quarterback has a passer rating of",qb_rating)

    # write conditional statement to determine whether or not the qb is perfect passer or not
    if qb_rating == 158.3:
        print("\n\tThe quarterback is a perfect passer!")
    else:
        print("\n\tThe quarterback is not a perfect passer.")
#-----------------------------------------------------------------------------------------------------------------------

# define gymnastics option
def gymnastics_option():
    scoring_difficulty = input("Please enter the scoring difficulty. (1-10): ")
    scoring_difficulty = only_digits(scoring_difficulty)

    execution_1 = input("Please enter the score of the first execution. (1-10)")
    execution_1 = only_digits(execution_1)

    execution_2 = input("Please enter the score of the second execution. (1-10)")
    execution_2 = only_digits(execution_2)

    execution_3 = input("Please enter the score of the third execution. (1-10)")
    execution_3 = only_digits(execution_3)

    execution_4 = input("Please enter the score of the fourth execution. (1-10)")
    execution_4 = only_digits(execution_4)

    execution_5 = input("Please enter the score of the fifth execution. (1-10)")
    execution_5 = only_digits(execution_5)

    # call function to calculate final score
    final_score = gymnastics_calculation(scoring_difficulty,execution_1,execution_2,execution_3,execution_4,execution_5)

    print("\n\tThe final score for the gymnastics routine is", final_score)
#-----------------------------------------------------------------------------------------------------------------------

# define function to determine minimum score
def minimum_score(execution_1, execution_2, execution_3, execution_4, execution_5):

    # identify the lowest score
    min_execution_score = execution_1
    if min_execution_score > execution_2:
        min_execution_score = execution_2

    if min_execution_score > execution_3:
        min_execution_score = execution_3

    if min_execution_score > execution_4:
        min_execution_score = execution_4

    if min_execution_score > execution_5:
        min_execution_score = execution_5

    return min_execution_score

#-----------------------------------------------------------------------------------------------------------------------

# define function to determine maximum score
def maximum_score(execution_1, execution_2, execution_3, execution_4, execution_5):

    # identify the highest score
    max_execution_score = execution_1

    if max_execution_score < execution_2:
        max_execution_score = execution_2

    if max_execution_score < execution_3:
        max_execution_score = execution_3

    if max_execution_score < execution_4:
        max_execution_score = execution_4

    if max_execution_score < execution_4:
        max_execution_score = execution_5

    return max_execution_score
#-----------------------------------------------------------------------------------------------------------------------

# define "only digits" function
def only_digits(user_value):

    # check the input is only digits
    while not user_value.isdigit():
        print("Error. Please input a numerical value.")
        user_value = input("Enter a valid value:")

    user_value = int(user_value)
    return user_value
#-----------------------------------------------------------------------------------------------------------------------

# define main function
def main():

    # output purpose to user
    print("The purpose of this program is to calculate the desired stats for the desired sport.")

    # ask user which sport they would like to calculate
    sport_selection = input("\nPlease enter the sport you would like to calculate stats for. (quidditch, football, or "
    "gymnastics): ")
    sport_selection = sport_selection.strip().lower()

    if sport_selection == "quidditch":
            quidditch_option()

    elif sport_selection == "football":
        football_option()

    elif sport_selection == "gymnastics":
        gymnastics_option()

    else:
        print("\nERROR. Please enter a valid sport. (football, gymnastics, or quidditch")

main()




























