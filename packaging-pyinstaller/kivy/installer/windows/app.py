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

        button_close = ImageButton(
            source=os.path.join(basedir, "icons", "lightning.png"),
        )

        button_close.bind(on_press=self.handle_close_button_clicked)

        button_maximize = ImageButton(
            source=os.path.join(basedir, "icons", "uparrow.png"),
        )

        button_maximize.bind(
            on_press=self.handle_maximize_button_clicked
        )

        self.add_widget(label)
        self.add_widget(button_close)
        self.add_widget(button_maximize)

    def handle_close_button_clicked(self, event):
        App.get_running_app().stop()

    def handle_maximize_button_clicked(self, event):
        Window.size = (600, 400)


class MyApp(App):
    def build(self):
        self.title = "Hello World"
        self.icon = os.path.join(basedir, "icons", "icon.png")
        return MainWindow()


app = MyApp()
app.run()
