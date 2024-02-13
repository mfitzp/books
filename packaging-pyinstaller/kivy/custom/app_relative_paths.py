import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

basedir = os.path.dirname(__file__)
Window.size = (300, 200)


class ImageButton(ButtonBehavior, Image):
    pass


class MainWindow(BoxLayout):
    def __init__(self):
        super().__init__()
        button = ImageButton(
            source=os.path.join(basedir, "icon.png"),
            size=(32, 32),
            pos=(16, 100 - 16),
        )
        button.bind(on_press=self.handle_button_clicked)
        self.add_widget(button)

    def handle_button_clicked(self, event):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        self.title = "Hello World"
        self.icon = os.path.join(basedir, "icon.png")
        return MainWindow()


app = MyApp()
app.run()
