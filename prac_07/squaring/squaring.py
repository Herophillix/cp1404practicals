"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
James Makarios, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'James Makarios'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """Build Function"""
        self.title = "Square Number"
        Window.size = (480, 270)
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = int(self.root.ids.input_number.text)
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
