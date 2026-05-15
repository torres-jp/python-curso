# Trabajando fechas y horas con python.
from datetime import datetime, timedelta
import locale

# 1° Obtener fecha y hora actual.
now = datetime.now()
print(now)

# 2° Crear una fecha y hora especifica.
specific_date = datetime(2027, 2, 14, 16, 30, 0)
print(f"Fecha especifica: {specific_date}")

# 3° Formatear Fechas
# metodo strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:
format_date = now.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# 4° Operaiones con fechas (sumas/restar dias , minutos , meses, años)
yesterday = datetime.now() - timedelta(days=1, hours=3)
print(f"Fecha de ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1, hours=5)
print(f"Fecha de mañana: {tomorrow}")

one_hour_later = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_later}")

# 5° Obtener componentes individuales de una fecha
year = now.year
mes = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(
    f"Año: {year}, Mes: {mes}, Día: {day}, Hora: {hour}, Minuto: {minute}, Segundo: {second}"
)

# 6° Calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2026, 11, 29)
difference = date2 - date1
print(f"Diferencia  {difference} días.")

# 7° Cambiar idiota de la fecha a español
language_date = now.strftime("%A/%B/%Y, %H:%M:%S")
print(f" Fecha por default {language_date}")
#### Cambiar el idioma a español
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
spanish_date = now.strftime("%A/%B/%Y, %H:%M:%S")
print(f"Fecha en español: {spanish_date}")
