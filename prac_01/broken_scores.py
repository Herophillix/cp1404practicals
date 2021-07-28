"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score, try again!")
        score = float(input("Enter score: "))
    grade = ""
    if score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    print("Your grade is:", grade)


if __name__ == '__main__':
    main()
