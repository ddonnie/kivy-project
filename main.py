#kivy.config = window size
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '400')

from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel

class Controller(AnchorLayout):

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        carousel = self.ids.minutes
        for i in range(1,61):
            carousel.add_widget(Label(text=str(i),font_size=60))

    def set_interval(self):
        self.ids.intervalcontainer.add_widget(Label(text=str(self.ids.minutes.index+1)+' min'))
        self.ids.increment.dismiss()


    def remove_interval(self):
        if not self.ids.intervalcontainer.children==[]:
            for widget in self.ids.intervalcontainer.walk(restrict=True):
                lastWidget = widget
            self.ids.intervalcontainer.remove_widget(lastWidget)
        else: pass

class RunApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    RunApp().run()




