import pandas as pd


def centimetros_a_pulgadas(cm):
    return cm / 2.54


# Leer el archivo excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una nueva columna con las medidas en pulgadas

df["Pulgadas"] = df["Centimetros"].apply(centimetros_a_pulgadas)

df.to_excel("muebles_medidas_con_pulgadas.xlsx", index=False)

print("Archivo 'muebles_medidas_con_pulgadas.xlsx' creado con éxito.")
