from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


def get_float(text: str):
    """Get a float from a string with error checking"""
    try:
        return_value = float(text)
        return return_value
    except ValueError:
        return 0.0


class DistanceConverterApp(App):
    """Application to convert miles to kilometer"""
    km_output = StringProperty()

    def build(self):
        """Build Function"""
        self.title = "Distance Converter"
        Window.size = (480, 270)
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert(self):
        value = get_float(self.root.ids.mi_input.text)
        converted_value = value * MILES_TO_KM
        self.km_output = str(converted_value)

    def increment(self, add_value):
        value = get_float(self.root.ids.mi_input.text)
        new_value = value + add_value if value + add_value > 0.0 else 0.0
        self.root.ids.mi_input.text = str(new_value)


if __name__ == "__main__":
    app = DistanceConverterApp()
    app.run()
