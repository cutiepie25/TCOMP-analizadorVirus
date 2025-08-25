class Analizador:
    def __init__(self, bytes_archivo: bytes):
        self.bytes_archivo = bytes_archivo

        self.virus_patterns = {
            "Usama": [15, 30, 15, 49],
            "Amtrax": [72, 72, 15, 29],
            "ÉBola": [29, 32, 53, 29],
            "Ah1N1": [72, 32, 32, 20],
            "Covid19": [30, 25, 20, 19],
        }

    def analizar(self):
        datos = list(self.bytes_archivo)
        for nombre, patron in self.virus_patterns.items():
            encontrado, estado = self._contiene_secuencia(datos, patron)
            if encontrado:
                return nombre, estado
        return None, 0  # No encontrado, estado q0

    def _contiene_secuencia(self, datos: list[int], patron: list[int]) -> tuple[bool, int]:
        estado = 0
        for b in datos:
            if b == patron[estado]:
                estado += 1
                if estado == len(patron):
                    return True, estado  # estado final = q4
            else:
                estado = 1 if b == patron[0] else 0
        return False, estado