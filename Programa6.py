celsius = float(input("Ingresa los grados Celsius: "))

print("1. Fahrenheit")
print("2. Kelvin")

opcion = input("Selecciona una opción: ")

match opcion:
    case "1":
        fahrenheit = (celsius * 9/5) + 32
        print("Temperatura:", fahrenheit, "°F")
    case "2":
        kelvin = celsius + 273.15
        print("Temperatura:", kelvin, "K")
    case _:
        print("Opción inválida")
