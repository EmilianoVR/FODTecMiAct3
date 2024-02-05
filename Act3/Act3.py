import os
import json

class ClienteManager:
    def __init__(self):
        self.clientes = {}

    def cargar_clientes(self):
        if os.path.exists("clientes.json"):
            with open("clientes.json", "r") as file:
                self.clientes = json.load(file)

    def guardar_clientes(self):
        with open("clientes.json", "w") as file:
            json.dump(self.clientes, file)

    def crear_cliente(self, nombre, descripcion):
        if nombre not in self.clientes:
            self.clientes[nombre] = {"descripcion": descripcion, "recurrente": False}
            self.guardar_clientes()
            return f"Nuevo cliente {nombre} creado con éxito."
        else:
            return f"Error: Cliente {nombre} ya existe."

    def actualizar_cliente(self, nombre, nueva_descripcion):
        if nombre in self.clientes:
            self.clientes[nombre]["descripcion"] = nueva_descripcion
            self.clientes[nombre]["recurrente"] = True
            self.guardar_clientes()
            return f"Cliente {nombre} actualizado con éxito."
        else:
            return f"Error: Cliente {nombre} no encontrado."

    def consultar_cliente(self, nombre):
        if nombre in self.clientes:
            return f"Información del cliente {nombre}: {self.clientes[nombre]}"
        else:
            return f"Error: Cliente {nombre} no encontrado."

# Ejemplo de uso
manager = ClienteManager()
manager.cargar_clientes()
print(manager.crear_cliente("NuevoCliente", "Descripción del nuevo cliente"))
print(manager.actualizar_cliente("ClienteExistente", "Nueva descripción para cliente existente"))
print(manager.consultar_cliente("NuevoCliente"))
print("Hola Diablo")
