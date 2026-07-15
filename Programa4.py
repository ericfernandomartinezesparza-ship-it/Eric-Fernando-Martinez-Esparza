precio = float(input("Ingresa el precio del producto: "))

if precio <= 100:
    descuento = 0.05
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.15
else:
    descuento = 0.20

total = precio - (precio * descuento)

print("Precio final:", round(total, 2))
