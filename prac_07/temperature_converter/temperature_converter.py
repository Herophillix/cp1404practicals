from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"


class TemperatureConverterApp(App):
    input = StringProperty("0.0")
    input_unit = StringProperty()
    output = StringProperty("0.0")
    output_unit = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_input_celsius = True

    def build(self):
        self.title = "Temperature Converter"
        Window.size = (960, 540)
        self.root = Builder.load_file("temperature_converter.kv")
        self.sort_units()
        return self.root

    def convert(self, value_text):
        value = get_float(value_text)
        if self.is_input_celsius:
            converted_value = value * 9.0 / 5 + 32
        else:
            converted_value = 5 / 9 * (value - 32)
        self.output = str(converted_value)

    def swap(self):
        self.is_input_celsius = not self.is_input_celsius
        self.sort_units()

    def sort_units(self):
        self.input_unit = CELSIUS if self.is_input_celsius else FAHRENHEIT
        self.output_unit = FAHRENHEIT if self.is_input_celsius else CELSIUS
        self.input = self.output
        self.convert(self.input)


def get_float(text: str):
    try:
        return_value = float(text)
        return return_value
    except ValueError:
        return 0.0


if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.run()
