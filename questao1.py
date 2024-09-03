# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
# escreva um programa na linguagem que desejar onde
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def pertence_fibonacci(numero):
  sequencia_1, sequencia_2 = 0, 1
  while sequencia_2 <= numero:
    if sequencia_2 == numero:
      return True
    sequencia_1, sequencia_2 = sequencia_2, sequencia_1 + sequencia_2
  return False

num = int(input("Digite um número: "))

if pertence_fibonacci(num):
  print(f"O número {num} pertence à sequência de Fibonacci.")
else:
  print(f"O número {num} não pertence à sequência de Fibonacci.")