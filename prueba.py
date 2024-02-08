import tkinter as tk




ventana=tk.Tk()

barralateral= tk.Frame(ventana, bg="red")
barralateral.pack(side=tk.LEFT, fill="both", expand=True)

def abrirvideo ():
    from v_abrirvideo import Reproductor
    Reproductor()

boton=tk.Button(barralateral, text="Reproducir",command= abrirvideo)
boton.pack()



ventana.mainloop()

        