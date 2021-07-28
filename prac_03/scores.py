"""
Generate random scores and save it into a .txt file
"""
import random
FILE_DIRECTORY = "results.txt"


def assess_grade(score):
    """Check the score and assign grade"""
    grade = ""
    if score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


def get_number_of_score():
    """Get the user to input a number of score"""
    is_input_valid = False
    while not is_input_valid:
        try:
            num_score = int(input("Number of scores: "))
            if num_score <= 0:
                print("Input a number greater than 0")
                continue
            is_input_valid = True
        except ValueError:
            print("Error, please input a number")
    return num_score


def main():
    """Get a number of score, and assess the grade and put it into a .txt file"""
    number_of_score = get_number_of_score()
    new_file = open(FILE_DIRECTORY, 'w')
    for i in range(0, number_of_score):
        score = random.randrange(0, 100)
        new_file.write("Your score is: {0}\n".format(score))
        new_file.write("Your grade is: {0}\n".format(assess_grade(score)))
    new_file.close()


if __name__ == "__main__":
    main()
