print("Listas")
print("Crear listas de control portuario")
vacia=[]
print(vacia)
muelles=[1,2,3,4,5,6,7]
print(muelles)
barcos=["Atlantic Star", "Pacific Queen", "Caribbean Wind", "Poseidón III","Mar Azul","Océano Libre"]
print(barcos)
mixta=[1, "Terminal Norte", "muelle 3", True, None, 3.4]
print(mixta)
aninada=[1,[5,5,[6,4,4]],5,7]
print(aninada)
print("Acceder a elementos de la lista de barcos")
print(barcos[0])
print(barcos[-1])
print(barcos[1:3])
print(barcos[::-1])

print("CRUD en lista de contenedores")
contenedores=["CTN-001","CTN-002","CTN-003","CTN-004"]
#agregar
contenedores.append("CTN-005")
print(contenedores)
contenedores.insert(1, "CTN-006")
print(contenedores)
contenedores.extend(["CTN-007", "CTN-008"])
#modificar
contenedores[0]="CTN-009"
print(contenedores)
#eliminar elementos
contenedores.remove("CTN-004")
print(contenedores)
eliminado=contenedores.pop()
print(contenedores)
eliminado=contenedores.pop(0)
print(contenedores)
del contenedores[0]
print(contenedores)


print("Buscar valores en la lista de contenedores")
print("CTN-007" in contenedores)
print(contenedores.index("CTN-007"))
print(contenedores.count("CTN-007"))

print("Ordenar lista de muelles")
muelles_desordenados=[5,2,9,1,5,6,34,9,0,1,2]
print(muelles_desordenados)
muelles_desordenados.sort()
print(muelles_desordenados)
muelles_desordenados.sort(reverse=True)
print(muelles_desordenados)
ordenada=sorted(muelles_desordenados)
print(muelles_desordenados)
print(ordenada)
