from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix

class Stepper(GridLayout):
    def __init__(self, **kwargs):
        super(Stepper, self).__init__(**kwargs)
        self.cols=2
        self.generate()

    def generate(self):
        label = Label(text='test', size_hint_x=.9)
        self.add_widget(label)
        button = Button(text='test button', size_hint_x=.1)
        self.add_widget(button)

