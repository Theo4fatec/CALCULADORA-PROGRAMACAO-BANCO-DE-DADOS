def somar(a, b):
  return a + b

def subtrair(a, b):
  return somar(a, b * -1)

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  if b == 0:
    print("Não consegue dividir por 0 ")
    return None
  return a / b