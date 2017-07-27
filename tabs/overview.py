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
        self.cols=1

    def generate(self, *args, **kwargs):
        step_list = kwargs['step_list']

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.35)
            for step in step_list:
                try:
                    coords = self.points_dict[str(step)]
                    image.points.point.add_point(coords[0],coords[1])
                except:
                    print('No point')

        scatter = Scatter(auto_bring_to_front=False)
        scatter.apply_transform(Matrix().scale(6.5,6.5,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        return self

