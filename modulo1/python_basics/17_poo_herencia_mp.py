# herencia.py — Control de Puerto Marítimo

class Embarcacion:
    def __init__(self, nombre, naviera, año):
        self.nombre  = nombre
        self.naviera = naviera
        self.año     = año
        self._velocidad = 0    # _ → convención "protegido"

    def acelerar(self, incremento):
        self._velocidad += incremento
        return self

    def reducir_velocidad(self, decremento):
        self._velocidad = max(0, self._velocidad - decremento)
        return self

    def __str__(self):
        return f"{self.nombre} [{self.naviera}] ({self.año}) — {self._velocidad} nudos"

class BarcoCarga(Embarcacion):
    def __init__(self, nombre, naviera, año, capacidad_teus=1000):
        super().__init__(nombre, naviera, año)   # llama al constructor del padre
        self.capacidad_teus = capacidad_teus

    def emitir_señal(self):
        return f"{self.nombre} [{self.naviera}]: ¡Señal de entrada al puerto!"

    def __str__(self):
        return f"{super().__str__()} ({self.capacidad_teus} TEUs)"

class BarcoTanquero(Embarcacion):
    def __init__(self, nombre, naviera, año, capacidad_barriles):
        super().__init__(nombre, naviera, año)
        self.capacidad_barriles = capacidad_barriles

    def activar_protocolo_descarga(self):
        return f"🚢 {self.nombre} activa protocolo de descarga de hidrocarburos"

    def __str__(self):
        return f"{super().__str__()} ({self.capacidad_barriles} barriles)"

class BarcoCargaElectrico(BarcoCarga):
    def __init__(self, nombre, naviera, año, autonomia_km):
        super().__init__(nombre, naviera, año)
        self.__autonomia_km = autonomia_km
        self.__bateria      = 100

    def recargar(self, porcentaje=100):
        self.__bateria = min(100, self.__bateria + porcentaje)
        return self

    @property
    def autonomia_restante(self):
        return self.__autonomia_km * self.__bateria / 100

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Batería: {self.__bateria}% | "
                f"Autonomía: {self.autonomia_restante:.0f} km")

# Herencia — cada objeto es también de todos sus tipos padre
eco_vessel = BarcoCargaElectrico("EcoVessel I", "Green Shipping", 2024, 800)
eco_vessel.acelerar(18)
print(eco_vessel)

print(isinstance(eco_vessel, BarcoCargaElectrico))  # True
print(isinstance(eco_vessel, BarcoCarga))            # True — herencia
print(isinstance(eco_vessel, Embarcacion))           # True — herencia transitiva
print(isinstance(eco_vessel, BarcoTanquero))         # False

# MRO — Method Resolution Order
print(BarcoCargaElectrico.__mro__)
