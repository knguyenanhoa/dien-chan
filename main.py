from functools import partial
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

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
            button.bind(on_press=partial(self.show_positions,key=key))
            self.add_widget(button)

    def show_positions(self, *args, **kwargs):
        self.clear_widgets()
        #label = Label(text=kwargs['key'])
        #self.add_widget(label)
        image = Image(source="./images/do_hinh_dien_chan_2.png")
        self.add_widget(image)

        menu = GridLayout(cols=2, size_hint_y=None, height=100)
        self.add_widget(menu)
        button = Button(text='Close')
        button.bind(on_press=partial(self.show_main_menu))
        menu.add_widget(button)
        button = Button(text='Close')
        button.bind(on_press=partial(self.show_main_menu))
        menu.add_widget(button)
        
    def show_main_menu(self, *args):
        self.clear_widgets()
        for key in self.sets.list_sets().keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_positions,key=key))
            self.add_widget(button)


class DienChanApp(App):
    def build(self):
        return MainMenu()

#MAIN
DienChanApp().run()

