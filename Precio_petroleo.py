# Librerias 

import pandas as pd
import matplotlib.pyplot as plt


# Dirección del programa:

direccion = "C:\\Users\\Mishell Enriquez\\Documents\\Precio_petroleo"

# Lectura de los datos a analizar
datos=pd.read_excel("Datos_historicos_Futuros_petroleo_crudo_WTI.xlsx")
eje_horizontal = datos.iloc[0:522,1]
eje_vertical = datos.iloc[0:522,2]

# Gráfica 
plt.plot(eje_horizontal, eje_vertical,color="green")
plt.ylabel("Precio del petróleo crudo WTI")
plt.xlabel("Fecha [2012-2022]")
plt.title("Precio del pétroleo") 
plt.show()
