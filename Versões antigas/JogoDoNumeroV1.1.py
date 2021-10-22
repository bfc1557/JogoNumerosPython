#Jogo : Adivinha o número
#Jogo feito por bfc

#Importar da biblioteca "random" o "randint"
from random import randint

#Variaveis e gerador do número
NumeroFacil = randint(1,10)
NumeroMedio = randint(1,100)
NumeroExtremo = randint(1,1000)
Tentativas = 1
Dificuldade = 0

#Inicio
print("  »»————-　★　————-««")
print("ADIVINHA O NÚMERO by bfc")
print("  »»————-　★　————-««\n")
print("Para jogar escolha a dificuldade inserindo um número.")
print("1-Fácil │ 2-Medio │ 3-Extremo │ 4-Impossivel")
Dificuldade = int(input())

#Dificuldade Facil 
if Dificuldade == 1:
  print("\n!O número está entre 1 a 10!")
  Tentativa = int(input("Tentativa: "))
  while Tentativa != NumeroFacil and Tentativa != 0:
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    if Tentativa < NumeroFacil :
     print(Tentativa, " é MENOR do que o número a ser adivinhado.")
    else:
     print(Tentativa, " é MAIOR do que o número a ser adivinhado.")
    Tentativa = int(input("\nTentativa: "))
  if Tentativa == NumeroFacil:
    print("\n\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0
  else: 
    print("O número era", NumeroFacil)

#Dificuldade Media
if Dificuldade == 2:
  print("\n!O número está entre 1 a 100!")
  Tentativa = int(input("Tentativa: "))
  while Tentativa != NumeroMedio and Tentativa != 0:
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    if Tentativa < NumeroMedio :
     print(Tentativa, " é MENOR do que o número a ser adivinhado.")
    else:
     print(Tentativa, " é MAIOR do que o número a ser adivinhado.")
    Tentativa = int(input("\nTentativa: "))
  if Tentativa == NumeroMedio:
    print("\n\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0
  else: 
    print("O número era", NumeroMedio)

#Dificuldade Extrema
if Dificuldade == 3:
  print("\n!O número está entre 1 a 1000!")
  Tentativa = int(input("Tentativa: "))
  while Tentativa != NumeroExtremo and Tentativa != 0:
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    if Tentativa < NumeroExtremo :
     print(Tentativa, " é MENOR do que o número a ser adivinhado.")
    else:
     print(Tentativa, " é MAIOR do que o número a ser adivinhado.")
    Tentativa = int(input("\nTentativa: "))
  if Tentativa == NumeroExtremo:
    print("\n\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0
  else: 
    print("O número era", NumeroExtremo)

#Dificuldade Impossivel
if Dificuldade == 4:
  print("\n!O número está entre 1 a 1000!")
  Tentativa = int(input("Tentativa: "))
  while Tentativa != NumeroExtremo and Tentativa != 0:
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    Tentativa = int(input("\nTentativa: "))
  if Tentativa == NumeroExtremo:
    print("\n\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0
  else: 
    print("O número era", NumeroExtremo)

#eastereag
while Dificuldade == 1557 :
 print("https://steamcommunity.com/id/bfc1557")
 break

print("")
Fim = input()

#changelogs
#V1.1
#Importei APENAS "randint"
#Mudei a estrutura das dificuldades colocando o if e so depois o while
#Adicionei um print que diz entre que números está a incognita
#Adicionado o caso de se o jogador quiser desistir coloca 0 na tentativa, o jogo acaba e é mostrado o valor da incognita