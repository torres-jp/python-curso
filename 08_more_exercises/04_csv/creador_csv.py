import pandas as pd

# DataFrame es la infoción que queremos guardar en el csv

data = {
    "Piezas": ["Pata", "Mesa", "Silla", "Tablero"],
    "Centimetros": [40, 120, 50, 80],
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_excel(
    "muebles_medidas.xlsx", index=False
)  # index=False para no guardar el índice del DataFrame en el archivo CSV
