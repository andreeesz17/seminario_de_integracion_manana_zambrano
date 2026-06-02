# polimorfismo.py — Control de Puerto Marítimo

# POLIMORFISMO POR HERENCIA — override de métodos
class AlertaPortuaria:
    """Clase base abstracta para alertas del puerto."""
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje      = mensaje

    def enviar(self):
        raise NotImplementedError("Las subclases deben implementar enviar()")

    def __str__(self):
        return f"{self.__class__.__name__} → {self.destinatario}"

class AlertaEmail(AlertaPortuaria):
    def __init__(self, destinatario, mensaje, asunto="Sin asunto"):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        return f"📧 Email a {self.destinatario}: [{self.asunto}] {self.mensaje}"

class AlertaSMS(AlertaPortuaria):
    MAX_CHARS = 160

    def enviar(self):
        msg = self.mensaje[:self.MAX_CHARS]
        return f"📱 SMS a {self.destinatario}: {msg}"

class AlertaPush(AlertaPortuaria):
    def enviar(self):
        return f"🔔 Alerta Push a {self.destinatario}: {self.mensaje[:50]}..."

class AlertaRadio(AlertaPortuaria):
    def __init__(self, canal, mensaje):
        super().__init__(canal, mensaje)

    def enviar(self):
        return f"📻 Radio Canal #{self.destinatario}: {self.mensaje}"

# Polimorfismo en acción — misma función, distintos tipos
def notificar_operadores(alertas: list):
    for alerta in alertas:
        print(f"  {alerta.enviar()}")   # cada uno envía a su manera

avisos = [
    AlertaEmail("capitan@maersk.com",    "Su embarque fue despachado", "Embarque #CTN-2024"),
    AlertaSMS("600111222",               "Contenedor listo para retiro en Terminal Norte"),
    AlertaPush("dispositivo-operador",   "¡Nuevo barco ingresando al muelle 5!"),
    AlertaRadio("16-VHF",               "Barco EcoVessel I solicitando atraque — responder urgente"),
]

print("Enviando alertas portuarias:")
notificar_operadores(avisos)

# POLIMORFISMO DUCK TYPING — sin herencia
# "Si camina como un pato y grazna como un pato, es un pato"
class ManifiestoLocal:
    def leer(self):   return "manifiesto de carga desde servidor local"
    def escribir(self, datos): print(f"Guardando manifiesto en disco local: {datos[:30]}...")

class ManifiestoNube:
    def leer(self):   return "manifiesto de carga desde la nube"
    def escribir(self, datos): print(f"Subiendo manifiesto a la nube: {datos[:30]}...")

class ManifiestoBD:
    def leer(self):   return "manifiesto de carga desde base de datos"
    def escribir(self, datos): print(f"Insertando manifiesto en BD: {datos[:30]}...")

# Esta función funciona con CUALQUIER objeto que tenga leer() y escribir()
def procesar_manifiesto(manifiesto):
    contenido = manifiesto.leer()
    print(f"Procesando: {contenido}")
    manifiesto.escribir(f"resultado_{contenido}")

for manifiesto in [ManifiestoLocal(), ManifiestoNube(), ManifiestoBD()]:
    procesar_manifiesto(manifiesto)
