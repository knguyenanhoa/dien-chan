from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix

from sets import Sets
from points_dict import PointsDict
from layouts import DefaultLayout
from tabs.stepper import Stepper
from tabs.overview import Overview

class MainMenu(GridLayout):
    sets = Sets()
    points_dict = PointsDict()
    letters = ['A','B','C','D','E','G','H']

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 4

        self.show_main_menu()

    def show_main_menu(self, *args, **kwargs):
        self.clear_widgets()
        for letter in self.letters:
            button = Button(text=letter)
            button.bind(on_press=partial(self.show_sub_menu, letter=letter))
            self.add_widget(button)


    def show_sub_menu(self, *args, **kwargs):
        self.clear_widgets()
        letter = kwargs['letter']
        list = self.sets.list(key=letter)

        for key in list.keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_overview, key=key, list=list, letter=letter))
            self.add_widget(button)

    def show_overview(self, *args, **kwargs):
        current_letter = kwargs['letter']
        step_list = kwargs['list'][kwargs['key']]

        self.clear_widgets()
        self.default_layout = DefaultLayout()
        self.add_widget(self.default_layout)

        ####map
        scatter = self.construct_overview(step_list,)
        stepper = self.construct_stepper(step_list,)
        stepper_controls = self.construct_stepper_controls(step_list,)

        tp = self.create_tabbed_panel(tab1=scatter,tab2_1=stepper,tab2_2=stepper_controls)
        self.default_layout.map.add_widget(tp)

        ####context_menu
        button = Button(text='Back', size_hint_x=.1)
        button.bind(on_press=partial(self.show_sub_menu, letter=current_letter))
        self.default_layout.context_menu.add_widget(button)

        button = Button(text='Main', size_hint_x=.1)
        button.bind(on_press=partial(self.show_main_menu))
        self.default_layout.context_menu.add_widget(button)

        steps = ""
        for point in step_list:
            steps += (" => %s" % point)
        label = Label(text=steps, size_hint_x=.8, color=[1,0,0,1], bold=True)
        self.default_layout.context_menu.add_widget(label)
        








    def construct_stepper_controls(self, step_list,):
        label = Button(text='test', size_hint_x=.1)

        return label

    def construct_stepper(self, step_list,):
        points_dict = self.points_dict.list()
        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.3)
            for step in step_list:
                try:
                    coords = points_dict[str(step)]
                    image.points.point.add_point(coords[0],coords[1])
                except:
                    print('No point')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.9)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)

        return scatter

    def construct_overview(self, step_list,):
        points_dict = self.points_dict.list()
        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.3)
            for step in step_list:
                try:
                    coords = points_dict[str(step)]
                    image.points.point.add_point(coords[0],coords[1])
                except:
                    print('No point')

        scatter = Scatter(auto_bring_to_front=False)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)

        return scatter

    def create_tabbed_panel(self, *args, **kwargs):
        tp = TabbedPanel(do_default_tab=False)

        tab1 = TabbedPanelHeader(text='Overview')
        tp.add_widget(tab1)
        tab2 = TabbedPanelHeader(text='Step')
        tp.add_widget(tab2)

        tab1.content = GridLayout(cols=1)
        tab2.content = Stepper()

        tab1.content.add_widget(kwargs['tab1'])

        return tp

