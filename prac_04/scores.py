"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


class Subject:
    def __init__(self, class_name):
        self.name = class_name
        self.scores = []

    def print_scores(self):
        for score in self.scores:
            print(score)

    def max_score(self):
        return max(self.scores)

    def min_score(self):
        return min(self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    scores_file.close()

    subjects = []
    for subject_name in scores_data[0].strip().split(","):
        subject = Subject(subject_name)
        subjects.append(subject)

    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        for i in range(len(score_numbers)):
            subjects[i].scores.append(score_numbers[i])

    for subject in subjects:
        print("{0} Scores:".format(subject.name))
        subject.print_scores()
        print("Max: {0}".format(subject.max_score()))


if __name__ == "__main__":
    main()
