"""
Describe features of a programming language
"""
from enum import IntEnum


class TypingStyle(IntEnum):
    """Typing style of a programming language"""
    STATIC = 0
    DYNAMIC = 1


class ProgrammingLanguage:
    """Describe features of a programming language"""

    def __init__(self, name: str, typing_style: TypingStyle, reflection: bool, year: int):
        """Constructor"""
        self.name = name
        self.typing_style = typing_style
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Description of class"""
        return "{0}, {1} Typing, Reflection={2}, First appeared in {3}".format(self.name,
                                                                               self.typing_style.name.title(),
                                                                               self.reflection, self.year)

    def is_dynamic(self):
        """Check if a language is dynamically typed"""
        return self.typing_style == TypingStyle.DYNAMIC
