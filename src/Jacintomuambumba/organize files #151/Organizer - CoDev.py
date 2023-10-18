import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk

def organizar_arquivos():
    diretorio_origem = filedialog.askdirectory(title="Selecione a pasta de origem")

    if not diretorio_origem:
        return  # Cancelou a seleção da pasta

    mapeamento_extensoes = {
        ".mp3": "my music",
        ".jpg": "my pictures",
        ".png": "my pictures",
        ".mp4": "my videos",
        # Adicione mais extensões e pastas conforme necessário
    }

    extensao_desconhecida = "others"

    for pasta in set(mapeamento_extensoes.values()):
        destino = os.path.join(diretorio_origem, pasta)
        os.makedirs(destino, exist_ok=True)

    arquivos = os.listdir(diretorio_origem)
    total_arquivos = len(arquivos)

    progresso = ttk.Progressbar(janela, length=400, mode="determinate")
    progresso.pack()

    for idx, arquivo in enumerate(arquivos):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = Path(arquivo).suffix.lower()
            if extensao in mapeamento_extensoes:
                pasta_destino = mapeamento_extensoes[extensao]
            else:
                pasta_destino = extensao_desconhecida

            destino = os.path.join(diretorio_origem, pasta_destino, arquivo)
            os.makedirs(os.path.join(diretorio_origem, pasta_destino), exist_ok=True)
            shutil.move(caminho_arquivo, destino)

            # Atualize o valor da barra de progresso
        progresso['value'] = idx + 1
        janela.update_idletasks()

    resultado_label.config(text="Organização de arquivos concluída.")

# Configuração da janela
janela = tk.Tk()
janela.title("Organizador de Arquivos - Codev")

# Personalização de cores e fontes
janela.configure(bg="#51f5b6")  # Cor de fundo da janela
janela.geometry("700x400")  # Tamanho da janela
janela.option_add("*TButton*highlightBackground", "#b0b0b0")

# Carregue a imagem e obtenha suas dimensões
imagem = Image.open("icon2.png")
largura, altura = imagem.size

# Crie um objeto ImageTk para a imagem
imagem_tk = ImageTk.PhotoImage(imagem)

# Defina o tamanho do botão com base nas dimensões da imagem
botao_organizar = tk.Button(janela, image=imagem_tk, text="Organizar Arquivos", compound="top", command=organizar_arquivos, width=largura, height=altura)
botao_organizar.pack(pady=50)

# Rótulo personalizado
resultado_label = tk.Label(janela, text="", bg="#f0f0f0", font=("Arial", 12))
resultado_label.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()
