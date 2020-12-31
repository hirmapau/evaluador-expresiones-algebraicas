# Importar dependencias
from Stack import Stack
from operators import OPERATORS, get_operator_weight

# Traduce una expresión de infijo a prefijo
def infix_to_prefix(infix_expression: str):
  # Invertir la expresión
  reversed_expression = []

  for character in infix_expression[::-1].split():
    # Reemplazar paréntesis
    if character == '(':
      reversed_expression.append(')')
    elif character == ')':
      reversed_expression.append('(')
    else:
      reversed_expression.append(character)
  
  # Crear Stack para la expresión
  expression_stack = Stack()
  expression_stack.push('(')

  # Expresión
  result_expression_list = []

  # Separar la expresión
  characters = reversed_expression + [')']

  # Iterar por los caracteres
  for character in characters:
    # Verificar el tipo de caracter
    if character == '(':
      expression_stack.push(character)
    elif character in OPERATORS:
      # Obtener valor en la jerarquía del operador
      operator_value = get_operator_weight(character)

      # Sacar elementos del Stack
      while not expression_stack.is_empty() and get_operator_weight(expression_stack.last().data) >= operator_value:
        result_expression_list.append(expression_stack.pop().data)
      
      # Añadir operador al Stack
      expression_stack.push(character)
    elif character == ')':
      while expression_stack.last().data != '(':
        result_expression_list.append(expression_stack.pop().data)
      
      # Eliminar paréntesis
      expression_stack.pop()
    else:
      result_expression_list.append(character)

  return ' '.join(result_expression_list)[::-1]