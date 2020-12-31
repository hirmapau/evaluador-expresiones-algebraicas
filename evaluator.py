'''
  Este archivo contiene las funciones para evaluar una expresión algebráica
  previamente traducida a posfijo. También hay una función para pedirle la usuario
  los valores de las incógnitas.
'''

# Importar dependencias
from Stack import Stack, Node
from operators import OPERATORS
from helper import is_number

# Obtiene las incóngnitas que se deben pedir al usuario
def identify_variables(prefix_expression:str) -> [str]:
  variables = []

  for char in prefix_expression.split():
    if not (char in OPERATORS or char in '() ' or is_number(char) or char in variables):
      variables.append(char)
  
  return variables

# Le pide el valor de las incógnitas al usuario
def ask_for_variables(variables:[str]) -> dict:
  # Almacenar las variables que se pedirán
  variables_dict = {}

  for variable in variables:
    value = float(input('Ingresa el valor de {}: '.format(variable)))
    variables_dict[variable] = value
  
  return variables_dict
