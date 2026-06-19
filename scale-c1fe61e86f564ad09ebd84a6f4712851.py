import tkinter as tk

janela = tk.Tk()
janela.title("🐾 Adoção Responsável — Energia do Pet")
janela.geometry("400x300")
janela.configure(bg="#C7A5FD")
janela.resizable(False, False)

tk.Label(
    janela,
    text="Nível de energia do pet",
    font=("Arial", 14, "bold"),
    bg="#C7A5FD",
    fg="#521F66"
).pack(pady=20)

# ── Scale ───────────────────────────────────────────────
var_energia = tk.DoubleVar(value=50)

scale = tk.Scale(
    janela,
    variable=var_energia,
    from_=0,
    to=100,
    resolution=1,
    orient="horizontal",
    length=280,
    label="Energia (%)",
    font=("Arial", 10),
    bg="#C7A5FD",
    fg="#521F66",
    troughcolor="#BC6EF0",
    activebackground="#2E86C1"
)
scale.pack(pady=10)

# ── Função ───────────────────────────────────────────────
def mostrar():
    valor = var_energia.get()

    if valor < 30:
        estado = "😴 Cansado"
    elif valor < 70:
        estado = "🙂 Calmo"
    else:
        estado = "🐶 Muito ativo!"

    label_resultado.config(
        text=f"{estado} — Energia: {int(valor)}%"
    )

# ── Label resultado ──────────────────────────────────────
label_resultado = tk.Label(
    janela,
    text="🙂 Calmo — Energia: 50%",
    font=("Arial", 12),
    bg="#C7A5FD",
    fg="#521F66"
)
label_resultado.pack(pady=10)

# ── Botão ────────────────────────────────────────────────
tk.Button(
    janela,
    text="Ver Energia do Pet",
    command=mostrar,
    bg="#BD5CFD",
    fg="#521F66",
    font=("Arial", 11, "bold"),
    width=18,
    relief="flat",
    cursor="hand2"
).pack(pady=8)

# ── Rodar ────────────────────────────────────────────────
janela.mainloop()