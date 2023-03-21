from variables import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
#import json
#from os import path, sep

"""PATH = path.dirname(__file__) + sep

with open(PATH+'language.json', 'r') as lang_json:
    languages = json.load(lang_json)

print(languages['uk'])"""



class ScreenF(Screen):
    def enter(self):
        self.manager.transition.direction = "up"
        self.manager.current = '2'

class ScreenS(Screen):
    def enter(self):
        self.manager.transition.direction = "down"
        self.manager.current = '1'
    ww = Window.width
    wh = Window.height


class Project0App(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenF())
        sm.add_widget(ScreenS())

        return sm


app = Project0App()

app.run()
