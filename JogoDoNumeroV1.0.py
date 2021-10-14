#Jogo : Adivinha o número
#Jogo feito por bfc

#-Notas-
#Existem 4 Dificuldades. Depois de o usuario escolher uma delas é executado um while(enquanto) em que a condição for verdadeira.
#Apos ser pedida a tentativa é verificada se a tentativa corresponde ao número gerado, e para isso usei o if e o else. Se a condição for falsa, ou seja o número não corresponder é mostrado um errado e se o número dado é maior ou menor do gerado. Caso o número seja igual ao gerado é mostrado um correto e o número de tentativas. Obs: O nivel impossivel(4)não da dicas ;)

#Importar biblioteca "random"
from random import *

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
print("1-Fácil │ 2-Medio │ 3-Extremo 4-Impossivel")
Dificuldade = int(input())

#Dificuldade Facil
while Dificuldade == 1:
  Tentativa = int(input("\nTentativa: ")) 
  if Tentativa != NumeroFacil :
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    if Tentativa < NumeroFacil :
     print(Tentativa, " é MENOR do que o número a ser adivinhado.")
    else:
     print(Tentativa, " é MAIOR do que o número a ser adivinhado.")
  else:
    print("\n\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0

#Dificuldade Media
while Dificuldade == 2:
  Tentativa = int(input("\nTentativa: ")) 
  if Tentativa != NumeroMedio :
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    if Tentativa < NumeroMedio :
     print(Tentativa, " é MENOR do que o número a ser adivinhado.")
    else:
     print(Tentativa, " é MAIOR do que o número a ser adivinhado.")
  else:
    print("\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0

#Dificuldade Extrema
while Dificuldade == 3:
  Tentativa = int(input("\nTentativa: ")) 
  if Tentativa != NumeroExtremo :
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
    if Tentativa < NumeroExtremo :
     print(Tentativa, " é MENOR do que o número a ser adivinhado.")
    else:
     print(Tentativa, " é MAIOR do que o número a ser adivinhado.")
  else:
    print("\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0

#Dificuldade Impossivel
while Dificuldade == 4:
  Tentativa = int(input("\nTentativa: ")) 
  if Tentativa != NumeroExtremo :
    print("-------- [ERRADO] --------")
    Tentativas = Tentativas + 1
  else:
    print("\n       -ˋˏ ༻✿༺ ˎˊ-")
    print("\n-------- [CORRETO] --------")
    print("Foram precisas: ", Tentativas, " tentativas.")
    Dificuldade = 0

#eastereag
while Dificuldade == 1557 :
 print("https://steamcommunity.com/id/bfc1557")
 break

Fim = input()
