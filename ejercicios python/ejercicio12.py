calificacion = float(input("Ingresa una calificación (0-10): "))


if 0 <= calificacion <= 2:
    evaluacion = "Muy Malo"
elif 3 <= calificacion <= 4:
    evaluacion = "Malo"
elif 5 <= calificacion <= 6:
    evaluacion = "Regular"
elif 7 <= calificacion <= 8:
    evaluacion = "Muy Bueno"
elif 9 <= calificacion <= 10:
    evaluacion = "Excelente"
else:
    evaluacion = "Calificación fuera del rango permitido (0-10)"

print(f"Evaluación: {evaluacion}")