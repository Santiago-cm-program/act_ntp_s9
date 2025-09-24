""" Ejercicio 5: Combinando Filtros
Combina diferentes tipos de filtros:

Empleados de IT con más de 30 años Y salario mayor a 60,000
Empleados cuyo nombre empieza con 'L' O son de RRHH
Desafío: Combina operadores lógicos con filtros de texto y numéricos. """

import pandas as pd
from data_frame_empleados import df

print("Empleados de IT con más de 30 años Y salario mayor a 60,000:")
filtro_it_edad_salario = df[(df['departamento'] == 'IT') & (df['edad'] > 30) & (df['salario'] > 60000)]
print(filtro_it_edad_salario)

print("\nEmpleados cuyo nombre empieza con 'L' O son de RRHH:")
filtro_nombre_rrhh = df[(df['nombre'].str.startswith('L')) | (df['departamento'] == 'RRHH')]
print(filtro_nombre_rrhh)
