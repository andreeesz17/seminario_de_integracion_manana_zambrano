# Enteros, Cadena de caracteres, booleano, None
nombre_barco="Atlantic Cargo" # string
eslora=185          # int (metros)
calado=12.5         # float
operativo=True      # bool
nulo=None           # NoneType

print(type(nombre_barco))
print(type(eslora))
print(type(calado))
print(type(operativo))
print(type(nulo))

# Asignar valor varias variables en una línea
muelle_a, muelle_b, muelle_c = 12, 13, 14
print(muelle_a)
print(muelle_b)
print(muelle_c)

# Asignar el mismo valor a varias variables
muelle_a = muelle_b = muelle_c = 0
print(muelle_a)
print(muelle_b)
print(muelle_c)

#Intercambiar valores
contenedor_entrada, contenedor_salida = 10, 20
print(contenedor_entrada, contenedor_salida)
contenedor_entrada, contenedor_salida = contenedor_salida, contenedor_entrada
print(contenedor_entrada, contenedor_salida)

# Convenciones de nombres
nombre_naviera="Maersk Line"       # snake_case
nombreNaviera="Maersk Line"        # NO USAR camelCase
MAX_CONTENEDORES=3                 # MAYUSCULAS SOSTENIDAS para Constantes
_codigo_interno="privado"          # para uso interno

# Manejo de Enteros
capacidad_pequena = 42
capacidad_negativa = -17
capacidad_grande=1_000_000_000_000
capacidad_enorme= 2 ** 100

print(capacidad_pequena)
print(capacidad_negativa)
print(capacidad_grande)
print(capacidad_enorme)

# Bases Numéricas
binario=0b1010
octal=0o17
hexadecimal=0xFF
print(binario, octal, hexadecimal)
#convertir de decimal a otras bases
print(bin(255))
print(oct(255))
print(hex(255))
