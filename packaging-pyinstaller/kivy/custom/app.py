from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (300, 200)


class MainWindow(BoxLayout):
    def __init__(self):
        super().__init__()
        button = Button(text="My simple app.")
        button.bind(on_press=self.handle_button_clicked)

        self.add_widget(button)

    def handle_button_clicked(self, event):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        self.title = "Hello World"
        self.icon = "icon.png"
        return MainWindow()


app = MyApp()
app.run()
