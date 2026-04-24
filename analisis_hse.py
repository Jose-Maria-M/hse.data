import pandas as pd

df = pd.read_excel("hse_data.xlsx")

print(df.head())

print("\nAREAS:")
print(df["Area"].unique())

print("\nTIPOS DE INCIDENTE:")
print(df["Tipo_Incidente"].unique())

#En que area hay mas accidentes: 

incidentes_area = df["Area"].value_counts()

print("\nINCIDENTES POR AREA:")
print(incidentes_area)

#Analisis de severidad;
severidad = df["Severidad"].value_counts()

print("\nSEVERIDAD:")
print(severidad)

#Grafica de inccidentes por area;
import matplotlib.pyplot as plt

incidentes_area.plot(kind="bar")
plt.title("Incidentes por Área")
plt.xlabel("Área")
plt.ylabel("Cantidad")
plt.savefig("incidentes_area.png")