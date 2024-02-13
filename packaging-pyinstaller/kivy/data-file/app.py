import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label

basedir = os.path.dirname(__file__)
Window.size = (300, 200)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class MainWindow(BoxLayout):
    def __init__(self):
        super().__init__(orientation="vertical")
        label = Label(text="My simple app.")

        button = ImageButton(
            source=os.path.join(basedir, "icon.png"),
            size=(32, 32),
            pos=(16, 50 - 16),
        )

        button.bind(on_press=self.handle_button_clicked)

        self.add_widget(label)
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
