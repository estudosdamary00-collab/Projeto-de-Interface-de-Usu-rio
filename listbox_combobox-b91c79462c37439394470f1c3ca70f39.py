"""
Exemplo didático: Listbox e Combobox com Tkinter
IFMT — Análise e Desenvolvimento de Sistemas
"""

import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("Listbox e Combobox")
janela.geometry("420x480")
janela.configure(bg="#EBF5FB")
janela.resizable(False, False)

# ── Título ──────────────────────────────────────────────────────────
tk.Label(
    janela,
    text="Listbox e Combobox",
    font=("Arial", 15, "bold"),
    bg="#1B4F72",
    fg="white",
    pady=12
).pack(fill="x")

# ── Combobox ────────────────────────────────────────────────────────
# Combobox → lista SUSPENSA (o usuário escolhe um item de um menu)
# values   → tupla ou lista com as opções disponíveis
# state    → 'readonly' impede que o usuário digite livremente
tk.Label(janela, text="1. Escolha um curso (Combobox):",
         font=("Arial", 11, "bold"), bg="#EBF5FB", fg="#1B4F72").pack(pady=(18, 4))

var_curso = tk.StringVar()
combo = ttk.Combobox(
    janela,
    textvariable=var_curso,
    values=["ADS", "Redes", "Informática", "Eletrotécnica"],
    font=("Arial", 11),
    width=24,
    state="readonly"
)
combo.set("Selecione...")   # texto padrão exibido
combo.pack()

# ── Listbox ─────────────────────────────────────────────────────────
# Listbox  → lista VISÍVEL (todos os itens ficam exibidos na tela)
# height   → quantas linhas ficam visíveis
# .insert(tk.END, item) → adiciona item ao final da lista
# .curselection()       → retorna o índice do item selecionado
# .get(índice)          → retorna o texto do item naquele índice
tk.Label(janela, text="2. Escolha uma linguagem (Listbox):",
         font=("Arial", 11, "bold"), bg="#EBF5FB", fg="#1B4F72").pack(pady=(18, 4))

listbox = tk.Listbox(
    janela,
    font=("Arial", 11),
    height=5,
    width=26,
    bg="white",
    selectbackground="#2E86C1",
    selectforeground="white",
    relief="solid",
    bd=1
)
listbox.pack()

# Populando a Listbox com .insert()
linguagens = ["Python", "Java", "JavaScript", "C++", "Kotlin"]
for linguagem in linguagens:
    listbox.insert(tk.END, linguagem)   # tk.END = insere sempre no fim

# ── Botão ───────────────────────────────────────────────────────────
def mostrar():
    curso = var_curso.get()
    indices = listbox.curselection()          # retorna tupla com índices selecionados

    if curso == "Selecione...":
        messagebox.showwarning("Atenção", "Escolha um curso no Combobox!")
        return

    if not indices:
        messagebox.showwarning("Atenção", "Escolha uma linguagem na Listbox!")
        return

    linguagem = listbox.get(indices[0])       # pega o texto pelo índice
    messagebox.showinfo(
        "Sua escolha",
        f"Curso:      {curso}\nLinguagem:  {linguagem}"
    )

tk.Button(
    janela,
    text="✅  Ver Escolha",
    command=mostrar,
    bg="#1B4F72",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18,
    relief="flat",
    cursor="hand2"
).pack(pady=24)

# ── Tabela de diferenças ────────────────────────────────────────────
frame_info = tk.Frame(janela, bg="#D5E8F0", padx=16, pady=10)
frame_info.pack(fill="x", padx=20)

tk.Label(frame_info, text="Diferença principal:",
         font=("Arial", 10, "bold"), bg="#D5E8F0", fg="#1A5276").pack(anchor="w")
tk.Label(frame_info, text="• Combobox → lista suspensa, ocupa pouco espaço",
         font=("Arial", 10), bg="#D5E8F0", fg="#1A5276").pack(anchor="w")
tk.Label(frame_info, text="• Listbox  → lista sempre visível, ideal para muitos itens",
         font=("Arial", 10), bg="#D5E8F0", fg="#1A5276").pack(anchor="w")

# ── Rodapé ──────────────────────────────────────────────────────────
tk.Label(janela, text="IFMT — Apostila de Tkinter",
         font=("Arial", 8, "italic"), bg="#EBF5FB", fg="#7F8C8D").pack(side="bottom", pady=6)

janela.mainloop()
