import tkinter as tk

# Função para realizar as conversões
def converter_distancia():
    try:
        # Pega o valor inserido
        distance = float(entry_distancia.get())
        
        # Realiza as conversões
        km = distance / 1000
        hm = distance / 100
        dam = distance / 10
        dm = distance * 10
        cm = distance * 100
        mm = distance * 1000
        
        # Exibe os resultados nas labels
        label_resultado.config(
            text=f'{km} km\n{hm} hm\n{dam} dam\n{dm} dm\n{cm} cm\n{mm} mm'
        )
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido!")  # Mensagem de erro em caso de input inválido

# Função para sair
def sair():
    root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Conversão de Distância")

# Centralizar a janela
root.geometry("400x380+{}+{}".format(
    int((root.winfo_screenwidth() - 400) / 2), 
    int((root.winfo_screenheight() - 380) / 2)
))

# Texto de introdução
intro_label = tk.Label(root, text="Digite a distância em metros para conversão:")
intro_label.pack(pady=10)

# Entrada para a distância
entry_distancia_label = tk.Label(root, text="Distância em metros:")
entry_distancia_label.pack()
entry_distancia = tk.Entry(root)
entry_distancia.pack(pady=5)

# Botão de calcular conversão com fundo azul e texto em Arial Black
calc_button = tk.Button(root, text="Converter", command=converter_distancia, 
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
