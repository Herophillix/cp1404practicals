"""
Class for printing values in a table
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