from tkinter import *
from tkinter import ttk
import datetime as dt

#Janela Inicial
janela_inicial = Tk()
janela_inicial.title("Tabuada")
janela_inicial.geometry('1000x600')

#Label 1
numero_multiplicacao = Label(janela_inicial,text= 'Digite o numero de vezes que será calculado a tabuada:')
numero_multiplicacao.grid(column=0, row=1, sticky='e')
#numero_multiplicacao.pack()

#Text Box 1
text_box1 = Entry(janela_inicial, width=10)
text_box1.grid(column=1, row=1) #Text(janela_inicial,height=1,width=20)
text_box1.focus_set()

#Label 2
numero_tabuada = Label(janela_inicial,text='Digite o numero da qual deseja saber a tabuada:')
numero_tabuada.grid(column=0, row=2, sticky='e')

#Text Box2
text_box2 = Entry(janela_inicial, width=10) #Text(janela_inicial,height=1,width=20) 
text_box2.grid(column=1, row=2)

#Método para preencher ListBox1 e ComboBox1 com resultado da tabuada
def getTextInput():
    lista_para_combobox = []
    primeira_entrada = float( text_box1.get() ) + 1
    segunda_entrada = float( text_box2.get())
    lista_tabuada.delete(0, END)
    combobox_resultado_tabuada.delete(0, END)
    linha = 0
    while linha < primeira_entrada:
        valor_tabuada = segunda_entrada * linha
        entrada_lista = f'{linha:2.0f} x {segunda_entrada:2.0f} = {valor_tabuada:3.1f}'
        lista_para_combobox.append(valor_tabuada)
        lista_tabuada.insert(END, entrada_lista)
        combobox_resultado_tabuada['values'] = lista_para_combobox
        linha += 1

#Botao para calcular tabuada
read_textbox1 = Button(janela_inicial, height=1, width=10, text='Calcular', command=getTextInput)
read_textbox1.grid(column=1, row=3)

#ListBox 1 : Resultado Calculo Tabuada
lista_tabuada = Listbox(janela_inicial, height=20, width=20)
lista_tabuada.grid(column=1, row=4)

#Combobox 1 : Resultado Calculo Tabuada
combobox_resultado_tabuada = ttk.Combobox(janela_inicial, background='White')
combobox_resultado_tabuada.grid(column=0, row=3, sticky='e')

#Label MÊS
label_mes = Label(janela_inicial,text='Selecione o mês:')
label_mes.grid(column=2, row=1, sticky='e')

#ComboBox MÊS
combobox_mes = ttk.Combobox(
    janela_inicial,
    values=['Janeiro',  'Fevereiro',    'Março',
            'Abril',    'Maio',         'Junho',
            'Julho',    'Agosto',       'Setembro',
            'Outubro',  'Novembro',     'Dezembro']
)
combobox_mes.grid(column=3, row=1)

#Label ANO
label_ano = Label(janela_inicial, text='Informe o ano:')
label_ano.grid(column=2, row=2, sticky='e')

#ComboBox ANO
combobox_ano = ttk.Combobox(janela_inicial,)
combobox_ano.grid(column=3, row=2)

#Analisar entradas para ComboBox ANO
ano_atual = dt.date.today().year
linha = 0
ano_inicial = ano_atual - 5
lista_ano = []
while linha < 10:
    lista_ano.append(ano_inicial + linha)
    linha += 1
combobox_ano['values']= lista_ano

# Manter janela aberta
janela_inicial.mainloop()
