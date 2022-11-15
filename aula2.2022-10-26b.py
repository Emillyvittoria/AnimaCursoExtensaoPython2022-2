#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é o bichão mesmo!"
nome= input("Qual o seu nome?")
nota=float(input("Digite sua nota:"))

if nota ==10:
  print(f"{nome}, você é o bichão mesmo!")
elif (nota>= 6 and nota<10):
    print(f"{nome}, bom trabalho!")
else:
  print("Burro, não tirou dez")
  