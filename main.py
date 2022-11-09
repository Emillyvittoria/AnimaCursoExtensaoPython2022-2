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