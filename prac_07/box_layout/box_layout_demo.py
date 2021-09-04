from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class BoxLayoutDemo(App):
    """Demo of the box layout"""
    message = StringProperty("Input your name")

    def build(self):
        """Build Function"""
        self.title = "Greeter"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def clear(self):
        self.message = "Input your name"
        self.root.ids.name.text = ""

    def greet(self):
        self.message = "Hello " + self.root.ids.name.text


BoxLayoutDemo().run()
