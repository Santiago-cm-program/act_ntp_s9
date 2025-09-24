""" Ejercicio 3: Método isin()
Usa isin() para filtrar múltiples valores:

Empleados de IT o Ventas
Empleados con edad de 28, 35 o 42 años
Pista: El método isin() acepta una lista de valores para comparar. """

import pandas as pd
from data_frame_empleados import df

print("Empleados de IT o Ventas:")
filtro_departamentos = df[df['departamento'].isin(['IT', 'Ventas'])]
print(filtro_departamentos)

print("\nEmpleados con edad de 28, 35 o 42 años:")
filtro_edades = df[df['edad'].isin([28, 35, 42])]
print(filtro_edades)



