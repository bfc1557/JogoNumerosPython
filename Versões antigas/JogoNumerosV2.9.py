#Jogo : Adivinha o número
#Jogo feito por bfc e APáscoa


Answer = True #True/False para as respostas aparecerem na consola

#Importar da biblioteca "random" e "tkinter"
from os import times
from random import randint
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

#Variaveis e gerador do número
NumeroFacil = int(randint(1,10))
NumeroMedio = int(randint(1,100))
NumeroExtremo = int(randint(1,1000))

#Escrita das respostas na consola
if Answer == True :
    print(NumeroFacil)
    print(NumeroMedio)
    print(NumeroExtremo)

#Janela
Inicio = Tk()
Inicio.title("Adivinha o Número")
w, h = Inicio.winfo_screenwidth(), Inicio.winfo_screenheight()
Inicio.geometry("%dx%d" % (w, h))

def Jogar():
    global Estrutura
    Estrutura.destroy()
    Estrutura2.pack()
    EstruturaInterna.pack()
    EstruturaInterna2.pack()
    EstruturaInterna3.pack()
    Estrutura2.update()
    EstruturaInterna.update()
    EstruturaInterna2.update()
    EstruturaInterna3.update()
    return Estrutura2

def Sair():
    Inicio.destroy()

#Menu Principal
Estrutura = Frame(Inicio)
Estrutura.pack()
Logo = PhotoImage(file="JogoNumeros\Logo.png")
LogoLabel = Label(Estrutura, image = Logo).pack()

#Botões Menu Principal
JogarBotao = Button(Estrutura, text="Jogar", font=(15) , width="40", height="2", command=Jogar)
JogarBotao.pack()
SairDesktop = Button(Estrutura, text="Sair", font=(15) , width="40", height="2", command=Sair)
SairDesktop.pack()


#Estrutura 2
Estrutura2 = Frame()

#Menu da escolha da dificuldade
MenuVariable = StringVar(Estrutura2)
MenuVariable.set("Dificuldade")
Menu = OptionMenu(Estrutura2, MenuVariable, "Fácil", "Medio", "Extremo") #, "Impossivel"
Menu.config(font=(10000))
Menu.pack()

#introdução do numero
Text2 = Label(Estrutura2, text= "Insira a sua tentativa do numero", font=(times,34,BOLD))
Text2.pack

EstruturaInterna = Frame(Estrutura2)
Input = Entry(EstruturaInterna, width="15", font=(times,34,BOLD), justify=CENTER)
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
    messagebox.showerror("Erro", "Tem de inserir uma dificuldade. ")

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
Submeter = Button(EstruturaInterna, command=ClickSubmeter , text="Submeter", font=(times,15,BOLD))
Submeter.pack()

EstruturaInterna2 = Frame(Estrutura2)
#escrita do resultado
Resultado = Label(EstruturaInterna2, text="", font=(times,34,BOLD))
Resultado.pack()

#Função desistir
def Geral():
    Desistir()
    MostrarNumero()
def Desistir():
    global Estrutura2
    global Estrutura3
    Estrutura2.destroy()
    Estrutura3.pack()
    Estrutura3.update
    return Estrutura3
def MostrarNumero():
    Dificuldade = StringVar()
    Dificuldade = MenuVariable.get()
    if Dificuldade == "Fácil":
        Numero = Label(Estrutura3, text=("O número era", NumeroFacil)).pack()
    elif Dificuldade == "Medio":
        Numero = Label(Estrutura3, text=("O número era", NumeroMedio)).pack()
    elif Dificuldade == "Extremo":
        Numero = Label(Estrutura3, text=("O número era", NumeroExtremo)).pack()

#Botao para Desistir
EstruturaInterna3 = Frame(Estrutura2)
DesistirBotao = Button(EstruturaInterna3, text="Desistir", command=Geral, bg="red", fg="white").pack()


#Estrutura 3
#Tela de Derrota
Estrutura3 = Frame(Inicio)
Perdeu = Label(Estrutura3, text="Perdeu", font=(times,60,BOLD) )
Perdeu.pack()

#Botao Sair
SairPerder = Button(Estrutura3, text="Sair", font=(15) , width="20", height="2", command=Sair, bg="red", fg="white")
SairPerder.pack()

#Não mexer, Manter em ultimo
Inicio.mainloop()

#Adicionada tela Inicial e tela de desistencia
#Melhoramento Estetico(A ser continuado)
#Erros agora são pop-ups

#To-do-list
#Continuar a melhorar o design
#Corrigir