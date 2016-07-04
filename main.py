#kivy.config = window size
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '270')
Config.set('graphics', 'height', '480')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class ScreenManagement(ScreenManager):
    pass

class IntervalScreen(Screen):

    def __init__(self, **kwargs):
        super(IntervalScreen, self).__init__(**kwargs)
        for i in range(1,61):
            self.ids.intervalCarouselMinutes.add_widget(Label(text=str(i),font_size=120))

    def set_interval(self):
        self.ids.intervalContainer.add_widget(Label(text=str(self.ids.intervalCarouselMinutes.index+1)+' min', size_hint =(1, .4), font_size=32))
        self.ids.increment.dismiss()

    def remove_interval(self):
        if not self.ids.intervalContainer.children==[]:
            for widget in self.ids.intervalContainer.walk(restrict=True):
                lastWidget = widget
            self.ids.intervalContainer.remove_widget(lastWidget)
        else: pass

    def reset_slides(self):
        self.ids.intervalCarouselMinutes.load_slide(self.ids.intervalCarouselMinutes.slides[0])

presentation = Builder.load_file("run.kv")

class CycleScreen(Screen):
    pass

class TimerScreen(Screen):
    pass

class RunApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    RunApp().run()







