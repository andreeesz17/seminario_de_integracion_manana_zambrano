# primera-clase.py — Control de Puerto Marítimo

class Barco:
    # Atributo de clase — compartido por TODAS las instancias
    tipo_transporte = "Embarcación Marítima"

    # __init__ es el constructor — se ejecuta al crear la instancia
    def __init__(self, nombre, eslora):
        # Atributos de instancia — propios de cada objeto
        self.nombre = nombre
        self.eslora = eslora

    # Método de instancia — self es la referencia al objeto
    def reportar_estado(self):
        return f"Embarcación {self.nombre} con eslora de {self.eslora} metros lista para atracar."

    def actualizar_eslora(self):
        self.eslora += 1
        print(f"Eslora actualizada para {self.nombre}. Nueva eslora: {self.eslora} metros.")

    # __str__ — representación legible (para print y str())
    def __str__(self):
        return f"Barco({self.nombre}, {self.eslora}m)"

    # __repr__ — representación oficial (para depuración)
    def __repr__(self):
        return f"Barco(nombre={self.nombre!r}, eslora={self.eslora!r})"

# Crear instancias (objetos) con la clase como función
atlantic = Barco("Atlantic Star", 185)
pacific  = Barco("Pacific Queen", 210)

print(atlantic.reportar_estado())       # Embarcación Atlantic Star con eslora de 185 metros lista para atracar.
print(pacific.reportar_estado())        # Embarcación Pacific Queen con eslora de 210 metros lista para atracar.
atlantic.actualizar_eslora()            # Eslora actualizada para Atlantic Star. Nueva eslora: 186 metros.
print(str(atlantic))                    # Barco(Atlantic Star, 186)
print(repr(atlantic))                   # Barco(nombre='Atlantic Star', eslora=186)
print(Barco.tipo_transporte)            # Embarcación Marítima  — atributo de clase
