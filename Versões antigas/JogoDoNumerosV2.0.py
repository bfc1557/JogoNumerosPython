#Jogo : Adivinha o número
#Jogo feito por bfc

#Importar da biblioteca "random" e "tkinter"
from random import randint
from tkinter import *
import tkinter

#Variaveis e gerador do número
NumeroFacil = randint(1,10)
NumeroMedio = randint(1,100)
NumeroExtremo = randint(1,1000)
Tentativas = 1
Dificuldade = 0

TextoCima = "Para jogar escolha a dificuldade inserindo um número."
TextoMeio = "1-Fácil │ 2-Medio │ 3-Extremo │ 4-Impossivel"

class First:

 def Facil():
     print("ok")
     TextoCima = "Ola"
     Inicio.update()
     Dificuldade = 1


#Inicio
Inicio = tkinter.Tk()
Inicio.title("Adivinha o Número")
Inicio.minsize("500","300")
Titlo = Label(Inicio, text="Adivinha o Número",)
Titlo.pack()
Texto1 = Label(Inicio, text= TextoCima)
Texto1.pack()
Texto2 = Label(Inicio, text=TextoMeio)
Texto2.pack()
Input = Entry(Inicio)
Input.pack()
Submeter = Button(Inicio, command=First , text="Submeter")
Submeter.pack()
Inicio.mainloop()

if Dificuldade == 1:
    TextoCima = "O número está compreendido entre 1 e 10"
    print("Sucesso")
