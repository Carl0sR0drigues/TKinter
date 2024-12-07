import tkinter as tk

# Função para calcular a soma
def calcular_soma():
    try:
        num1 = float(entry_num1.get())  # Pega o primeiro número
        num2 = float(entry_num2.get())  # Pega o segundo número
        resultado = num1 + num2  # Realiza a soma
        label_resultado.config(text=f"A soma de {num1} e {num2} é {resultado}")  # Exibe o resultado
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos!")  # Mensagem de erro em caso de input inválido

# Função para sair
def sair():
    root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Soma")

# Centralizar a janela
root.geometry("400x300+{}+{}".format(
    int((root.winfo_screenwidth() - 400) / 2), 
    int((root.winfo_screenheight() - 300) / 2)
))

# Texto de introdução
intro_label = tk.Label(root, text="Digite dois números para somar:")
intro_label.pack(pady=10)

# Entrada para o primeiro número
entry_num1_label = tk.Label(root, text="Digite o primeiro número:")
entry_num1_label.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Entrada para o segundo número
entry_num2_label = tk.Label(root, text="Digite o segundo número:")
entry_num2_label.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Botão de calcular soma com fundo azul e texto em Arial Black
calc_button = tk.Button(root, text="Calcular Soma", command=calcular_soma, 
                        bg="blue", fg="white", font=("Arial Black", 12))
calc_button.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="", font=("Helvetica", 12))
label_resultado.pack(pady=10)

# Botão de saída com fundo azul e texto em Arial Black
exit_button = tk.Button(root, text="Sair", command=sair, 
                        bg="blue", fg="white", font=("Arial Black", 12))
exit_button.pack(pady=10)

# Iniciar a janela
root.mainloop()
