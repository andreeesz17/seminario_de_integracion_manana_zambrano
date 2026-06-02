# diccionarios.py — Control de Puerto Marítimo

# Crear diccionarios
vacio    = {}
barco    = {"nombre": "Atlantic Star", "eslora": 185, "terminal": "Terminal Norte"}
config   = dict(host="puerto-server", puerto=5432, debug=True)

# Acceso
print(barco["nombre"])              # Atlantic Star
print(barco.get("naviera"))         # None — no lanza error si no existe
print(barco.get("naviera", "N/A"))  # N/A — valor por defecto

# Modificar
barco["naviera"]  = "Maersk Line"   # añadir/modificar
barco["eslora"]   = 190             # modificar
del barco["terminal"]               # eliminar
valor = barco.pop("naviera")        # eliminar y obtener el valor
print(barco)

# Verificar existencia
print("nombre" in barco)            # True
print("terminal" in barco)          # False

# Métodos esenciales
print(barco.keys())    # dict_keys(['nombre', 'eslora'])
print(barco.values())  # dict_values(['Atlantic Star', 190])
print(barco.items())   # dict_items([('nombre', 'Atlantic Star'), ('eslora', 190)])

# Iterar
for clave, valor in barco.items():
    print(f"  {clave}: {valor}")

# update — fusionar diccionarios
barco.update({"terminal": "Terminal Sur", "codigo_imo": "9876543"})
print(barco)

# Fusionar con | (Python 3.9+)
extra  = {"tipo_carga": "contenedor", "operativo": True}
completo = barco | extra
print(completo)

# Diccionarios anidados
puerto = {
    "nombre": "Puerto Marítimo Central",
    "operadores": {
        1: {"nombre": "Ana García", "turno": "mañana"},
        2: {"nombre": "Luis Pérez", "turno": "tarde"},
    },
    "terminales": ["Terminal Norte", "Terminal Sur"]
}

print(puerto["operadores"][1]["nombre"])   # Ana García
puerto["operadores"][3] = {"nombre": "Marta Ruiz", "turno": "noche"}

# setdefault — añadir solo si no existe
barco.setdefault("pais_bandera", "Panamá")   # añade "pais_bandera"
barco.setdefault("nombre", "Otro")           # no modifica — ya existe
