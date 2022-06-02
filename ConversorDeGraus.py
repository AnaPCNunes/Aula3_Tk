# impotação da biblioteca
from tkinter import *

# comando para o botão
def transpor():
    if entrada.get().replace('.','', 1).isnumeric():
        label4['text'] = float(entrada.get()) * 1.8 + 32

# criando a janela
janela = Tk()
janela.config(background='#d0f7f7')
janela.bind('<Return>', lambda event: transpor())

entrada = Entry(janela)
btn = Button(janela, text='Converter', font='14', command=transpor)
label1 = Label(janela, text='Convertendo Valores', font='Arial 14 bold', bg='#d0f7f7')
label2 = Label(janela, text='Graus Celsius:', font='11', bg='#d0f7f7')
label3 = Label(janela, text='Graus Fahrenheit:', font='11', bg='#d0f7f7')
label4 = Label(janela, text='', font='11', bg='#d0f7f7')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entrada.grid(row=1, column=1)
label3.grid(row=2, column=0)
label4.grid(row=2, column=1)
btn.grid(row=3, column=1)

# EXECUÇÃO
mainloop()