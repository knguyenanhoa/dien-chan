import subprocess

from functools import partial
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.graphics import *

from data.sets import Sets
from data.legend import Legend
from layouts import DefaultLayout
from tabs.stepper import Stepper
from tabs.overview import Overview
from tabs.locator import Locator

class MainMenu(GridLayout):
    sets = Sets()
    legend = Legend()
    letters = ['A','B','C','D','E','G',
        'H','I','K','L','M','N',
        'O','P','Q','R','S','T',
        'U','V','X','Y'
    ]
    current_letter = None
    current_key = None
    current_key_list = None
    current_step_list = None

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 6

        self.show_main_menu()

    def show_main_menu(self, *args, **kwargs):
        self.clear_widgets()
        Window.set_title('Main')

        for letter in self.letters:
            button = Button(text=letter)
            button.bind(on_press=partial(self.show_sub_menu, letter=letter))
            self.add_widget(button)

        button = Button(text='Locate')
        button.bind(on_press=self.show_locator)
        self.add_widget(button)

    def show_locator(self, *args, **kwargs):
        self.clear_widgets()
        Window.set_title('Locator')

        self.default_layout = DefaultLayout()
        self.add_widget(self.default_layout)

        ####top
        locator = Locator().generate(point=0)
        self.default_layout.main.add_widget(locator)

        ####bottom
        button = Button(text='Main', size_hint_x=.1)
        button.bind(on_press=partial(self.show_main_menu))
        self.default_layout.context_menu.add_widget(button)

    def show_sub_menu(self, *args, **kwargs):
        self.clear_widgets()
        Window.set_title('Sub')

        self.current_letter = kwargs['letter']
        self.current_key_list = self.sets.list(key=self.current_letter)

        for key in self.current_key_list.keys():
            button = Button(
                    text=key,
                    text_size=(100,500),
                    valign='middle',
                    halign='center',
                    )
            button.bind(on_press=partial(self.show_overview, key=key))
            self.add_widget(button)

    def show_overview(self, *args, **kwargs):

        self.current_key = kwargs['key']
        self.current_step_list = self.current_key_list[self.current_key]

        self.clear_widgets()
        Window.set_title(self.current_key)
        self.default_layout = DefaultLayout()
        self.add_widget(self.default_layout)

        ####top
        tp = self.create_tabbed_panel()
        self.default_layout.main.add_widget(tp)

        ####bottom
        button = Button(text='Back', size_hint_x=.1)
        button.bind(on_press=partial(self.show_sub_menu, letter=self.current_letter))
        self.default_layout.context_menu.add_widget(button)

        button = Button(text='Main', size_hint_x=.1)
        button.bind(on_press=partial(self.show_main_menu))
        self.default_layout.context_menu.add_widget(button)

        steps = ""
        for point in self.current_step_list:
            steps += (" => %s" % point)
        label = Label(text=steps, size_hint_x=.8, color=[1,0,0,1], bold=True)
        self.default_layout.context_menu.add_widget(label)

        button = Button(text='Print', size_hint_x=.1)
        #doesnt work yet
        button.bind(on_press=partial(self.printer))
        self.default_layout.context_menu.add_widget(button)

        self.legend_on = Button(text='Legend', size_hint_x=.1)
        self.legend_on.bind(on_press=self.show_legend)
        self.default_layout.context_menu.add_widget(self.legend_on)






    def show_legend(self, *args, **kwargs):
        legend_list = self.legend.list()

        self.default_layout.context_menu.remove_widget(self.legend_on)
        self.legend_off = Button(text='Overview', size_hint_x=.1)
        self.legend_off.bind(on_press=partial(self.show_overview, key=self.current_key))
        self.default_layout.context_menu.add_widget(self.legend_off)

        self.default_layout.main.clear_widgets()
        self.legend_layout = GridLayout(cols=6)
        self.default_layout.main.add_widget(self.legend_layout)

        for key in legend_list.keys():
            legend = "%s => %s" % (key,legend_list[key])
            button = Button(text=legend, color=[1,0,0,1])
            self.legend_layout.add_widget(button)

    def printer(self, *args, **kwargs):
        pass

        #try:
        #    path = "./images/print.png"
        #    result = subprocess.run(["lpr",path])
        #except:
        #    print('No image')

    def create_tabbed_panel(self, *args, **kwargs):
        tp = TabbedPanel(do_default_tab=False)

        tab1 = TabbedPanelHeader(text='Overview')
        tp.add_widget(tab1)
        tab2 = TabbedPanelHeader(text='Step')
        tp.add_widget(tab2)

        tab1.content = Overview().generate(step_list=self.current_step_list, key=self.current_key,)
        tab2.content = Stepper().generate(step_list=self.current_step_list, current_point=0,)
        # current_point=0 to init only

        return tp

