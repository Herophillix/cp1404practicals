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
    def __init__(self, content: str, alignment='<'):
        self.content = content
        self.alignment = alignment if alignment in ['<', '>', '^'] else '<'

    def get_formatted_content(self, alignment_value):
        """Create a formatted content to be printed in the table"""
        return "{0:{a}{v}}".format(self.content[:alignment_value], a=self.alignment, v=alignment_value)


class Table:
    """Table to print scores in a nice format"""
    buffer = "buffer"

    def __init__(self):
        self.print_stacks = []
        self.column_spacing = []
        self.add_buffer()

    def column_count(self):
        """Return the count of columns"""
        return len(self.column_spacing)

    def row_count(self):
        """Return the count of rows"""
        return len(self.print_stacks) - self.print_stacks.count(Table.buffer)

    def add_row(self, cells: [Cell]):
        """Add a row into the stack"""
        column_count = self.column_count()
        if column_count < len(cells):
            for i in range(column_count, len(cells)):
                self.column_spacing.append(len(cells[i].content))

        for i in range(len(cells)):
            old_spacing = self.column_spacing[i]
            new_spacing = len(cells[i].content)
            self.column_spacing[i] = old_spacing if old_spacing > new_spacing else new_spacing

        self.print_stacks.append(cells)

    def add_buffer(self):
        """Add buffer into the stack"""
        self.print_stacks.append(Table.buffer)

    def get_buffer(self):
        """Create the buffer content"""
        buffer_content = '+'
        for size in self.column_spacing:
            buffer_content = buffer_content + '-' * (size + 2) + '+'
        return buffer_content

    def print_table(self):
        """Print the table"""
        buffer_content = self.get_buffer()
        for stack in self.print_stacks:
            if stack is Table.buffer:
                print(buffer_content)
            else:
                cells = stack
                print('|', end='')
                for i, cell in enumerate(cells):
                    print(" {0} |".format(cell.get_formatted_content(self.column_spacing[i])), end='')
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
    header_rows = [Cell("Subject")]

    num_of_scores = 0

    for subject in subjects:
        header_rows.append(Cell(subject.name))

        num_of_scores = num_of_scores if num_of_scores > len(subject.scores) else len(subject.scores)

    table.add_row(header_rows)
    table.add_buffer()

    # add all the scores into separate rows
    for i in range(num_of_scores):
        score_rows = [Cell("Student {0}".format(i + 1))]
        for subject in subjects:
            if i < len(subject.scores):
                score_rows.append(Cell(str(subject.scores[i]), '>'))
            else:
                score_rows.append(Cell('', '>'))
        table.add_row(score_rows)
        table.add_buffer()

    # add all the analyzed data into separate rows
    min_columns = [Cell('Min')]
    max_columns = [Cell('Max')]
    average_columns = [Cell('Average')]
    for subject in subjects:
        min_columns.append(Cell(str(subject.min_score()), '>'))
        max_columns.append(Cell(str(subject.max_score()), '>'))
        average_columns.append(Cell(str(subject.average_score()), '>'))

    table.add_row(min_columns)
    table.add_buffer()
    table.add_row(max_columns)
    table.add_buffer()
    table.add_row(average_columns)
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
