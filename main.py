from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ScreenF(Screen):
    def press(self):
        self.manager.transition.direction = "down"
        self.manager.current = '2'

class ScreenS(Screen):
    def press(self):
        self.manager.transition.direction = "up"
        self.manager.current = '1'


class Project0App(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(ScreenF())
        sm.add_widget(ScreenS())

        return sm


app = Project0App()

app.run()