import re

from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix
from kivy.core.window import Window

from data.points_dict import PointsDict

class Overview(GridLayout):
    points_dict = PointsDict().list()

    def __init__(self, **kwargs):
        super(Overview, self).__init__(**kwargs)
        self.cols=3
        self.step_list = []
        self.description = ""

    def generate(self, *args, **kwargs):
        instructions = kwargs['step_list']
        for description, steps in instructions.items():
            self.step_list += steps
            self.description += (f" => {description} {steps}")
        key = kwargs['key']

        self.add_widget(
            Label(
                text=self.description,
                text_size=(100,500),
                valign='middle',
                size_hint_x=.2
            )
        )

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.35)
            for step in self.step_list:
                left = str(step) + ".L"
                right = str(step) + ".R"

                for key in [str(step), left, right]:
                    try:
                        coords = self.points_dict[str(key)]
                        image.points.point.add_point(coords[0],coords[1])
                    except:
                        print('Not a point or no point found')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.4)
        scatter.apply_transform(Matrix().scale(8,8,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/DoHInhTracDien.jpg")
            image.points = Widget()
            image.points.canvas.add(Color(1,0,0)) 
            image.points.point = Point(pointsize=.35)
            for step in self.step_list:
                adjacent = str(step) + ".A"
                try:
                    coords = self.points_dict[str(adjacent)]
                    image.points.point.add_point(coords[0],coords[1])
                except:
                    print('Not a point or no point found')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.4)
        scatter.apply_transform(Matrix().scale(8,8,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        return self

