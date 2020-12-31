# Indica si un string es en realidad un número
def is_number(string):
  try:
    float(string)
    return True
  except:
    return False