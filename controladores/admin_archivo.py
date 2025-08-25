import os

class AdminArchivo:
    def __init__(self, archivo_seleccionado: str):
        self.nombre_archivo = archivo_seleccionado
        self.bytes_archivo = None

    def leer_bytes(self) -> bytes:
        with open(self.nombre_archivo, "rb") as f:
            self.bytes_archivo = f.read()
        return self.bytes_archivo

    def crear_archivo(self, ruta: str, contenido: bytes):
        with open(ruta, "wb") as f:
            f.write(contenido)
