# tuplas.py — Control de Puerto Marítimo

# Crear tuplas
vacia      = ()
unitaria   = (42,)          # ← la coma es obligatoria para una tupla de un elemento
coordenada = (3, 4)
rgb        = (255, 128, 0)
embarque   = ("Atlantic Star", 185, "Terminal Norte")

# Tupla sin paréntesis — el empaquetado implícito
posicion_barco  = 10, 20             # también es una tupla
print(type(posicion_barco))          # <class 'tuple'>

# Acceso — igual que las listas
print(embarque[0])           # Atlantic Star
print(embarque[-1])          # Terminal Norte
print(embarque[1:])          # (185, 'Terminal Norte')

# Las tuplas son INMUTABLES
# embarque[0] = "Pacific Queen"       # TypeError — no se puede modificar

# Desempaquetado (unpacking)
nombre_barco, eslora, terminal = embarque
print(nombre_barco, eslora, terminal)  # Atlantic Star 185 Terminal Norte

# Desempaquetado con *
primero, *resto = (1, 2, 3, 4, 5)
print(primero)   # 1
print(resto)     # [2, 3, 4, 5]

*inicio, ultimo = (1, 2, 3, 4, 5)
print(inicio)    # [1, 2, 3, 4]
print(ultimo)    # 5

# Tuplas de retorno de funciones
def calcular_tarifa_embarque(toneladas, tarifa):
    if tarifa == 0:
        return None, "División por cero — tarifa inválida"
    return toneladas / tarifa, None

resultado, error = calcular_tarifa_embarque(10, 3)
if error:
    print(f"Error: {error}")
else:
    print(f"Tarifa por tonelada: {resultado:.4f}")

# Tuplas como claves de diccionario (las listas NO pueden ser claves)
posiciones_muelle = {(0, 0): "origen", (1, 0): "muelle norte", (0, 1): "muelle sur"}
print(posiciones_muelle[(0, 0)])   # origen

# Cuándo usar tuple vs list
# tuple → datos que no cambian: coordenadas GPS del puerto, datos de embarque, registros de BD
# list  → datos que se modifican: lista de barcos atracados, contenedores en patio, etc.
