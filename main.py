from kivy.app import App
from kivy.config import Config

from main_menu import MainMenu

class DienChanApp(App):
    def build(self):
        Config.set('graphics','width','1000')
        Config.set('graphics','height','800')
        # Turn on in prod
        #Config.set('kivy','exit_on_escape','0')
        return MainMenu()

#MAIN
DienChanApp().run()

