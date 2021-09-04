from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Constructor"""
        super().__init__(**kwargs)
        self.names = ['James', 'John', 'Wanda', 'Mary']

    def build(self):
        """Build Function"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from given text"""
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return


if __name__ == "__main__":
    app = DynamicLabelsApp()
    app.run()
