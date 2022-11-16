#Criação de funções

preço= 1999.90

#Calcular 5% de imposto, guardar na variável imposto e exibir na tela
imposto= preço * 0.05
print(imposto)

preço2= 100
imposto2= preço2 * 0.05
print (imposto2)

#Criar uma função calcular_imposto () que calcular um imposto de 5% e retorna a quem pediu...
def calcular_imposto(preço_produto):
  imposto = preço_produto * 0.07
  return imposto

#Aqui é o uso... aqui é o imposto a calcular
preço= 299
imposto= calcular_imposto(preço)
print (f" Esse aqui é com a função (7%) {imposto}")

print(preço)
preço_produto= 100
print(preço_produto)


#Agora calcular imposto a alíquota agora é 7%

valores= [1.99, 24.50, 78.27, 1515.5]
#E se eu quiser calcular o imposto destea quatro valores e exibir na tela assim "O imposto de ... é.... (1º preço, 2º imposto)"
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto (valor)}")

#Declarar um função calcula_imposto_alíquota que recebe dois parâmetros: o preço do produto e a alíquota do imposto a ser aplicada e retorna o imposto calculado. Se a alíquota não for informada, utilize 7% como padrão.
def calcular_imposto_alíquota(valor,alíquota=7):
  imposto = valor * alíquota / 100
  return imposto

for valor in valores:
  print (f"O imposto de {valor} é {calcular_imposto_alíquota(valor)}")

for valor in valores:
  print (f"O imposto de {valor} é {calcular_imposto_alíquota(valor,7)}")

#E se o imposto for de 10%?
  
for valor in valores:
  print (f"O imposto de {valor} é {calcular_imposto_alíquota(valor,10)}")