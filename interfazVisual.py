from tkinter import *
from tkinter import ttk

class Interfaz:
    __precioVenta= None
    __ventana= None
    __cantDolares= None
    __precioFinal = None

    def __init__(self, precioVenta):
        self.__ventana = Tk()
        self.__ventana.geometry("230x100")
        self.__ventana.title("Conversor de Dolares a Pesos")
        self.__precioVenta = precioVenta
        self.frames()
        self.__cantDolares = StringVar()
        self.__precioFinal = DoubleVar()
        self.__cantDolares.trace("w", self.calculo)
        self.entrys()
        self.cantDolaresEntry.focus()
        self.labels()
        self.calculo()
        self.boton()

    def frames(self):
        self.mainframe = ttk.Frame(self.__ventana, borderwidth=2,relief="sunken")
        self.mainframe.grid()
        self.frameCotizacion = ttk.Frame(self.__ventana, borderwidth=2, relief= "solid")
        self.frameCotizacion.grid()
        self.__ventana.columnconfigure(0, weight=1)# mainframe
        self.__ventana.columnconfigure(1, weight=1)# frameCotizacion
    def ejecutar(self):
        self.__ventana.mainloop()

    def labels(self):
        #ttk.Label(self.mainframe, text=self.__precioVenta).grid()
        ttk.Label(self.mainframe, text=" dolares").grid(row=1, column=3)
        ttk.Label(self.mainframe, text=f"es equivalente a ").grid(row=2, column=1)
        ttk.Label(self.mainframe, text="pesos").grid(row=2, column=3)
        ttk.Label(self.mainframe, textvariable=self.__precioFinal).grid(row=2, column=2)
        ttk.Label(self.frameCotizacion, text="Cotizacion: ").grid(row=0, column=1)
        ttk.Label(self.frameCotizacion, text=self.__precioVenta).grid(row=0, column=2)
    
    def entrys(self):
        self.cantDolaresEntry = ttk.Entry(self.mainframe,textvariable=self.__cantDolares, width=8)
        self.cantDolaresEntry.grid(row=1, column=2)

    def calculo(self,*args):
        cantidad = self.cantDolaresEntry.get()
        if cantidad != "":
            self.__precioFinal.set(float(cantidad)*float(self.__precioVenta.replace(",", ".")))
            #como precioFinal es una variable de control(porque la asigno como DoubleVar() al comienzo)
            #entonces, para que se muestre en Label, textvariable reconoce el cambio de la misma
            #solo si se asigna con set
        else: self.__precioFinal.set(0)

    def boton(self):
        ttk.Button(self.mainframe,text="Salir", command=self.mainframe.quit).grid(row=3, column=3)






