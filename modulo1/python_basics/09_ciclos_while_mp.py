contador=1
while (contador<=5):
    print(f"Turno de inspección portuaria: {contador}")
    contador+=1

print("continue")
i=1
while(contador<=5):
    i+=1
    if i==3:
        continue
    print(f"Revisión de contenedor: {i}")

print("break")
i=1
while(contador<=5):
    i+=1
    if i==3:
        break
    print(f"Revisión de contenedor: {i}")

codigo_embarque=int(input("Ingrese el código de embarque (0 para salir): "))
while codigo_embarque!=0:
    print("Embarque registrado: ", codigo_embarque)
    codigo_embarque=int(input("Ingrese el código de embarque (0 para salir): "))

contador=1
while (contador<=5):
    print(f"Barco en muelle {contador}")
    contador+=1
else:
    print("Todos los barcos han sido registrados")

contador=1
while (contador<=5):
    print(f"Barco en muelle {contador}")
    contador+=1
    if contador==3:
        break
else:
    print("Todos los barcos han sido registrados")
