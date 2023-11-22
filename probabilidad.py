import math

# Datos proporcionados
edades = [26, 28, 33, 34, 38, 40, 43, 43, 45, 47, 48, 49, 50, 55, 56]
probabilidad = 1 / 15  # Probabilidad para cada edad

# Calcular la media
media = sum(edades) / len(edades)

# Calcular la varianza
varianza = sum((x - media)**2 * probabilidad for x in edades)

# Calcular la desviación estándar
desviacion_estandar = math.sqrt(varianza)

# Resultados
print("Varianza: {:.2f}".format(varianza))
print("Desviación Estándar: {:.2f}".format(desviacion_estandar))
