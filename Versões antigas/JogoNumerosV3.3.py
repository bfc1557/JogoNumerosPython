#--------------------------------- Informações ---------------------------------#
#Jogo : Adivinha o número
#Jogo feito por bfc e APáscoa

#--------------------------------- Configurações do Código ---------------------------------#
Answer = True #True/False para as respostas aparecerem na consola

#--------------------------------- Importações ---------------------------------#
from os import times
from random import randint
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

#--------------------------------- gerador do número ---------------------------------#
NumeroFacil = int(randint(1,10))
NumeroMedio = int(randint(1,100))
NumeroExtremo = int(randint(1,1000))

#--------------------------------- Resposta na Consola ---------------------------------#
if Answer == True :
    print(NumeroFacil)
    print(NumeroMedio)
    print(NumeroExtremo)

#--------------------------------- Funções ---------------------------------#

#Botão para iniciar o jogo
def Jogar():
    global Dificuldade
    Dificuldade = MenuVariable.get()
    if Dificuldade == "Dificuldade":
        messagebox.showerror("Erro", "Tem de inserir uma dificuldade. ")
    else:
        #Escrever a dificuldade escolhida na estrtura 2
        Label(Estrutura2, text=("A dificuldade escolhida foi", Dificuldade), font=(times,28,BOLD)).pack()
        #
        Estrutura.destroy()
        Estrutura2.pack()
        Estrutura2.update()
        EstruturaInterna.pack()
        EstruturaInterna.update()
        EstruturaInterna2.pack()
        EstruturaInterna2.update()
        EstruturaInterna3.pack()
        EstruturaInterna3.update()
        return Estrutura2

#Botão de desistir
def SairPerder():
    Estrutura2.destroy()
    Estrutura3.pack()
    Estrutura3.update
    if Dificuldade == "Fácil":
        Label(Estrutura3, text=("O número era", NumeroFacil)).pack()
    elif Dificuldade == "Medio":
        Label(Estrutura3, text=("O número era", NumeroMedio)).pack()
    elif Dificuldade == "Extremo":
        Label(Estrutura3, text=("O número era", NumeroExtremo)).pack()
    return Estrutura3

#Botão para sair
def Sair():
    Inicio.destroy()

#Resposta se errado
def Errado():
    Resultado.config(text= "Erraste o numero")
    Resultado.pack()

#Reposta se vitoria
def TelaVitoria():
    Estrutura2.destroy()
    Estrutura4.pack()
    Estrutura4.update
    return Estrutura4

#--------------------------------- Core do Jogo ---------------------------------#
def ClickSubmeter() :
    #Declaração global das variaveis
    global Inicio
    global Errado
    global Numero

    #obter valor introduzido e dificuldade
    Numero = Input.get()

    #testar se o valor introduzido não foi um numero
    NumeroPalavra = False
    try:
        Numero = int(Numero)
    except Exception:
        NumeroPalavra = True

    #Erro na introdução do numero
    if Numero == "":
        messagebox.showerror("Erro", "Tem de inserir um numero. ")
    elif NumeroPalavra:
        NumeroPalavra = False
        messagebox.showerror("Erro", "Só pode inserir um numero. ")
    else:
        Numero = int(Numero)
        #Dificuldade e se o numero está correto
        if Dificuldade == "Fácil" :
            if Numero == NumeroFacil :
                TelaVitoria()
            else:
                Errado()
        elif Dificuldade == "Medio" :
            if Numero == NumeroMedio :
                TelaVitoria()
            else:
                Errado()
        elif Dificuldade == "Extremo" :
            if Numero == NumeroExtremo :
                TelaVitoria()
            else:
                Errado()
#        elif Dificuldade == "Impossivel" :
#            if Numero == NumeroExtremo :
#                TelaVitoria()
#           else:
#               Errado()

#--------------------------------- Janela ---------------------------------#
Inicio = Tk()
Inicio.title("Adivinha o Número")
w, h = Inicio.winfo_screenwidth(), Inicio.winfo_screenheight()
Inicio.geometry("%dx%d" % (w, h))

#--------------------------------- Pagina Inicial ---------------------------------#
Estrutura = Frame(Inicio)
Estrutura.pack()
Logo = PhotoImage(file="Logo.png")
LogoLabel = Label(Estrutura, image = Logo).pack()
Button(Estrutura, text="Jogar", font=(15) , width="40", height="2", command=Jogar).pack()
Button(Estrutura, text="Sair", font=(15) , width="40", height="2", command=Sair).pack()

#Menu da escolha da dificuldade
MenuVariable = StringVar()
MenuVariable.set("Dificuldade")
Menu = OptionMenu(Estrutura, MenuVariable, "Fácil", "Medio", "Extremo") #, "Impossivel"
Menu.config(font=(10000))
Menu.pack()

#--------------------------------- Pagina de Jogo ---------------------------------#
Estrutura2 = Frame()
Label(Estrutura2, text= "Insira a sua tentativa do numero", font=(times,34,BOLD)).pack()

#introdução do numero
EstruturaInterna = Frame(Estrutura2)
Input = Entry(EstruturaInterna, width="15", font=(times,34,BOLD), justify=CENTER)
Input.pack()

#Botão de submeter
Submeter = Button(EstruturaInterna, command=ClickSubmeter , text="Submeter", font=(times,15,BOLD))
Submeter.pack()

EstruturaInterna2 = Frame(Estrutura2)
#escrita do resultado
Resultado = Label(EstruturaInterna2, text="", font=(times,34,BOLD))
Resultado.pack()

#Botao para Desistir
EstruturaInterna3 = Frame(Estrutura2)
Button(EstruturaInterna3, text="Desistir", command=SairPerder, bg="red", fg="white").pack()

#--------------------------------- Pagina de Derrota ---------------------------------#
#Tela de Derrota
Estrutura3 = Frame(Inicio)
Label(Estrutura3, text="Perdeu", font=(times,60,BOLD) ).pack()
Button(Estrutura3, text="Sair", font=(15) , width="20", height="2", command=Sair, bg="red", fg="white").pack()
Label(Estrutura3, text="A resposta era:", font=(times,60,BOLD))

#--------------------------------- Pagina de Vitoria ---------------------------------#
#Tela de Vitoria
Estrutura4 = Frame(Inicio)
Label(Estrutura4, text="Ganhou", font=(times,60,BOLD) ).pack()
Button(Estrutura4, text="Sair", font=(15) , width="20", height="2", command=Sair, bg="red", fg="white").pack()

#Não mexer, Manter em ultimo
Inicio.mainloop()

#Atualização da UI
#Organização do código
#Correção de bugs

#ToDo:
#Adicionar tentativas
#Embelezar o UI
#Corrigir bug de texto