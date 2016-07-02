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
from kivy.uix.carousel import Carousel

class Controller(AnchorLayout):



    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        carousel = self.ids.minutes
        for i in range(0,60):
            carousel.add_widget(Label(text=str(i),font_name='Roboto',font_size=60))

    def set_min(self):
        intervalcontainer = self.ids.intervalcontainer
        intervalcontainer.add_widget(Label(text=str(self.ids.minutes.index)))
        self.ids.increment.dismiss()



class RunApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    RunApp().run()




