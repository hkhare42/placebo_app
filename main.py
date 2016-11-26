from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

class MultiScreens(ScreenManager):
    """ Screen management class containing most of app. """
    pass

class PlaceboApp(App):
    """ Main app class. """
    
    def build(self):
        return MultiScreens()

if __name__ == '__main__':
    PlaceboApp().run()