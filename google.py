import tkinter as tk
import random


class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Pesquisa Maria")
        self.geometry("800x600")
        self.configure(bg="#ffa6dd")
        self.minsize(400, 300)

        # 🎀 Aleatórios pela tela
        for i in range(20):
            x = random.randint(20, 750)
            y = random.randint(20, 550)

            lbl = tk.Label(
                self,
                text='🎀 ',
                font=('Arial', 20),
                bg="#ffa6dd"
            )
            lbl.place(x=x, y=y)

        # Container principal
        main_frame = tk.Frame(self, bg="#ffa6dd")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # --- Título ---
        title_frame = tk.Frame(main_frame, bg="#ffa6dd")
        title_frame.pack(pady=(0, 30))

        colors = [
            "#955097", "#FF5BFF", "#FF88EF",
            "#E958BD", "#FF45E6"
        ]

        text = "Maria"

        for i, char in enumerate(text):
            tk.Label(
                title_frame,
                text=char,
                font=("Georgia", 56, "bold"),
                fg=colors[i],
                bg="#ffa6dd"
            ).pack(side="left")

        # --- Barra de Pesquisa ---
        search_frame = tk.Frame(
            main_frame,
            bg="#ffffff",
            bd=1,
            relief="solid"
        )
        search_frame.pack(ipadx=10, ipady=5, fill="x")

        # Ícone lupa
        search_icon = tk.Label(
            search_frame,
            text="🔍",
            bg="#ffffff",
            font=("Arial", 14)
        )
        search_icon.pack(side="left", padx=(10, 5))

        # Placeholder
        self.placeholder_text = "digite sua dúvida"

        self.search_var = tk.StringVar()

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 14),
            width=40,
            bd=0,
            bg="#ffffff",
            fg="grey"
        )

        self.search_entry.pack(side="left", padx=5, pady=5)
        self.search_entry.insert(0, self.placeholder_text)

        # Ícone microfone
        mic_icon = tk.Label(
            search_frame,
            text="🎤",
            bg="#ffffff",
            font=("Arial", 14)
        )
        mic_icon.pack(side="right", padx=(5, 10))

        # Eventos
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)

        # --- Botões ---
        buttons_frame = tk.Frame(main_frame, bg="#ffa6dd")
        buttons_frame.pack(pady=30)

        search_button = tk.Button(
            buttons_frame,
            text="Pesquisar",
            font=("Arial", 11),
            bg="#f8f9fa",
            relief="flat",
            padx=15,
            pady=8,
            command=self.perform_search
        )
        search_button.pack(side="left", padx=10)

        lucky_button = tk.Button(
            buttons_frame,
            text="Estou com sorte",
            font=("Arial", 11),
            bg="#f8f9fa",
            relief="flat",
            padx=15,
            pady=8
        )
        lucky_button.pack(side="left", padx=10)

    # ==========================
    # FUNÇÕES
    # ==========================

    def on_entry_click(self, event):
        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="black")

    def on_focus_out(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg="grey")

    def perform_search(self, event=None):
        query = self.search_entry.get()

        if query and query != self.placeholder_text:
            print(f"Buscando por: {query}")


# ==========================
# EXECUÇÃO
# ==========================

if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()