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


class Cell:
    """Cell content of a table"""
    def __init__(self, content: str, alignment='<', alignment_value=0):
        self.content = content
        self.alignment = alignment if alignment in ['<', '>', '^'] else '<'
        self.alignment_value = alignment_value if alignment_value > 0 else len(content)

    def get_formatted_content(self):
        """Create a formatted content to be printed in the table"""
        return "{0:{a}{v}}".format(self.content[:self.alignment_value], a=self.alignment, v=self.alignment_value)


class Table:
    """Table to print scores in a nice format"""
    buffer = "buffer"

    def __init__(self):
        self.print_stacks = []
        self.buffer_content = ''
        self.add_buffer()

    def add_stack(self, cells: [Cell]):
        """Add cells into the stack"""
        self.print_stacks.append(cells)

    def add_buffer(self):
        """Add buffer into the stack"""
        self.print_stacks.append(Table.buffer)

    def set_buffer_size(self, sizes: [int]):
        """Create the buffer content"""
        self.buffer_content = '+'
        for size in sizes:
            self.buffer_content = self.buffer_content + '-' * (size + 2) + '+'

    def print_table(self):
        """Print the table"""
        for stack in self.print_stacks:
            if stack is Table.buffer:
                print(self.buffer_content)
            else:
                cells = stack
                print('|', end='')
                for cell in cells:
                    print(" {0} |".format(cell.get_formatted_content()), end='')
                print()


class Subject:
    """Subject in the class"""
    def __init__(self, class_name: str):
        self.name = class_name
        self.scores = []

    def print_scores(self):
        """Print all the scores"""
        for score in self.scores:
            print(score)

    def max_score(self):
        """Return maximum score in the list"""
        return max(self.scores)

    def min_score(self):
        """Return minimum score in the list"""
        return min(self.scores)

    def average_score(self):
        """Return average score"""
        return sum(self.scores) / len(self.scores)


def analyze_scores(scores_data):
    """Analyze the scores in the data"""
    subjects = []
    for subject_name in scores_data[0].strip().split(","):
        subject = Subject(subject_name)
        subjects.append(subject)

    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        for i in range(len(score_numbers)):
            subjects[i].scores.append(score_numbers[i])
    return subjects


def print_subjects(subjects):
    """Print the subjects with its scores and analyzed data"""
    for subject in subjects:
        print("{0} Scores:".format(subject.name))
        subject.print_scores()
        print("Max: {0}".format(subject.max_score()))


def print_subjects_table(subjects):
    """Print the subjects in a table"""
    table = Table()

    # create a header
    subject_string = "Subject"
    columns_char_size = [len(subject_string)]
    header_rows = [Cell(subject_string)]

    num_of_scores = 0

    for subject in subjects:
        columns_char_size.append(len(subject.name))
        header_rows.append(Cell(subject.name))

        num_of_scores = num_of_scores if num_of_scores > len(subject.scores) else len(subject.scores)

    table.set_buffer_size(columns_char_size)
    table.add_stack(header_rows)
    table.add_buffer()

    # add all the scores into separate rows
    for i in range(num_of_scores):
        score_rows = [Cell('', alignment_value=len(subject_string))]
        for subject in subjects:
            if i < len(subject.scores):
                score_rows.append(Cell(str(subject.scores[i]), '>', len(subject.name)))
            else:
                score_rows.append(Cell('', '>', len(subject.name)))
        table.add_stack(score_rows)
        table.add_buffer()

    # add all the analyzed data into separate rows
    min_columns = [Cell('Min', alignment_value=len(subject_string))]
    max_columns = [Cell('Max', alignment_value=len(subject_string))]
    average_columns = [Cell('Average', alignment_value=len(subject_string))]
    for subject in subjects:
        min_columns.append(Cell(str(subject.min_score()), '>', len(subject.name)))
        max_columns.append(Cell(str(subject.max_score()), '>', len(subject.name)))
        average_columns.append(Cell(str(subject.average_score()), '>', len(subject.name)))

    table.add_stack(min_columns)
    table.add_buffer()
    table.add_stack(max_columns)
    table.add_buffer()
    table.add_stack(average_columns)
    table.add_buffer()

    table.print_table()


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    scores_file.close()

    subjects = analyze_scores(scores_data)
    print_subjects_table(subjects)


if __name__ == "__main__":
    main()
