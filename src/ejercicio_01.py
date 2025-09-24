""" Ejercicio 1: Filtros Básicos
Realiza estos filtros simples:

Empleados con salario mayor a 50,000
Empleados menores de 35 años
Empleados del departamento 'IT' """

import pandas as pd
from data_frame_empleados import df 

print("Empleados con salario mayor a 50,000:")
filtro_salario = df[df['salario']>50000]
print(filtro_salario)


print("\nEmpleados menores de 35 años:")
filtro_edad = df[df['edad']<35]
print(filtro_edad)

print("\nEmpleados del departamento 'IT':")
filtro_departamento = df[df['departamento']=='IT']
print(filtro_departamento)
