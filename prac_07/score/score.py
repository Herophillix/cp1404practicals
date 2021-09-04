from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

GRADES = {50: "Fail", 65: "Pass", 75: "Credit", 85: "Distinction", 101: "High Distinction"}


class ScoreApp(App):
    """Application to check a user's score"""
    result = StringProperty()

    def build(self):
        """Build Function"""
        self.title = "Score Checker"
        self.root = Builder.load_file("score.kv")
        return self.root

    def check_score(self, score_text):
        """Check the score that is given by the user"""
        score = clamp(get_float(score_text), 0, 100)
        for max_score, grade in GRADES.items():
            if score < max_score:
                self.result = grade
                break


def get_float(text: str):
    """Get a float from a string with error checking"""
    try:
        return_value = float(text)
        return return_value
    except ValueError:
        return 0.0


def clamp(value: float, min_value: float, max_value: float):
    """Clamp a number within a range"""
    max_value = max_value if min_value < max_value else max_value
    if value < min_value:
        value = min_value
    elif value > max_value:
        value = max_value
    return value


if __name__ == "__main__":
    app = ScoreApp()
    app.run()
