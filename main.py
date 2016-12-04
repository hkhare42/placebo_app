from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import codecs
import requests

class MultiScreens(ScreenManager):
    """ Screen management class containing most of app. """
    # Picked from http://www.alexandrafranzen.com/2012/02/25/50-ways-to-say-youre-awesome/
    message_string = [line.strip() for line in codecs.open(
        'messages.txt', 'r', encoding='utf-8', errors='ignore')]

    def send_resp(self, response):
        ind = 1 if response == 'YES' else 0
        requests.post('http://127.0.0.1:5000/entry',
            data= {'user_id': 0, 'msg_id': 0, 'response': ind})
        self.current = 'home'

class PlaceboApp(App):
    """ Main app class. """
    
    def build(self):
        return MultiScreens()

    def open_settings(*args):
        pass

if __name__ == '__main__':
    PlaceboApp().run()