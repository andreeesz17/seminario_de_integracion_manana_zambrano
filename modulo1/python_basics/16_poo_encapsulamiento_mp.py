# encapsulamiento.py — Control de Puerto Marítimo

class CuentaNaviera:
    def __init__(self, naviera, saldo_inicial=0):
        self.naviera        = naviera
        self.__saldo        = saldo_inicial     # __ → privado (name mangling)
        self.__historial    = []
        self.__activa       = True
        self.__registrar(f"Cuenta naviera creada con {saldo_inicial}€")

    # Property — getter (acceso como atributo, no como método)
    @property
    def saldo(self):
        return self.__saldo

    @property
    def activa(self):
        return self.__activa

    @property
    def historial(self):
        return list(self.__historial)   # devuelve copia, no referencia

    # Método público — la "ventanilla portuaria"
    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo += cantidad
        self.__registrar(f"Depósito de tarifa portuaria: +{cantidad}€")
        return self

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__saldo:
            raise ValueError(f"Saldo insuficiente (disponible: {self.__saldo}€)")
        self.__saldo -= cantidad
        self.__registrar(f"Retiro por servicio portuario: -{cantidad}€")
        return self

    def transferir(self, destino, cantidad):
        self.retirar(cantidad)
        destino.depositar(cantidad)
        self.__registrar(f"Transferencia a naviera {destino.naviera}: -{cantidad}€")
        return self

    # Método privado — solo para uso interno
    def __registrar(self, operacion):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial.append(f"[{hora}] {operacion}")

    def __str__(self):
        return f"CuentaNaviera({self.naviera}: {self.__saldo}€)"

# Uso
c1 = CuentaNaviera("Maersk Line", 1000)
c2 = CuentaNaviera("MSC Shipping", 500)

c1.depositar(500).retirar(200)     # encadenamiento — depositar y retirar devuelven self
c1.transferir(c2, 300)

print(c1)    # CuentaNaviera(Maersk Line: 1000€)
print(c2)    # CuentaNaviera(MSC Shipping: 800€)
print(f"Saldo Maersk Line: {c1.saldo}€")   # acceso como atributo (property)

# c1.__saldo = 99999  # AttributeError — acceso directo denegado
# c1.saldo = 99999    # AttributeError — no hay setter

for entrada in c1.historial:
    print(f"  {entrada}")
