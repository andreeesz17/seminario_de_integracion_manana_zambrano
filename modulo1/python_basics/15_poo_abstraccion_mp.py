# abstraccion.py — Control de Puerto Marítimo
from abc import ABC, abstractmethod

# ABC (Abstract Base Class) — clase abstracta que no puede instanciarse
class ZonaPortuaria(ABC):
    def __init__(self, identificador="zona-general"):
        self.identificador = identificador

    # Método abstracto — CADA subclase DEBE implementarlo
    @abstractmethod
    def capacidad(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    # Método concreto — compartido por todas las zonas portuarias
    def describir(self) -> str:
        return (f"{self.__class__.__name__} [{self.identificador}]: "
                f"capacidad={self.capacidad():.2f} m², perímetro={self.perimetro():.2f} m")

# ZonaPortuaria()  # TypeError — no puede instanciarse

class PatioCircular(ZonaPortuaria):
    def __init__(self, radio, identificador="zona-general"):
        super().__init__(identificador)
        self.radio = radio

    def capacidad(self):
        import math
        return math.pi * self.radio ** 2

    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

class MuelleRectangular(ZonaPortuaria):
    def __init__(self, ancho, largo, identificador="zona-general"):
        super().__init__(identificador)
        self.ancho = ancho
        self.largo  = largo

    def capacidad(self):
        return self.ancho * self.largo

    def perimetro(self):
        return 2 * (self.ancho + self.largo)

class TerminalTriangular(ZonaPortuaria):
    def __init__(self, a, b, c, identificador="zona-general"):
        super().__init__(identificador)
        self.a, self.b, self.c = a, b, c

    def perimetro(self):
        return self.a + self.b + self.c

    def capacidad(self):
        s = self.perimetro() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

# Polimorfismo — mismo código para cualquier ZonaPortuaria
zonas = [PatioCircular(5, "Patio Sur"), MuelleRectangular(4, 6, "Muelle Norte"), TerminalTriangular(3, 4, 5, "Terminal Este")]

for zona in zonas:
    print(zona.describir())

capacidad_total = sum(z.capacidad() for z in zonas)
print(f"Capacidad total del puerto: {capacidad_total:.2f} m²")
