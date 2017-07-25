from functools import partial
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sets import Sets


class MainMenu(GridLayout):
    sets = Sets()

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 1
        self.initialize()

    def initialize(self):
        for key in self.sets.list_sets().keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_positions,key))
            self.add_widget(button)

    def show_positions(self, *args):
        self.clear_widgets()
        label = Label(text=args[0], height=200)
        self.add_widget(label)
        button = Button(text='Close', height=15)
        button.bind(on_press=partial(self.show_main_menu))
        self.add_widget(button)
        
    def show_main_menu(self, *args):
        self.clear_widgets()
        for key in self.sets.list_sets().keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_positions,key))
            self.add_widget(button)


class DienChanApp(App):
    def build(self):
        return MainMenu()

#MAIN
DienChanApp().run()

