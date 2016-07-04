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
import time

class Controller(FloatLayout):

    timer_interval = False
    timer_started_seconds = 0
    whole_time = 0
    time_summary = []

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 0)
        for i in range(1,61):
            self.ids.intervalCarouselMinutes.add_widget(Label(text=str(i),font_size=120))
        for i in range(1,11):
            self.ids.intervalCarouselCycles.add_widget(Label(text=str(i),font_size=144))

    def set_interval(self):
        self.ids.intervalContainer.add_widget(Label(text=str(self.ids.intervalCarouselMinutes.index+1), size_hint =(1, .4), font_size=32))
        self.ids.increment.dismiss()


    def remove_interval(self):
        if not self.ids.intervalContainer.children==[]:
            for interval in self.ids.intervalContainer.walk(restrict=True):
                lastInterval = interval
            self.ids.intervalContainer.remove_widget(lastInterval)
        else: pass

    def start_stop(self):
        self.ids.play_pause.source = 'data/icons/ic_play_circle_outline_white_48dp.png' if self.timer_interval else 'data/icons/ic_pause_circle_outline_white_48dp.png'
        self.timer_interval = not self.timer_interval
        if self.timer_interval: print('Timer Started')

    def run_summary(self):
        self.time_summary = []
        self.ids._screen_manager.current = 'RunScreen'
        cycle_number = self.ids.intervalCarouselCycles.current_slide.text
        for i in range(int(cycle_number)):
            for interval in self.ids.intervalContainer.walk(restrict=True):
                if not interval == self.ids.intervalContainer:
                    self.time_summary.append(int(interval.text))
                else: pass
        print(self.time_summary)


    def update(self, nap):
        if self.timer_interval:
            self.timer_started_seconds += nap
            self.whole_time +=nap
        m, s = divmod(self.timer_started_seconds, 60)
        self.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
                                        (int(m), int(s), int(s * 100 % 100)))
        mi,si = divmod(self.whole_time, 60)
        self.ids.allwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
                                        (int(mi), int(si), int(si * 100 % 100)))

        ######################Array of Interval Checks#############################
        if self.time_summary != []:
            if int(s) == self.time_summary[0]:
                self.time_summary.remove(int(s))
                self.timer_started_seconds = 0
                print(self.time_summary)
        else:
            self.ids.play_pause.source = 'data/icons/ic_play_circle_outline_white_48dp.png'
            self.timer_interval = False
            self.timer_started_seconds = 0
            self.whole_time = 0








class RunApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    RunApp().run()






