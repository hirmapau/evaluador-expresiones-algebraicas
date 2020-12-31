# Operadores permitidos
OPERATORS = [
  '^',
  '*',
  '/',
  '+',
  '-'
]

# Regresa la posición en la jerarquía de algún operador
def get_operator_weight(operator):
  if operator == '^': return 3
  elif operator == '*' or operator == '/': return 2
  elif operator == '+' or operator == '-': return 1
  else: return 0