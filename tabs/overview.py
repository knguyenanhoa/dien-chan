from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix

class Overview(GridLayout):
    def __init__(self, **kwargs):
        super(Overview, self).__init__(**kwargs)
        self.cols=1

    def generate(self, step_list, points_dict,):
        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.3)
            for step in step_list:
                try:
                    coords = points_dict[str(step)]
                    print(coords)
                    image.points.point.add_point(coords[0],coords[1])
                except:
                    print('No point')

        scatter = Scatter(auto_bring_to_front=False)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        return self

