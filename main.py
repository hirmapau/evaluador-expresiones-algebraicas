'''
  Archivo principal para el menú e interactuar con los otros paquetes
'''

# Importar dependencias
from operators import OPERATORS
from prefix import infix_to_prefix
from postfix import infix_to_postfix
from evaluator import identify_variables, ask_for_variables

# Pide un polinomio al usuario y limpia la entrada
def ask_for_polynomial():
  polynomial = input('Ingresa el polinomio: ')

  # Eliminar espacios innecesarios
  polynomial = polynomial.replace(' ', '')
  clear_polynomial = ''

  # Insertar espacios al rededor de los operadores y paréntesis
  for char in polynomial:
    if char in OPERATORS or char in '()':
      clear_polynomial += ' {} '.format(char)
    else:
      clear_polynomial += char

  return clear_polynomial

# Punto de entrada al programa
if __name__ == "__main__":
  # Obtener polinomio
  polynomial = ask_for_polynomial()
  prefix_expression = infix_to_prefix(polynomial)
  postfix_exp = infix_to_postfix(polynomial)
  
  # Identificar las incógnitas y pedírselas al usuario
  variables = ask_for_variables(identify_variables(prefix_expression))
  print(variables)