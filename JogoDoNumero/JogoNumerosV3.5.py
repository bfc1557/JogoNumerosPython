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

#--------------------------------- Tentativas ------------------------------#
Tentativas = 0
Dicas = 1

#--------------------------------- Resposta na Consola ---------------------------------#
if Answer == True :
    print(NumeroFacil)
    print(NumeroMedio)
    print(NumeroExtremo)

#--------------------------------- Funções ---------------------------------#
def ComDicas():
    global Dicas
    Dicas = 1
    return Dicas
def SemDicas():
    global Dicas
    Dicas = 0
    return Dicas

#Botão para iniciar o jogo
def EscolherDificuldade():
    Estrutura.destroy()
    EstruturaDificuldade.pack()
    return EstruturaDificuldade

def Jogar():
    global Dificuldade
    Inicio.bind('<Return>', func)
    Dificuldade = MenuVariable.get()
    if Dificuldade == "Dificuldade":
        messagebox.showerror("Erro", "Tem de inserir uma dificuldade. ")
    else:
        #Escrever a dificuldade escolhida na estrtura 2
        TextoDificuldade = "A dificuldade escolhidada foi {}".format(Dificuldade)
        Label(Estrutura2, text=TextoDificuldade, font=(times,28,BOLD)).pack()
        #
        EstruturaDificuldade.destroy()
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
        Label(Estrutura3, text=("A resposta era {}".format(NumeroFacil))).pack()
    elif Dificuldade == "Medio":
        Label(Estrutura3, text=("A resposta era {}".format(NumeroMedio))).pack()
    elif Dificuldade == "Extremo":
        Label(Estrutura3, text=("A resposta era {}".format(NumeroExtremo))).pack()
    return Estrutura3

#Botão para sair
def Sair():
    Inicio.destroy()

#Resposta se errado
def Errado():
    global Tentativas
    global Dicas
    global Numero
    global NumeroFacil
    Tentativas = Tentativas + 1
    Resultado.config(text= "Erraste o numero")
    Resultado.pack()
    if Dificuldade == "Fácil":
        DicasNumero = NumeroFacil
    elif Dificuldade == "Medio":
        DicasNumero = NumeroMedio
    else:
        DicasNumero = NumeroExtremo
    
    if Dicas == 1:
        if Numero < DicasNumero:
            MostrarDicas.config(text="O número a adivinhar é maior.")
        else:
            MostrarDicas.config(text="O número a adivinhar é menor.")
    MostrarDicas.pack
    MostrarTentativas.config(text="Tentativas {}".format(Tentativas))
    MostrarTentativas.pack()
    return MostrarTentativas, MostrarDicas

#Reposta se vitoria
def TelaVitoria():
    Estrutura2.destroy()
    Estrutura4.pack()
    Estrutura4.update
    MostrarTentativasFim.config(text="Foram Precisas {} tentativas".format(Tentativas))
    MostrarTentativasFim.pack()
    return Estrutura4, MostrarTentativas


#--------------------------------- Core do Jogo ---------------------------------#
def func(event):
    ClickSubmeter()

def ClickSubmeter() :
    #Declaração global das variaveis
    global Inicio
    global Errado
    global Numero

    #obter valor introduzido e dificuldade
    Numero = Input.get()

    #Apagar Tentativa
    Input.delete(0, 'end')

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
Button(Estrutura, text="Jogar", font=(15) , width="40", height="2", command=EscolherDificuldade).pack()
Button(Estrutura, text="Sair", font=(15) , width="40", height="2", command=Sair).pack()

#------------------------------ Pagina Escolha Dificuldade ------------------------------#

#Menu da escolha da dificuldade
EstruturaDificuldade = Frame()
ExplicacaoDificuldade = Label(EstruturaDificuldade, text="Facil- de 0 a 10 | Medio- de 0 a 100 | Extremo- de 0 a 1000")
ExplicacaoDificuldade.config(font=(10000))
ExplicacaoDificuldade.pack()
MenuVariable = StringVar()
MenuVariable.set("Dificuldade")
Menu = OptionMenu(EstruturaDificuldade, MenuVariable, "Fácil", "Medio", "Extremo")
Menu.config(font=(10000))
Menu.pack()

#Dicas
var = IntVar(value= 1)
BotaoDicas = Radiobutton(EstruturaDificuldade, text="Abilitar Dicas", variable=var, value = 1, command = ComDicas)
BotaoSemDicas = Radiobutton(EstruturaDificuldade, text="Desabilitar Dicas", variable=var, value = 2, command= SemDicas)
BotaoDicas.pack()
BotaoSemDicas.pack()

#Botão de submeter
Button(EstruturaDificuldade, text="Iniciar", command=Jogar ).pack()


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

#Dicas
MostrarDicas = Label(EstruturaInterna2, text="")
MostrarDicas.pack()

#Tentativas
MostrarTentativas = Label(EstruturaInterna2, text="")
MostrarTentativas.pack()

#Botao para Desistir
EstruturaInterna3 = Frame(Estrutura2)
Button(EstruturaInterna3, text="Desistir", command=SairPerder, bg="red", fg="white").pack()

#--------------------------------- Pagina de Derrota ---------------------------------#
#Tela de Derrota
Estrutura3 = Frame(Inicio)
Label(Estrutura3, text="Perdeu", font=(times,60,BOLD) ).pack()
Button(Estrutura3, text="Sair", font=(15) , width="20", height="2", command=Sair, bg="red", fg="white").pack()
Label(Estrutura3, text="", font=(times,60,BOLD))

#--------------------------------- Pagina de Vitoria ---------------------------------#
#Tela de Vitoria
Estrutura4 = Frame(Inicio)
Label(Estrutura4, text="Ganhou", font=(times,60,BOLD) ).pack()
MostrarTentativasFim = Label(Estrutura4, text="")
MostrarTentativasFim.pack()
Button(Estrutura4, text="Sair", font=(15) , width="20", height="2", command=Sair, bg="red", fg="white").pack()

#Não mexer, Manter em ultimo
Inicio.mainloop()

#ChangeLog V3.5
#Adicionado as dicas

#ToDo:
#Embelezar o UI 
#Adicionar o jogar de novo
