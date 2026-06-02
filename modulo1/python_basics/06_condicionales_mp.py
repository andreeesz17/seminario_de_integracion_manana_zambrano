print("Condicionales simples")
eslora=input("Ingrese la eslora del barco en metros: ")
if (int(eslora)>=100):
    print("Barco de gran calado — requiere muelle especializado")

print("Condicionales dos caminos")
carga_peligrosa=input("Ingrese el nivel de riesgo de la carga (0-100): ")
if (int(carga_peligrosa)>=70):
    print("Carga peligrosa — se requiere protocolo de seguridad especial")
else:
    print("Carga estándar — puede ingresar al puerto")

print("Condicionales if anidados")
tiene_permiso=True
fondos=25
tipo_carga="contenedor"
if (tiene_permiso):
    if (fondos>=20):
        if tipo_carga=="contenedor":
            print("Contenedor autorizado. Tarifa: $20. Embarque confirmado")
        else:
            print("Tipo de carga disponible para ingreso")
    else:
        print("Fondos insuficientes para el atraque")
else:
    print("Embarcación sin permiso de ingreso al puerto")
