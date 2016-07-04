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
    timer_seconds = 0
    global_timer_seconds = 0
    timer_stop = 0
    curr_interval = 0
    number_of_intervals = 0
    event = 0
    #Clock.schedule_once(dummy_callback, 0)
    #def dummy_callback(dt):
    #    pass

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        for i in range(1,61):
            self.ids.intervalCarouselMinutes.add_widget(Label(text=str(i),font_size=120))
        for i in range(1,11):
            self.ids.intervalCarouselCycles.add_widget(Label(text=str(i),font_size=196))
        #self.ids.intervalContainerRun.add_widget(Label(text='next intervals:', size_hint =(1, .4), font_size=20))

        #Clock.schedule_interval(self.update, 0)

    def set_interval(self):
        minutes = self.ids.intervalCarouselMinutes.index+1
        self.ids.intervalContainer.add_widget(Label(text=str(minutes), size_hint =(1, .4), font_size=32))
        if minutes < 10:
            self.ids.intervalContainerRun.add_widget(Label(text='00:0'+str(minutes)+':00', size_hint =(1, .4), font_size=20))
        else:
            self.ids.intervalContainerRun.add_widget(Label(text='00:'+str(minutes)+':00', size_hint =(1, .4), font_size=20))
        self.ids.increment.dismiss()

    def remove_interval(self):
        if not self.ids.intervalContainer.children==[]:
            for widget in self.ids.intervalContainer.walk(restrict=True):
                lastWidget = widget
            self.ids.intervalContainer.remove_widget(lastWidget)
            for widget in self.ids.intervalContainerRun.walk(restrict=True):
                lastWidgetRun = widget
            self.ids.intervalContainerRun.remove_widget(lastWidgetRun)
        else: pass

    def start_stop(self):
        self.ids.play_pause.source = 'data/icons/ic_play_circle_outline_white_48dp.png' if self.timer_started else 'data/icons/ic_pause_circle_outline_white_48dp.png'
        self.timer_started = not self.timer_started

        if self.timer_started:
            if self.curr_interval == 0:
            #we are hitting play for the 1st time
                self.number_of_intervals = len(self.ids.intervalContainer.children)
                if not self.number_of_intervals == 0:
                #intervals are stored as minutes backwards
                    self.event = Clock.schedule_interval(self.update, 0)
                    self.curr_interval = 1
                    self.stop = int(self.ids.intervalContainer.children[self.number_of_intervals - self.curr_interval].text) #*60

                    self.timer_seconds = self.stop
                    m, s = divmod(self.timer_seconds, 60)
                    h, m = divmod(m, 60)
                    self.ids.stopwatch.text = ('[size=20]%02d:%02d:[/size][size=40]%02d[/size][size=20].%02d[/size]' %
                                        (int(h), int(m), int(s), int(s * 100 % 100)))



                    #delete intervals as they are starting
                    i = 1
                    for widget in self.ids.intervalContainerRun.walk(restrict=True):
                        if i<3:
                            i += 1
                            firstWidgetRun = widget
                        else:
                            break
                    self.ids.intervalContainerRun.remove_widget(firstWidgetRun)
            else:
                self.event = Clock.schedule_interval(self.update, 0)
        else:
            Clock.unschedule(self.event)

    def update(self, nap):
        if self.timer_started:
            if self.timer_seconds > 0:
                self.timer_seconds -= nap
                self.global_timer_seconds += nap
            elif not self.curr_interval == self.number_of_intervals:
                self.curr_interval = self.curr_interval +1

                self.timer_stop = self.get_next_interval()
                #self.timer_seconds = 0
                self.timer_seconds = self.stop
                m, s = divmod(self.timer_seconds, 60)
                h, m = divmod(m, 60)
                self.ids.stopwatch.text = ('[size=20]%02d:%02d:[/size][size=40]%02d[/size][size=20].%02d[/size]' %
                                    (int(h), int(m), int(s), int(s * 100 % 100)))
                #delete intervals as they are starting
                i = 1
                for widget in self.ids.intervalContainerRun.walk(restrict=True):
                    if i<3:
                        i += 1
                        firstWidgetRun = widget
                    else:
                        break
                self.ids.intervalContainerRun.remove_widget(firstWidgetRun)
            else:
                self.ids.stopwatch.text = ('[size=20]00:00:[/size][size=40]00[/size][size=20].00[/size]')


        global_m, global_s = divmod(self.global_timer_seconds, 60)
        global_h, global_m = divmod(global_m, 60)
        self.ids.global_stopwatch.text = ('%02d:%02d:[size=40]%02d[/size].%02d' %
                                        (int(global_h), int(global_m), int(global_s), int(global_s * 100 % 100)))

        m, s = divmod(self.timer_seconds, 60)
        h, m = divmod(m, 60)
        self.ids.stopwatch.text = ('[size=20]%02d:%02d:[/size][size=40]%02d[/size][size=20].%02d[/size]' %
                                        (int(h), int(m), int(s), int(s * 100 % 100)))

    def get_next_interval(self):
        self.stop = int(self.ids.intervalContainer.children[self.number_of_intervals - self.curr_interval].text) #*60

class RunApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    RunApp().run()






