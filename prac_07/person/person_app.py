from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

FILE_DIRECTORY = "people_database.txt"


class PersonApp(App):
    information = StringProperty()

    def __init__(self, **kwargs):
        """Constructor"""
        super().__init__(**kwargs)
        file = open(FILE_DIRECTORY, 'r')
        lines = file.readlines()
        file.close()

        self.people = {}
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                name = parts[0]
                age = get_int(parts[1])
                self.people[name] = age

    def build(self):
        """Build Function"""
        self.title = "Person Profile"
        self.root = Builder.load_file("person.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.people.keys():
            new_button = Button(text=name)
            new_button.bind(on_press=self.display_info)
            self.root.ids.person_holder.add_widget(new_button)

    def display_info(self, instance):
        self.information = str(self.people[instance.text])
        return


def get_int(text: str):
    try:
        return_value = int(text)
        return return_value
    except ValueError:
        return 0


if __name__ == "__main__":
    app = PersonApp()
    app.run()
