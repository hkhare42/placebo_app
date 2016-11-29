from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import codecs

class MultiScreens(ScreenManager):
    """ Screen management class containing most of app. """
    # Picked from http://www.alexandrafranzen.com/2012/02/25/50-ways-to-say-youre-awesome/
    message_string = [line.strip() for line in codecs.open(
        'messages.txt', 'r', encoding='utf-8', errors='ignore')]

class PlaceboApp(App):
    """ Main app class. """
    
    def build(self):
        return MultiScreens()

if __name__ == '__main__':
    PlaceboApp().run()