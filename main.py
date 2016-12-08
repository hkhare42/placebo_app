from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import codecs
import requests
import random
from kivy.utils import get_color_from_hex
# from kivy.config import Config
# Config.set('graphics', 'width', '1080')
# Config.set('graphics', 'height', '1920')

class MultiScreens(ScreenManager):
    """ Screen management class containing most of app. """

    # Picked from http://www.alexandrafranzen.com/2012/02/25/50-ways-to-say-youre-awesome/
    message_dict = eval(codecs.open('messages.txt', 'r', 
        encoding='utf-8', errors='ignore').read())
    ranstr = random.choice(list(message_dict.keys()))

    def send_resp(self, response):
        ind = 1 if response == 'YES' else 0
        requests.post('http://ec2-35-154-66-204.ap-south-1.compute.amazonaws.com:8080/entry',
            data= {'user_id': self.ids.ti.text,
             'msg_id': self.ranstr, 'response': ind})
        self.current = 'home'
        self.transition = SlideTransition(
            direction=random.choice(['left','right','up','down'])
            )
        self.ranstr = random.choice(list(self.message_dict.keys()))
        self.ids.cl.set_canvas()

    def set_stage(self):
        self.ids.pm.disabled = False
        self.ids.pm.opacity = 1
        self.ids.al2.pos_hint = {'x': 0, 'top': 1.2}

class ColLayout(FloatLayout):
    def set_canvas(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        with self.canvas.before:
            Color(rgba= [random.random() for i in range(3)] + [0.3])
            Rectangle(pos=self.pos, size=self.size)
        for widget in saved:
            self.add_widget(widget)

class PlaceboApp(App):
    """ Main app class. """
    
    def build(self):
        return MultiScreens()

    def open_settings(*args):
        pass

if __name__ == '__main__':

    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex('#FFFFFF')

    PlaceboApp().run()