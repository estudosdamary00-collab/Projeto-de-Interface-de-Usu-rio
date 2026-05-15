import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


class GothicApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("dark elegance")
        self.geometry("500x500")
        self.configure(bg="#000000")

        # CORES
        self.bg_color = "#000000"
        self.accent_color = "#4B001F"
        self.btn_active = "#720026"
        self.text_color = "#EAEAEA"

        # =========================
        # TÍTULO
        # =========================

        title = tk.Label(
            self,
            text="midnight society",
            font=("Georgia", 28, "bold"),
            bg=self.bg_color,
            fg="#C9C9C9"
        )
        title.pack(pady=40)

        # SUBTÍTULO
        subtitle = tk.Label(
            self,
            text="enter the shadows and embrace your essence.",
            font=("Georgia", 11, "italic"),
            bg=self.bg_color,
            fg="#8A8A8A"
        )
        subtitle.pack(pady=5)

        # =========================
        # FORMULÁRIO
        # =========================

        form_frame = tk.Frame(self, bg=self.bg_color)
        form_frame.pack(pady=40)

        # CAMPO NOME
        self.ent_nome = tk.Entry(
            form_frame,
            font=("Georgia", 12),
            bg="#1A1A1A",
            fg="white",
            insertbackground="white",
            relief="flat",
            width=30
        )
        self.ent_nome.pack(pady=10, ipady=10)

        # CAMPO EMAIL
        self.ent_email = tk.Entry(
            form_frame,
            font=("Georgia", 12),
            bg="#1A1A1A",
            fg="white",
            insertbackground="white",
            relief="flat",
            width=30
        )
        self.ent_email.pack(pady=10, ipady=10)

        # =========================
        # BOTÃO
        # =========================

        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(pady=20)

        # HOVER
        def on_enter(e):
            self.btn_submit.config(bg=self.btn_active)

        def on_leave(e):
            self.btn_submit.config(bg=self.accent_color)

        self.btn_submit = tk.Button(
            btn_frame,
            text="join the darkness",
            font=("Georgia", 12, "bold"),
            bg=self.accent_color,
            fg="#FFFFFF",
            activebackground=self.btn_active,
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.submit
        )

        self.btn_submit.pack(fill="x", ipady=12)

        self.btn_submit.bind("<Enter>", on_enter)
        self.btn_submit.bind("<Leave>", on_leave)

        # =========================
        # IMAGEM
        # =========================

        # pega automaticamente a pasta do script
        pasta_atual = os.path.dirname(__file__)

        # caminho da imagem
        caminho_imagem = os.path.join(
            pasta_atual,
            "gato.jpg"
        )

        # abre a imagem
        img = Image.open(caminho_imagem)

        # redimensiona
        img = img.resize((140, 140))

        # converte para tkinter
        self.gato_img = ImageTk.PhotoImage(img)

        # label da imagem
        img_label = tk.Label(
            self,
            image=self.gato_img,
            bg=self.bg_color,
            borderwidth=0
        )

        # posição no canto inferior direito
        img_label.place(
            relx=1.0,
            rely=1.0,
            anchor="se",
            x=-20,
            y=-20
        )

        # =========================
        # RODAPÉ
        # =========================

        footer = tk.Label(
            self,
            text="© 2026 dark muse collective.",
            font=("Georgia", 9),
            bg=self.bg_color,
            fg="#5A5A5A"
        )

        footer.pack(side="bottom", pady=30)

    # =========================
    # FUNÇÃO DO BOTÃO
    # =========================

    def submit(self):
        nome = self.ent_nome.get()
        email = self.ent_email.get()

        if not nome or not email:
            messagebox.showwarning(
                "the void calls...",
                "preencha todos os campos para continuar.",
                parent=self
            )
            return

        messagebox.showinfo(
            "as sombras te recebem...",
            f"bem-vindo(a), {nome}.\nlogo enviaremos mensagens para {email}.",
            parent=self
        )

        # limpa campos
        self.ent_nome.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)

        # foco no nome
        self.ent_nome.focus()


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    app = GothicApp()
    app.mainloop()