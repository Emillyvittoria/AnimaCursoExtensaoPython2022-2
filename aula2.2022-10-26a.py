# Comando de input(): quero permitir que o usuário digite algo

nome=input("Digite o seu nome:")
# Pede a idade para o usuário "Qual a sua idade?"
idade= int(input("Qual a sua idade?"))

# Comando de saída... exibir na tela
print(f"Boa noite, seu nome é {nome}")
# Exibir "Sua idade é..."
print(f"A sua idade é {idade}")

#Mostrar o dobro da idade informada
dobro = idade * 2
print("O dobro da idade informada é {}". format(dobro))

# Estrutura condicional - o famoso "SE" (IF)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade>= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir.")
else:
  print("Você é jovem ainda...")

#E esse eu quisesse perguntar o gênero (M= Masculino e F= Feminino)  
#Mostre (... e você também precisa prestar serviço militar obrigatório.)
gênero=input("Informe o gênero M=Masculino, F=Feminino e O= Outros:")
if idade>=18 and gênero == "M":
  print("Você precisa prestar serviço militar obrigatório")



print("Vai ser executada do mesmo jeito.")
