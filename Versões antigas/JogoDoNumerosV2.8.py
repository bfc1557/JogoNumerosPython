#Jogo : Adivinha o número
#Jogo feito por bfc e APáscoa

Answer = True #True/False para as respostas aparecerem na consola

#Importar da biblioteca "random" e "tkinter"
from random import randint
from tkinter import *

#Variaveis e gerador do número
NumeroFacil = int(randint(1,10))
NumeroMedio = int(randint(1,100))
NumeroExtremo = int(randint(1,1000))

#Escrita das respostas na consola
if Answer == True :
    print(NumeroFacil)
    print(NumeroMedio)
    print(NumeroExtremo)

#Texto inicial
Inicio = Tk()
Inicio.title("Adivinha o Número")
Inicio.minsize("500","300")
Titulo = Label(Inicio, text="Adivinha o Número",)
Titulo.pack()
Text1 = Label(Inicio, text= "Escolha a dificuldade!")
Text1.pack()

#Menu da escolha da dificuldade
MenuVariable = StringVar(Inicio)
MenuVariable.set("Dificuldade")
Menu = OptionMenu(Inicio, MenuVariable, "Fácil", "Medio", "Extremo") #, "Impossivel"
Menu.pack()

#introdução do numero
Text2 = Label(Inicio, text= "Insira a sua tentativa do numero")
Text2.pack
Input = Entry(Inicio)
Input.pack()

#Resposta se correto
def Correto():
    Resultado.config(text= "Acertaste o numero")
    Resultado.pack()

#Resposta se errado
def Errado():
    Resultado.config(text= "Erraste o numero")
    Resultado.pack()

#Resposta se não introduzir dificuldade
def ErroDificuldade():
    Resultado.config(text= "Não foi introduzida nenhuma dificuldade.")
    Resultado.pack()

#Ao clicar fazer isto
def ClickSubmeter() :
    #Declaração global das variaveis
    global ErroDificuldade
    global Inicio
    global Correto
    global Errado
    
    #obter variaveis
    Dificuldade = MenuVariable.get()
    Numero = int(Input.get())
    

    #Dificuldade e se o numero está correto
    if Dificuldade == "Fácil" :
        if Numero == NumeroFacil :
            Correto()
        else:
            Errado()
    elif Dificuldade == "Medio" :
        if Numero == NumeroMedio :
            Correto()
        else:
            Errado()
    elif Dificuldade == "Extremo" :
        if Numero == NumeroExtremo :
            Correto()
        else:
            Errado()
#    elif Dificuldade == "Impossivel" :
#        if Numero == NumeroExtremo :
#            Correto()
#        else:
#            Errado()
    
    #erro de sem dificuldade introduzida
    elif Dificuldade == "Dificuldade":
        ErroDificuldade()

#Botão de submeter
Submeter = Button(Inicio, command=ClickSubmeter , text="Submeter")
Submeter.pack()

#escrita do resultado
Resultado = Label(Inicio, text="")
Resultado.pack()

#Não mexer, Manter em ultimo
mainloop()

