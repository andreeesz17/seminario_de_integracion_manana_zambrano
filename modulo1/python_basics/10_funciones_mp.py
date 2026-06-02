print('Funciones del Sistema de Puerto Marítimo')
print('Función básica')

def bienvenida_puerto():
    print('Bienvenido al Sistema de Control Portuario')

bienvenida_puerto()


print('Función con parámetros')
def registrar_barco(nombre_barco):
    print(f'Barco registrado: {nombre_barco} — ingreso autorizado al puerto')

registrar_barco('Atlantic Cargo')

print('Función que devuelve valor con return')
def calcular_tarifa(toneladas, tarifa_por_tonelada):
    return toneladas * tarifa_por_tonelada

print(calcular_tarifa(5,6))

print('Función con valor por posición')
def registrar_embarque(naviera, muelle, terminal):
    print(f'{naviera},{muelle}, {terminal}')
registrar_embarque('Maersk', 'Muelle 3', 'Terminal Norte')  #por posicion
registrar_embarque(terminal='Terminal Sur', naviera='MSC', muelle='Muelle 7') #por nombre

print('Función con valor por defecto')
def saludo_operador(nombre, saludo="Bienvenido", puntuacion="f"):
    print(f'{saludo}, {nombre} {puntuacion}')
saludo_operador('Operador Zambrano', "Buenos días", "...")  #por posicion
saludo_operador("Operador García", puntuacion="...")
saludo_operador("Operador Pérez", "Buenas tardes")



print('Función parámetros posicionales')
def calcular_carga_total(*args):
    print(f"Cargas recibidas (toneladas): {args}")
    return sum(args)

print(calcular_carga_total(1,2,3))
print(calcular_carga_total(1,2,3,4,5,6,7))
print(calcular_carga_total(10,20,22))


print('Función parámetros combinados con posicional')
def mostrar_manifiesto(terminal,*contenedores):
    print(f"Terminal: {terminal}, Contenedores: {contenedores}")
    print(terminal)
    for contenedor in contenedores:
        print(f"  - {contenedor}")

mostrar_manifiesto("Terminal Norte","CTN-001", "CTN-002", "CTN-003", "CTN-004")

print('Función parámetros con clave valor variables')
def registrar_naviera(**kwargs):
    print(f"Datos de naviera recibidos: {kwargs}")
    for clave,valor in kwargs.items():
        print(f" {clave}: {valor}")

registrar_naviera(nombre="Maersk Line", pais="Dinamarca", flota=700, sede="Copenhague")


print("Función parámetros combinación de todos los tipos")
def configurar_terminal(host, *muelles, debug=False, **opciones):
    print(f"Host: {host}")
    print(f"Muelles: {muelles}")
    print(f"Debug: {debug}")
    print(f"Opciones: {opciones}")

configurar_terminal("puerto-server", 80, 443, 8080, debug=True, timeout=30, ssl=True)

print("Devolver múltiples valores")
def minmax(numeros):
    return min(numeros), max(numeros)

minimo, maximo = minmax([3,5,7,2,8,9])
print(f"Carga máxima: {maximo} ton, carga mínima: {minimo} ton")
_, maximo = minmax([12,13,16,24,100])
print(f"Solo carga máxima {maximo} ton")


print("Devolver un diccionario en el caso de muchos valores")
def analizar_carga(toneladas):
    total = sum(toneladas)
    n=len(toneladas)

    return {
        "total": total,
        "media": total/n if n >0 else 0,
        "minimo": min(toneladas) if toneladas else None,
        "maximo": max(toneladas) if toneladas else None,
        "count": n
    }
datos = [12,88,44,55,23,45]
stats = analizar_carga(datos)
print(f"Total de carga: {stats['total']} ton")
print(f"Promedio de carga: {stats['media']:.2f} ton")
print(f"Rango de carga: {stats['minimo'] - stats['maximo']} ton")

print("Funciones lambda")

def calcular_flete(x):
    return x*2
calcular_flete_lambda=lambda x: x*2
print(calcular_flete(2))
print(calcular_flete_lambda(2))

tarifa_total=lambda a,b: a+b
print(tarifa_total(5,4))
