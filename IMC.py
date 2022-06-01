# impotação da biblioteca
from tkinter import *

# comando para o botão
def calculo():
    if ePeso.get().replace('.', '', 1).isnumeric() and eAltu.get().replace('.', '', 1).isnumeric():
        lResult['text'] = float(ePeso.get()) / float(eAltu.get()) ** 2
        if lResult['text'] < 18.5:
            lmagreza['background'] = '#f3f788'
        elif 18.5 < lResult['text'] < 24.9:
            lnormal['background'] = '#88f7ab'
        elif 25.0 < lResult['text'] < 29.9:
            lsobrep['background'] = '#f3f788'
        elif 30.0 < lResult['text'] < 39.9:
            lobesidade['background'] = '#fac975'
        elif lResult['text'] > 40.0:
            lobesigrave['background'] = '#f78472'
    else:
        lResult['text'] = 'Valor Inválido!'


def limpar():
    lmagreza['background'] = '#d0f7f7'
    lnormal['background'] = '#d0f7f7'
    lsobrep['background'] = '#d0f7f7'
    lobesidade['background'] = '#d0f7f7'
    lobesigrave['background'] = '#d0f7f7'


# criando a janela
janela = Tk()
janela.config(background='#d0f7f7')
janela.bind('<Return>', lambda event: calculo())

# label's
lPeso = Label(janela, text='Peso', font='Calibri 14', bg='#d0f7f7')
lAltu = Label(janela, text='Altura', font='Calibri 14', bg='#d0f7f7')
lImc = Label(janela, text='Seu IMC:', font='Calibri 14', bg='#d0f7f7')
lResult = Label(janela, text=0, font='Calibri 14', bg='#d0f7f7')

lmagreza = Label(janela, text='MENOR QUE 18,5	 |   MAGREZA', bg='#d0f7f7')

lnormal = Label(janela, text='ENTRE 18,5 E 24,9   |   IDEAL', bg='#d0f7f7')

lsobrep = Label(janela, text='ENTRE 25,0 E 29,9	   |   SOBREPESO', bg='#d0f7f7')

lobesidade = Label(janela, text='ENTRE 30,0 E 39,9   |    OBESIDADE', bg='#d0f7f7')

lobesigrave = Label(janela, text='MAIOR QUE 40,0	  |    OBESIDADE GRAVE', bg='#d0f7f7')

ltabela = Label(janela, text='IMC         CLASSIFICAÇÃO', font='Calibri 12', bg='#d0f7f7')


# entry do peso e altura
ePeso = Entry(janela)
eAltu = Entry(janela)

# botão para fazer o calculo
bCalculo = Button(janela, text='Calcular', bg='#9ef7f7', command=calculo)

bLimpar = Button(janela, text='Limpar', bg='#9ef7f7', command=limpar)


# ORGANIZAÇÃO

# peso
lPeso.grid(row=0, column=0)
ePeso.grid(row=1, column=0)

# altura
lAltu.grid(row=2, column=0)
eAltu.grid(row=3, column=0)

# calculo
bCalculo.grid(row=5, column=0)
bLimpar.grid(row=7, column=0)

# resultado
lImc.grid(row=0, column=1)
lResult.grid(row=1, column=1)

# tabela de classificação
ltabela.grid(row=2, column=1)
lmagreza.grid(row=3, column=1)
lnormal.grid(row=4, column=1)
lsobrep.grid(row=5, column=1)
lobesidade.grid(row=6, column=1)
lobesigrave.grid(row=7, column=1)

# EXECUÇÃO
mainloop()