pesos = float(input("Cantidad en pesos mexicanos: "))

print("USD")
print("EUR")
print("JPY")
print("KRW")
print("AUD")
print("PEN")
print("CAD")
print("VES")
print("ARS")

moneda = input("Moneda destino: ").upper()

match moneda:
    case "USD":
        print("Resultado:", round(pesos / 18.5, 2), "USD")
    case "EUR":
        print("Resultado:", round(pesos / 21.0, 2), "EUR")
    case "JPY":
        print("Resultado:", round(pesos * 8.3, 2), "JPY")
    case "KRW":
        print("Resultado:", round(pesos * 73, 2), "KRW")
    case "AUD":
        print("Resultado:", round(pesos / 12, 2), "AUD")
    case "PEN":
        print("Resultado:", round(pesos / 5, 2), "PEN")
    case "CAD":
        print("Resultado:", round(pesos / 13.5, 2), "CAD")
    case "VES":
        print("Resultado:", round(pesos * 2, 2), "VES")
    case "ARS":
        print("Resultado:", round(pesos * 65, 2), "ARS")
    case _:
        print("Moneda inválida")
