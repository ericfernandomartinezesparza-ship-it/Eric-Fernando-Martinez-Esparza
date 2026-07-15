mes = input("Escribe un mes: ").lower()

match mes:
    case "diciembre" | "enero" | "febrero":
        print("Es Invierno")
    case "marzo" | "abril" | "mayo":
        print("Es Primavera")
    case "junio" | "julio" | "agosto":
        print("Es Verano")
    case "septiembre" | "octubre" | "noviembre":
        print("Es Otoño")
    case _:
        print("Mes inválido")
