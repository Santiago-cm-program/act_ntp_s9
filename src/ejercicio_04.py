""" Ejercicio 4: Filtros con Texto
Filtra usando métodos de string:

Empleados cuyos nombres empiezan con 'M'
Departamentos que contienen 'R'
Pista: Usa .str.startswith() y .str.contains() para filtros de texto. """

import pandas as pd
from data_frame_empleados import df

print("Empleados cuyos nombres empiezan con 'M':")
filtro_nombres_m = df[df['nombre'].str.startswith('M')]
print(filtro_nombres_m)

print("\nDepartamentos que contienen 'R':")
filtro_departamentos_r = df[df['departamento'].str.contains('R')]
print(filtro_departamentos_r)

