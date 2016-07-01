#kivy.config = window size
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '400')

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

class Controller(AnchorLayout):


    def add_time(self,btn):
        intervalcontainer = self.ids.intervalcontainer
        intervalcontainer.add_widget(Label(text=btn.text))

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        mincontainer = self.ids.mincontainer
        for i in range(0,60):
            mincontainer.add_widget(ScrollButton(text=str(i),font_size=24,background_color=[0,0,0,.1],on_press=self.add_time))

class ScrollButton(Button):
    pass

class RunApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    RunApp().run()



