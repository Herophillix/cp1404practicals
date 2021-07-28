"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


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


def main():
    """Ask user to input score and get their grades"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score, try again!")
        score = float(input("Enter score: "))
    print("Your grade is:", assess_grade(score))

    score = random.randrange(0, 100)
    print("Your random score is:", score)
    print("Your grade is:", assess_grade(score))


if __name__ == '__main__':
    main()
