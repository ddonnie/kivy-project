#kivy.config = window size
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '270')
Config.set('graphics', 'height', '480')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from time import strftime

class Controller(FloatLayout):

    timer_started = False

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        for i in range(1,61):
            self.ids.intervalCarouselMinutes.add_widget(Label(text=str(i),font_size=120))
        for i in range(1,11):
            self.ids.intervalCarouselCycles.add_widget(Label(text=str(i),font_size=196))

    def set_interval(self):
        self.ids.intervalContainer.add_widget(Label(text=str(self.ids.intervalCarouselMinutes.index+1)+' min', size_hint =(1, .4), font_size=32))
        self.ids.increment.dismiss()


    def remove_interval(self):
        if not self.ids.intervalContainer.children==[]:
            for widget in self.ids.intervalContainer.walk(restrict=True):
                lastWidget = widget
            self.ids.intervalContainer.remove_widget(lastWidget)
        else: pass

    def start_stop(self):
        self.ids.play_pause.source = 'data/icons/ic_play_circle_outline_white_48dp.png' if self.timer_started else 'data/icons/ic_pause_circle_outline_white_48dp.png'
        self.timer_started = not self.timer_started

class RunApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    RunApp().run()






