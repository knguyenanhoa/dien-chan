import re

from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix

from data.points_dict import PointsDict

class Stepper(GridLayout):
    points_dict = PointsDict().list()

    def __init__(self, **kwargs):
        super(Stepper, self).__init__(**kwargs)
        self.cols=3

    def generate(self, *args, **kwargs):
        self.clear_widgets()
        current_point = kwargs['current_point']
        step_list = kwargs['step_list']

        self.controls = GridLayout(cols=2, size_hint_x=.2)
        self.add_widget(self.controls)
        self.generate_controls(step_list, current_point,)

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.35)
            draw = re.compile("A")
            if draw.search(str(current_point)) == None:
                try:
                    coords = self.points_dict[str(current_point)]
                    image.points.point.add_point(coords[0],coords[1])
                    image.points.vline = Line(points=[coords[0],100,coords[0],0])
                    image.points.hline = Line(points=[13,coords[1],87,coords[1]])
                except:
                    print('Not a point or no point found')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.6)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/DoHInhTracDien.jpg")
            image.points = Widget()
            image.points.canvas.add(Color(1,0,0)) 
            image.points.point = Point(pointsize=.35)
            draw = re.compile("A")
            if draw.search(str(current_point)) != None:
                try:
                    coords = self.points_dict[str(current_point)]
                    image.points.point.add_point(coords[0],coords[1])
                    image.points.vline = Line(points=[coords[0],100,coords[0],0])
                    image.points.hline = Line(points=[13,coords[1],87,coords[1]])
                except:
                    print('Not a point or no point found')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.6)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        return self

    def generate_controls(self, step_list, current_point):
        for step in step_list:        
            button = Button(text=step)
            if step == current_point:
                button.color=[1,0,0,1]
            button.bind(on_press=partial(self.generate,step_list=step_list,current_point=step))
            self.controls.add_widget(button)

