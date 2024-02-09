from kivy.lang import Builder
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.logger import Logger

class Modelo (GridLayout):
    def __init__(self, **kwargs):
        super(Modelo,self).__init__(**kwargs)

        Logger.info("CONSTRUYENDO INTERFAZ")

        self.cols=1

        self.add_widget(Label(text="VIDEO"))

        self.Player= VideoPlayer(source= "VOCALE.mp4")        
        self.Player.state='play'
        self.Player.options={'eos': 'stop' }
        self.Player.allow_stretch=True
        self.add_widget(self.Player)

        self.boton_c_v=Button(text="CERRAR")
        self.boton_c_v.bind(on_press=self.presionado)
        self.add_widget(self.boton_c_v)
    
    def presionado(self, instace):
        Logger.info("BOTON CERRAR VIDEO PRESIONADO")
        Logger.info(self.Player.state)
        if self.Player.state == 'play': 
            
            Logger.info("DETENIENDO VIDEO")
            self.Player.state='stop'
            Logger.info(self.Player.state)
            
            Logger.info("DETENIENDO APLICACION")
            Reproductor.on_stop(self)
            #Reproductor.get_running_app().stop()

            Logger.info("CERRANDO VENTANA")
            Window.close()
        else:
            pass

class Reproductor (App):

    Logger.info("INICIANDO CREACION VDPLAYER")

    def build (self):
        return Modelo()
    
Reproductor().run()