# Trabajando fechas y horas en python
import os
from datetime import datetime, timedelta
import locale

os.system("cls")

# 1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Obtener una hora y fecha especifica.
specific_date = datetime(2026, 11, 29, 00, 00)
print(f"Fecha especifica: {specific_date}")

# 3. Formatear fechas
# se usa el metodo strftime( formato )
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

formated_date = now.strftime("%A - %B - %Y %H:%M:%S")
print(f"Fecha formateada: {formated_date}")

# 4. Operaciones con fechas (sumar/restar dias, minutos , meses , horas)
yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

print(f"Fecha de ayer: {yesterday}")
print(f"Fecha de mañana: {tomorrow}")

one_hour_later = datetime.now() + timedelta(hours=1)
print(f"Fecha dentro de una hora: {one_hour_later}")

# 5. Obtener los componentes indivuales de una fecha
year = now.year
print(f"Año: {year}")
month = now.month
print(f"Mes: {month}")
day = now.day
print(f"Día: {day}")
hour = now.hour
print(f"Hora: {hour}")
minute = now.minute
print(f"Minuto: {minute}")
second = now.second
print(f"Segundo: {second}")


# 6. Calcular diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2026, 11, 29)
diff = date2 - date1
print(f"Diferencia: {diff.days} dias")
