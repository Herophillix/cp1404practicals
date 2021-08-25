"""
Describe the different programming languages
"""
from programming_language import *


def main():
    """Describe the different programming languages"""
    languages = []
    java = ProgrammingLanguage("Java", TypingStyle.STATIC, True, 1995)
    languages.append(java)
    cpp = ProgrammingLanguage("C++", TypingStyle.STATIC, False, 1983)
    languages.append(cpp)
    python = ProgrammingLanguage("Python", TypingStyle.DYNAMIC, True, 1991)
    languages.append(python)
    visual_basic = ProgrammingLanguage("Visual Basic", TypingStyle.STATIC, False, 1991)
    languages.append(visual_basic)
    ruby = ProgrammingLanguage("Ruby", TypingStyle.DYNAMIC, True, 1995)
    languages.append(ruby)

    for language in languages:
        print(language)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
