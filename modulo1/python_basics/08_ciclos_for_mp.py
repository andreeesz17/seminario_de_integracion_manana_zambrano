print("Ciclo for")
muelles=["Muelle A","Muelle B","Muelle C","Muelle D",]
for muelle in muelles:
    print(muelle)
print("Recorrer código de terminal")
for letra in "PUERTO":
    print(letra)

print("Recorrer rango")
for i in range(1,10,2):
    print(i)

print("Enumerar lista de muelles")
for i in enumerate(muelles):
    print(i)

print("Dos listas a la vez")
barcos=["Atlantic Star","Pacific Queen","Caribbean Wind",]
esloras=[185,220]
for barco,eslora in zip(barcos,esloras):
    print(barco,eslora)

print("Control del Ciclo")
print("Break")
for i in range(5):
    if i==6:
        break
    print(i)
print("Continue")
for i in range(5):
    if i==2:
        continue
    print(i)

print("For anidado")
for i in range(3):
    for j in range(2):
        print(i,j)
print("Lista comprehension forma corta")
capacidades=[x**2 for x in range(5)]
print(capacidades)
