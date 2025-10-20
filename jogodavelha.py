import tkinter as tk
from tkinter import messagebox

# ==============================
# 🎮 JOGO DA VELHA - Tkinter
# ==============================
# Autor: Iago Mello
# Turma: (adicione sua turma)
# Arquivo: jogo_da_velha_tkinter.py
# ==============================

# Cores e fontes
COR_FUNDO = "#e8ecf1"
COR_TABULEIRO = "#d6dee6"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"
COR_X = "#ff4d4d"
COR_O = "#2ecc71"

# Janela principal
janela = tk.Tk()
janela.title("🎮 Jogo da Velha")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

# Variáveis globais
jogador_atual = "X"
placar = {"X": 0, "O": 0}
botoes = []


# ==============================
# Funções do jogo
# ==============================

def verificar_vitoria():
    """Verifica se algum jogador venceu a partida"""
    for linha in range(3):
        if botoes[linha][0]["text"] == botoes[linha][1]["text"] == botoes[linha][2]["text"] != "":
            return True

    for coluna in range(3):
        if botoes[0][coluna]["text"] == botoes[1][coluna]["text"] == botoes[2][coluna]["text"] != "":
            return True

    if botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "":
        return True

    if botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != "":
        return True

    return False


def verificar_empate():
    """Verifica se houve empate"""
    for linha in botoes:
        for botao in linha:
            if botao["text"] == "":
                return False
    return True


def jogar(linha, coluna):
    """Executa a jogada do jogador atual"""
    global jogador_atual

    botao = botoes[linha][coluna]

    if botao["text"] == "":
        botao["text"] = jogador_atual
        botao["fg"] = COR_X if jogador_atual == "X" else COR_O

        if verificar_vitoria():
            placar[jogador_atual] += 1
            atualizar_placar()
            messagebox.showinfo("Fim de Jogo", f"Jogador {jogador_atual} venceu!")
            reiniciar_tabuleiro()
            return

        elif verificar_empate():
            messagebox.showinfo("Empate", "A partida terminou empatada!")
            reiniciar_tabuleiro()
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"


def reiniciar_tabuleiro():
    """Limpa o tabuleiro, mantendo o placar"""
    global jogador_atual
    jogador_atual = "X"
    for linha in botoes:
        for botao in linha:
            botao["text"] = ""


def zerar_placar():
    """Zera o placar dos jogadores"""
    placar["X"] = 0
    placar["O"] = 0
    atualizar_placar()


def atualizar_placar():
    """Atualiza a exibição do placar"""
    label_placar_x.config(text=f"Jogador X: {placar['X']}")
    label_placar_o.config(text=f"Jogador O: {placar['O']}")


def mostrar_creditos():
    """Exibe os créditos do projeto"""
    messagebox.showinfo(
        "Créditos",
        "🎮 Jogo da Velha desenvolvido por:\n"
        "Iago Mello\n"
        "Turma: (insira sua turma aqui)\n\n"
        "Projeto em Python com Tkinter."
    )


# ==============================
# Layout da Interface
# ==============================

# --- Linha 0: Placar ---
frame_placar = tk.Frame(janela, bg=COR_FUNDO)
frame_placar.grid(row=0, column=0, columnspan=3, pady=10)

label_placar_x = tk.Label(frame_placar, text="Jogador X: 0", font=("Helvetica", 14, "bold"),
                          bg=COR_FUNDO, fg=COR_X, padx=20)
label_placar_x.pack(side="left")

label_placar_o = tk.Label(frame_placar, text="Jogador O: 0", font=("Helvetica", 14, "bold"),
                          bg=COR_FUNDO, fg=COR_O, padx=20)
label_placar_o.pack(side="right")

# --- Linha 1: Tabuleiro ---
frame_tabuleiro = tk.Frame(janela, bg=COR_TABULEIRO)
frame_tabuleiro.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

for i in range(3):
    linha_botoes = []
    for j in range(3):
        botao = tk.Button(
            frame_tabuleiro,
            text="",
            font=("Helvetica", 32),
            width=5,
            height=2,
            bg=COR_BOTAO,
            fg=COR_TEXTO,
            activebackground="#5aa0f0",
            command=lambda linha=i, coluna=j: jogar(linha, coluna)
        )
        botao.grid(row=i, column=j, padx=5, pady=5)
        linha_botoes.append(botao)
    botoes.append(linha_botoes)

# --- Linha 2: Botões de Controle ---
frame_controles = tk.Frame(janela, bg=COR_FUNDO)
frame_controles.grid(row=2, column=0, columnspan=3, pady=15)

botao_reiniciar = tk.Button(frame_controles, text="♻️ Reiniciar Partida", font=("Helvetica", 12, "bold"),
                            bg="#3498db", fg="white", width=18, command=reiniciar_tabuleiro)
botao_reiniciar.grid(row=0, column=0, padx=10)

botao_zerar = tk.Button(frame_controles, text="🔄 Zerar Placar", font=("Helvetica", 12, "bold"),
                        bg="#e67e22", fg="white", width=15, command=zerar_placar)
botao_zerar.grid(row=0, column=1, padx=10)

botao_creditos = tk.Button(frame_controles, text="👤 Créditos", font=("Helvetica", 12, "bold"),
                           bg="#2ecc71", fg="white", width=12, command=mostrar_creditos)
botao_creditos.grid(row=0, column=2, padx=10)

# ==============================
# Iniciar o programa
# ==============================
janela.mainloop()
