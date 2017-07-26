from kivy.app import App

from main_menu import MainMenu

class DienChanApp(App):
    def build(self):
        return MainMenu()

#MAIN
DienChanApp().run()

