parciales = float(input("Promedio de parciales: "))
proyecto = float(input("Calificación del proyecto: "))
examen = float(input("Calificación del examen: "))

final = parciales * 0.40 + proyecto * 0.30 + examen * 0.30

print("Calificación final:", round(final,2))
