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
  imposto = preço_produto * 0.05
  return imposto

#Aqui é o uso... aqui é o imposto a calcular
preço= 299
imposto= calcular_imposto(preço)
print (imposto)