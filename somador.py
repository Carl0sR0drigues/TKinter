from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def somador():
    n1 = entrada1.get()
    n2 = entrada2.get()
    try:
        resultado = int(n1) + int(n2)
        # Adicionando título à mensagem
        resultado_label.config(text=f"Resultado da soma de {n1}+{n2} é {resultado}")
    except ValueError:
        # Adicionando título ao erro
        resultado_label.config(text="Erro: insira apenas números válidos.")

window = Tk()
window.title('SOMADOR!')
window.geometry('400x320')
window.eval('tk::PlaceWindow . center')

enter_text1 = ttk.Label(window, text= 'DIGITE UM VALOR')
enter_text1.pack(pady=10)

entrada1 = ttk.Entry(window, width=20)
entrada1.pack(pady=5)

enter_text2 = ttk.Label(window, text= 'DIGITE OUTRO VALOR')
enter_text2.pack(pady=10)

entrada2 = ttk.Entry(window, width=20)
entrada2.pack(pady=5)

button_sum = ttk.Button(window, text='CLICK PARA SOMAR', command=somador)
button_sum.pack(pady=10)

resultado_label = Label(window, text='', font=('Arial', 14), fg='blue')
resultado_label.pack(pady=10)

saida = ttk.Label(window, text='PRECIONE A TECLA ESC PARA SAIR')
saida.pack(pady=5)

text_sum = Label(window, text='')
text_sum.pack(pady=10)

window.bind("<Escape>", lambda event: window.destroy())

window.mainloop()

