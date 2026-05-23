# 1. Introduccion a las clases en python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase. Las clases pueden tener atributos (variables) y métodos (funciones).
# Nos permiten organizar el código de manera más eficiente y reutilizable.


# Ejemplo basico de una clase en Python
class Auto:
    # atributo de clase (comparte todas las instancias)
    tipo = "Vehículo de cuatro ruedas"

    # metodo especial que es el que construye el objeto, se llama cada vez que se crea una instancia de la clase
    # al llamar a la clase con new
    # se llama automaticamente ese metodo cuando creas la instancia de la clase
    def __init__(self, marca, modelo, color):  # self se refiere a si mismo
        # Atributos de instancia (cada instancia tiene sus propios atributos)
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} ha arrancado.")


mi_auto = Auto("Totyota", "Corolla", "Rojo")
mi_auto.arrancar()

otro_auto = Auto("Ford", "Fiesta", "Blanco")
otro_auto.arrancar()


# Encapsulamiento: Es el concepto de ocultar los detalles internos de una clase y solo exponer lo necesario a través de métodos públicos. Esto ayuda a proteger los datos y a mantener la integridad del objeto.

OPENAI_KEY = ""

import requests


# Crear una clase para llamar un api
class API:
    def __init__(self, url, model, api_key):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        data = {"model": self.model, "messages": [{"role": "user", "content": prompt}]}

        response = requests.post(self.url, json=data, headers=headers)
        res_json = response.json()
        print(res_json["choices"][0]["message"]["content"])


openai_api = API(
    OPENAI_KEY, "gpt-3.5-turbo", "https://api.openai.com/v1/chat/completions"
)

openai_api.call("¿Cuál es la capital de Francia?")
