# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def contar_as(texto):
  texto_minusculo = texto.lower()
  quantidade_as = texto_minusculo.count('a')

  if quantidade_as > 0:
    print(f"A letra 'a' aparece {quantidade_as} vezes no texto.")
  else:
    print("A letra 'a' não foi encontrada no texto.")

texto = input("Digite um texto: ")

contar_as(texto)