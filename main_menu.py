from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix

from sets import Sets
from points_dict import PointsDict

class MainMenu(GridLayout):
    sets = Sets()
    points_dict = PointsDict()
    letters = ['A','B','C','D','E','G','H']

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 4
        self.initialize()

    def initialize(self):
        for letter in self.letters:
            button = Button(text=letter)
            button.bind(on_press=partial(self.dial_letter,letter=letter))
            self.add_widget(button)


    def dial_letter(self, *args, **kwargs):
        self.clear_widgets()

        for key in self.sets.list(key=kwargs['letter']).keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_positions,key=key))
            self.add_widget(button)

    def construct_overlay(self, step_list,):
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

        return image

    def show_positions(self, *args, **kwargs):
        self.clear_widgets()
        step_list = self.sets.list(key='H')[kwargs['key']]

        show_layout = GridLayout(cols=1)
        self.add_widget(show_layout)

        map = GridLayout(cols=1, size_hint_y=.9)
        show_layout.add_widget(map)
        context_menu = GridLayout(cols=3, size_hint_y=.1)
        show_layout.add_widget(context_menu)

        #map
        scatter = Scatter(auto_bring_to_front=False)
        scatter.apply_transform(Matrix().scale(6,6,1))
        map.add_widget(scatter)

        image = self.construct_overlay(step_list,)
        scatter.add_widget(image)


        #context_menu
        button = Button(text='Back', size_hint_x=.2)
        button.bind(on_press=partial(self.show_sub_menu))
        context_menu.add_widget(button)

        button = Button(text='Main', size_hint_x=.2)
        button.bind(on_press=partial(self.show_main_menu))
        context_menu.add_widget(button)

        steps = ""
        for point in step_list:
            steps += (" => %s" % point)
        label = Label(text=steps, size_hint_x=.6, color=[1,0,0,1], bold=True)
        context_menu.add_widget(label)
        
    def show_sub_menu(self, *args, **kwargs):
        self.clear_widgets()
        for key in self.sets.list(key='H').keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_positions,key=key))
            self.add_widget(button)

    def show_main_menu(self, *args, **kwargs):
        self.clear_widgets()
        for letter in self.letters:
            button = Button(text=letter)
            button.bind(on_press=partial(self.dial_letter,letter=letter))
            self.add_widget(button)

