import requests

class ObjectEncoder:

    def leerDatos(self):
        response = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        if response.status_code == 200:
            diccionario = response.json()
            return diccionario
        else: print("Solicitud de datos no procesada")
            

    def decodificador(self, diccionario):
        for datos in diccionario:
            casa = datos["casa"]["nombre"]
            if casa == "Blue":
                precioVenta = datos["casa"]["venta"]
                return precioVenta
