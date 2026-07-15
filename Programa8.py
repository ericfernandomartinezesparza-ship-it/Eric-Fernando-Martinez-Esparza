print("1. Artista")
print("2. Película")
print("3. Serie")
print("4. Videojuego")
print("5. Libro")

opcion = input("Selecciona una opción: ")

match opcion:
    case "1":
        print("Artista: Bad Bunny. Cantante puertorriqueño de música urbana.")
    case "2":
        print("Película: Avatar. Ciencia ficción dirigida por James Cameron.")
    case "3":
        print("Serie: Breaking Bad. Trata sobre un profesor de química que fabrica metanfetamina.")
    case "4":
        print("Videojuego: Minecraft. Juego de construcción y supervivencia.")
    case "5":
        print("Libro: El Principito. Obra escrita por Antoine de Saint-Exupéry.")
    case _:
        print("Opción inválida.")
