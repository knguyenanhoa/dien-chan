from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from sets import Sets


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        sets = Sets()
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        for key in sets.list_sets().keys():
            self.add_widget(Button(text=key))

class DienChanApp(App):
    def build(self):
        return LoginScreen()


DienChanApp().run()
