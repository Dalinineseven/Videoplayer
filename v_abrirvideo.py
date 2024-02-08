from kivy.lang import Builder
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


class Reproductor (App):

    def build (self):
        Player= VideoPlayer(source= "VOCALE.mp4")        
        Player.state='play'
        Player.options={'eos': 'stop' }
        Player.allow_stretch=True
        return Player
    
Reproductor().run()
