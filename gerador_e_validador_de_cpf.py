import tkinter as tk
import random
import re

# Função para gerar CPF
def gerar_cpf():
    gerado_novo = ''
    for i in range(9):
        gerado_novo += str(random.randint(0, 9))
    cpf_9 = gerado_novo[:9]
    resultado = 0
    contador = 10

    for digito in cpf_9:
        resultado += int(digito) * contador
        contador -= 1
        resto = resultado * 10 % 11

    if resto > 9:
        resto_final = 'Resultado= 0'
    elif resto <= 9:
        resto_final = resto
        cpf_resto_final = (f'{gerado_novo}{resto_final}')

    cpf_10 = cpf_resto_final[:10]
    resultado_2 = 0
    contador_11 = 11

    for digito2 in cpf_10:
        resultado_2 += int(digito2) * contador_11
        contador_11 -= 1
        resto2 = resultado_2 * 10 % 11

    if resto2 > 9:
        resto_final2 = 'Resultado= 0'
    elif resto2 <= 9:
        resto_final2 = resto2

    return f'{gerado_novo}{resto_final}{resto_final2}'

# Função para validar CPF
def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    repedidos = cpf == cpf[0] * len(cpf)
    
    if repedidos:
        return 'Você inseriu números inválidos'

    cpf_9 = cpf[:9]
    resultado = 0
    contador = 10

    for digito in cpf_9:
        resultado += int(digito) * contador
        contador -= 1
        resto = resultado * 10 % 11

    if resto > 9:
        resto_final = 'Resultado= 0'
    elif resto <= 9:
        resto_final = resto
        cpf_resto_final = (f'{cpf}{resto_final}')

    cpf_10 = cpf_resto_final[:10]
    resultado_2 = 0
    contador_11 = 11

    for digito2 in cpf_10:
        resultado_2 += int(digito2) * contador_11
        contador_11 -= 1
        resto2 = resultado_2 * 10 % 11

    if resto2 > 9:
        resto_final2 = 'Resultado= 0'
    elif resto2 <= 9:
        resto_final2 = resto2

    if cpf[-2:] == f"{resto_final}{resto_final2}":
        return f"CPF {cpf} válido"
    else:
        return f"CPF {cpf} inválido"

# Função que é chamada quando o botão é pressionado
def on_button_click():
    atividade = atividade_var.get()
    cpf_input = cpf_entry.get().strip()

    if atividade == 1:
        # Gerar CPF
        cpf_gerado = gerar_cpf()
        cpf_gerado_entry.delete(0, tk.END)  # Limpar a Entry
        cpf_gerado_entry.insert(0, cpf_gerado)  # Inserir o CPF gerado na Entry
    elif atividade == 2:
        # Validar CPF
        resultado = validar_cpf(cpf_input)
        result_label.config(text=resultado)

# Função para configurar o tipo de atividade
def escolher_atividade(atividade):
    atividade_var.set(atividade)

# Função para permitir apenas números no campo de CPF
def validar_entrada_numeros(event):
    texto = cpf_entry.get()
    if not texto.isdigit() and texto != "":
        cpf_entry.delete(len(texto)-1, tk.END)  # Remove o último caractere

# Função para fechar a aplicação
def sair():
    root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador e Validador de CPF")

# Centralizar a janela
root.geometry("400x470+{}+{}".format(
    int((root.winfo_screenwidth() - 400) / 2), 
    int((root.winfo_screenheight() - 470) / 2)
))

# Variável para armazenar a atividade escolhida
atividade_var = tk.IntVar(value=1)

# Texto de introdução
intro_label = tk.Label(root, text="Escolha a atividade:")
intro_label.pack(pady=10)

# Botões de atividade com fundo azul e texto em Arial Black
btn_gerar = tk.Radiobutton(root, text="Gerar CPF", variable=atividade_var, value=1, 
                           fg="black", font=("Arial Black", 12))
btn_validar = tk.Radiobutton(root, text="Validar CPF", variable=atividade_var, value=2, 
                            fg="black", font=("Arial Black", 12))
btn_gerar.pack()
btn_validar.pack()

# Entrada de CPF
cpf_label = tk.Label(root, text="Digite o CPF (se aplicável):")
cpf_label.pack(pady=10)

cpf_entry = tk.Entry(root, width=25)
cpf_entry.pack(pady=5)

# Configurar para aceitar apenas números no campo CPF
cpf_entry.bind("<KeyRelease>", validar_entrada_numeros)

# Botão de ação com fundo azul e texto em Arial Black
action_button = tk.Button(root, text="Executar", command=on_button_click, 
                          bg="blue", fg="white", font=("Arial Black", 12))
action_button.pack(pady=20)

# Label para mostrar o resultado
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Entrada para mostrar o CPF gerado
cpf_gerado_label = tk.Label(root, text="CPF Gerado:")
cpf_gerado_label.pack(pady=10)

cpf_gerado_entry = tk.Entry(root, width=25)
cpf_gerado_entry.pack(pady=5)

# Botão de saída com fundo azul e texto em Arial Black
exit_button = tk.Button(root, text="Sair", command=sair, 
                        bg="blue", fg="white", font=("Arial Black", 12))
exit_button.pack(pady=10)

# Iniciar a janela
root.mainloop()
