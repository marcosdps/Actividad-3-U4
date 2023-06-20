from objectEncoder import ObjectEncoder
from interfazVisual import Interfaz

if __name__ == "__main__":
    encoder = ObjectEncoder()
    diccionario = encoder.leerDatos()
    precioVenta = encoder.decodificador(diccionario)
    miApp = Interfaz(precioVenta)
    miApp.ejecutar()

