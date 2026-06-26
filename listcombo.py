import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("☕ Café com Patas")
janela.geometry("520x500")
janela.configure(bg="#F8E8D8")


tk.Label(
    janela,
    text="☕🐾 Café com Patas",
    font=("Arial", 18, "bold"),
    bg="#F8E8D8",
    fg="#6B3E26"
).pack(pady=15)


tk.Label(
    janela,
    text="Escolha sua bebida:",
    bg="#F8E8D8",
    font=("Arial", 12)
).pack()

combo = ttk.Combobox(
    janela,
    values=[
        "☕ Café Expresso",
        "🥛 Cappuccino",
        "🍫 Chocolate Quente",
        "🫖 Chá",
        "🧋 Café Gelado"
    ],
    state="readonly",
    width=25
)
combo.pack(pady=10)


tk.Label(
    janela,
    text="Escolha um pet para visitar:",
    bg="#F8E8D8",
    font=("Arial", 12)
).pack()

listbox = tk.Listbox(
    janela,
    width=30,
    height=6,
    font=("Arial", 11)
)

pets = [
    "🐶 Thor",
    "🐶 Mel",
    "🐱 Luna",
    "🐱 Simba",
    "🐶 Bob",
    "🐱 Nina"
]

for pet in pets:
    listbox.insert(tk.END, pet)

listbox.pack(pady=10)


def confirmar():
    bebida = combo.get()

    if bebida == "":
        messagebox.showwarning(
            "Atenção",
            "Escolha uma bebida!"
        )
        return

    indice = listbox.curselection()

    if not indice:
        messagebox.showwarning(
            "Atenção",
            "Escolha um pet!"
        )
        return

    pet = listbox.get(indice[0])

    messagebox.showinfo(
        "Pedido Confirmado",
        f"☕ Bebida: {bebida}\n\n"
        f"🐾 Pet escolhido: {pet}\n\n"
        "Seu pedido foi registrado!\n"
        "Aproveite um momento especial no Café com Patas. 💜"
    )


tk.Button(
    janela,
    text="✅ Confirmar Pedido",
    command=confirmar,
    bg="#8B5E3C",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=20)


frame = tk.Frame(
    janela,
    bg="#F3D8C7",
    padx=15,
    pady=10
)
frame.pack(fill="x", padx=20)

tk.Label(
    frame,
    text="🐾 No Café com Patas você pode relaxar enquanto conhece nossos animais.",
    bg="#F3D8C7",
    fg="#6B3E26",
    font=("Arial", 10, "bold"),
    wraplength=450,
    justify="left"
).pack(anchor="w")


tk.Label(
    janela,
    text="☕💜 Café com Patas • Onde café, carinho e adoção se encontram.",
    bg="#F8E8D8",
    fg="#6B3E26",
    font=("Arial", 9, "italic")
).pack(side="bottom", pady=10)

janela.mainloop()
