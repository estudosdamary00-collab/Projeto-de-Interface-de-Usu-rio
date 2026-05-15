
import tkinter as tk
from tkinter import ttk, messagebox


class AppVeterinario(tk.Tk):
    def __init__(self):
        super().__init__()

        # =========================
        # CONFIGURAÇÕES DA JANELA
        # =========================
        self.title("Clínica Veterinária")
        self.geometry("950x680")
        self.configure(bg="#ED92FF")
        self.resizable(False, False)

        # =========================
        # PALETA DE CORES
        # =========================
        self.bg_color = "#E29CFD"
        self.fg_color = "#FFFFFF"
        self.accent_color = "#AC79E2"
        self.input_bg = "#3C0F52"
        self.border_color = "#B387D1"
        self.text_muted = "#260A31"

        # =========================
        # ESTILO COMBOBOX
        # =========================
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.input_bg,
            background=self.input_bg,
            foreground=self.fg_color,
            bordercolor=self.border_color,
            arrowcolor=self.accent_color,
            padding=5
        )

        self.create_widgets()

    def create_widgets(self):

        # =========================
        # CABEÇALHO
        # =========================
        header_frame = tk.Frame(self, bg=self.bg_color)
        header_frame.pack(fill="x", pady=(40, 20))

        title = tk.Label(
            header_frame,
            text="🐾 SISTEMA VETERINÁRIO 🐾",
            font=("Segoe UI", 14, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title.pack()

        subtitle = tk.Label(
            header_frame,
            text="CADASTRO DE PACIENTES",
            font=("Segoe UI", 32, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle.pack()

        separator = tk.Frame(
            header_frame,
            bg=self.accent_color,
            height=2,
            width=150
        )
        separator.pack(pady=(10, 0))

        # =========================
        # FORMULÁRIO
        # =========================
        form_frame = tk.Frame(self, bg=self.bg_color)
        form_frame.pack(expand=True, fill="both", padx=100)

        def create_input(parent, label_text, row, col, width=30):

            lbl = tk.Label(
                parent,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg=self.bg_color,
                fg=self.text_muted
            )

            lbl.grid(
                row=row,
                column=col,
                sticky="w",
                pady=(15, 0),
                padx=15
            )

            entry = tk.Entry(
                parent,
                font=("Segoe UI", 13),
                bg=self.input_bg,
                fg=self.fg_color,
                insertbackground=self.accent_color,
                relief="flat",
                width=width,
                highlightthickness=1,
                highlightbackground=self.border_color,
                highlightcolor=self.accent_color
            )

            entry.grid(
                row=row + 1,
                column=col,
                sticky="we",
                pady=(5, 5),
                padx=15,
                ipady=8
            )

            return entry

        # =========================
        # CAMPOS
        # =========================
        self.ent_tutor = create_input(
            form_frame,
            "NOME DO TUTOR",
            0, 0,
            width=35
        )

        self.ent_pet = create_input(
            form_frame,
            "NOME DO PET",
            0, 1,
            width=25
        )

        self.ent_raca = create_input(
            form_frame,
            "RAÇA",
            2, 0,
            width=35
        )

        self.ent_telefone = create_input(
            form_frame,
            "TELEFONE",
            2, 1,
            width=25
        )

        # =========================
        # ESPÉCIE
        # =========================
        lbl_especie = tk.Label(
            form_frame,
            text="ESPÉCIE",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_color,
            fg=self.text_muted
        )

        lbl_especie.grid(
            row=4,
            column=0,
            sticky="w",
            pady=(15, 0),
            padx=15
        )

        self.combo_especie = ttk.Combobox(
            form_frame,
            values=[
                "Cachorro",
                "Gato",
                "Coelho",
                "Ave",
                "Hamster",
                "Outro"
            ],
            font=("Segoe UI", 12),
            state="readonly"
        )

        self.combo_especie.grid(
            row=5,
            column=0,
            sticky="we",
            pady=(5, 5),
            padx=15
        )

        self.combo_especie.set("Cachorro")

        # =========================
        # IDADE
        # =========================
        self.ent_idade = create_input(
            form_frame,
            "IDADE DO PET",
            4, 1,
            width=25
        )

        # Configurar Grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        # =========================
        # BOTÃO
        # =========================
        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(fill="x", pady=(20, 40))

        self.btn_cadastrar = tk.Button(
            btn_frame,
            text="CADASTRAR PACIENTE",
            font=("Segoe UI", 12, "bold"),
            bg=self.accent_color,
            fg="#2C142E",
            activebackground="#31003D",
            activeforeground="#CB4BEB",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=self.cadastrar
        )

        self.btn_cadastrar.pack()

        # Hover
        self.btn_cadastrar.bind(
            "<Enter>",
            lambda e: self.btn_cadastrar.config(bg="#CF55FF")
        )

        self.btn_cadastrar.bind(
            "<Leave>",
            lambda e: self.btn_cadastrar.config(bg=self.accent_color)
        )

        # =========================
        # STATUS
        # =========================
        self.status_lbl = tk.Label(
            self,
            text="",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.accent_color
        )

        self.status_lbl.pack(pady=(10, 0))

    # =========================
    # CADASTRAR
    # =========================
    def cadastrar(self):

        tutor = self.ent_tutor.get()
        pet = self.ent_pet.get()
        especie = self.combo_especie.get()

        if not tutor or not pet:
            messagebox.showwarning(
                "Atenção",
                "Preencha os campos obrigatórios!"
            )
            return

        # Simulação de cadastro
        self.status_lbl.config(
            text="Registrando paciente...",
            fg=self.fg_color
        )

        self.after(
            700,
            lambda: self.finalizar_cadastro(
                tutor,
                pet,
                especie
            )
        )

    # =========================
    # FINALIZAÇÃO
    # =========================
    def finalizar_cadastro(self, tutor, pet, especie):

        self.status_lbl.config(
            text=f"✓ {pet} ({especie}) foi cadastrado com sucesso!",
            fg=self.accent_color
        )

        # Limpar campos
        self.ent_tutor.delete(0, tk.END)
        self.ent_pet.delete(0, tk.END)
        self.ent_raca.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)
        self.ent_idade.delete(0, tk.END)

        self.combo_especie.set("Cachorro")

        self.ent_tutor.focus()


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app = AppVeterinario()
    app.mainloop()

