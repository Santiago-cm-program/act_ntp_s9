""" Ejercicio 2: Operadores Lógicos (AND, OR, NOT)
Combina condiciones con operadores lógicos:

Empleados de IT Y salario mayor a 60,000
Empleados de Ventas O mayores de 40 años
Empleados que NO son de Marketing """
import pandas as pd
from data_frame_empleados import df
print("Empleados de TI Y con salario mayor a 60,000:")
filtro_salario_ti = df[(df['departamento'] == 'IT') & (df['salario'] > 60000)]
print(filtro_salario_ti)

print("\nEmpleados de Ventas O mayores de 40 años:")
print_ventas_edad = df[(df['departamento'] == 'Ventas') | (df['edad'] > 40)]
print(print_ventas_edad)

print("\nEmpleados que NO son de Marketing:")
filtro_no_marketing = df[(df['departamento'] != 'Marketing')]
print(filtro_no_marketing)
