import random
import string
import tkinter as tk

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_senha_e_mostrar():
    tamanho_da_senha = int(tamanho_var.get())
    senha_gerada = gerar_senha(tamanho_da_senha)
    senha_label.config(text="Senha gerada: " + senha_gerada)

# Configuração da janela
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Estilização da janela
janela.geometry("400x200")  # Define o tamanho da janela
janela.configure(bg="lightgray")  # Define a cor de fundo


# Criação de widgets
tamanho_label = tk.Label(janela, text="Tamanho da Senha:")
tamanho_var = tk.StringVar()
tamanho_entry = tk.Entry(janela, textvariable=tamanho_var)
gerar_botao = tk.Button(janela, text="Gerar Senha", command=gerar_senha_e_mostrar)
senha_label = tk.Label(janela, text="Senha gerada: ")

# Layout dos widgets
tamanho_label.pack()
tamanho_entry.pack()
gerar_botao.pack()
senha_label.pack()

# Iniciar a janela
janela.mainloop()
