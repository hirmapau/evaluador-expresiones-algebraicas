from Stack import Stack, Node
from helper import is_number
from characters import OPERATORS, get_operator_weight

def infix_to_postfix(algebraic_expression: str):
  result=''
  stacksito=Stack()
  for char in algebraic_expression:
    if char not in OPERATORS:
      result+=char
    elif char=='(':
      stacksito.push('(')
    elif char==')':
      while stacksito.is_empty() and stacksito.last() != '(':
        result+=stacksito.pop()
      stacksito.pop()
    else:
      while stacksito.is_empty() and stacksito.last()!='(' and get_operator_weight(char)<=get_operator_weight(stacksito.last()):
        result+=stacksito.pop()
      stacksito.append(char)
  while stacksito:
    result+=stacksito.pop()
  return result