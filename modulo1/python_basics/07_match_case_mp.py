print("Match case")
comando=input("Comando de operación portuaria — atracar/zarpar/inspeccionar: ")
match comando:
    case "atracar":
        print("Embarcación atracando en muelle asignado")
    case "zarpar":
        print("Embarcación autorizada para zarpar")
    case "inspeccionar":
        print("Iniciando inspección aduanera de la embarcación")
    case _:
        print(f"Comando '{comando}' no reconocido por el sistema portuario")

print("Match condiciones")
numero=7
match numero:
    case n if n<0:
        print(f"{n} es negativo")
    case 0:
        print("Es cero")
    case n if n % 2 == 0:
        print(f"{n} es par")
    case n:
        print(f"{n} es positivo e impar")
