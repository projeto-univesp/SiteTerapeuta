import tkinter as tk
from tkinter import messagebox
import pyotp
import qrcode

def login():
    login = login_entry.get()
    senha = senha_entry.get()

    if not login or not senha:
        messagebox.showerror("Erro de Entrada", "Por favor, insira o usuário e a senha.")
    else:
        with open('registrados.txt') as arq:
            registrados = arq.readlines()
            if f"{login}{senha}\n" in registrados:
                root.withdraw()  # Fecha a janela de autenticação
                abrir_tela_verificacao(login, senha)  # Abre a janela de verificação
            else:
                messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")

def abrir_tela_cadastro():
    root.withdraw()  # Fecha a janela principal
    cadastro_window = tk.Toplevel(root)  # Define a janela principal
    cadastro_window.title("Cadastro")
    cadastro_window.geometry("350x250")  # Definindo o tamanho da janela

    cadastro_login_label = tk.Label(cadastro_window, text="Login:")
    cadastro_login_label.grid(row=0, column=0, padx=5, pady=5)
    cadastro_login_entry = tk.Entry(cadastro_window)
    cadastro_login_entry.grid(row=0, column=1, padx=5, pady=5)

    cadastro_senha_label = tk.Label(cadastro_window, text="Senha:")
    cadastro_senha_label.grid(row=1, column=0, padx=5, pady=5)
    cadastro_senha_entry = tk.Entry(cadastro_window, show="*")
    cadastro_senha_entry.grid(row=1, column=1, padx=5, pady=5)


    comentario_label = tk.Label(cadastro_window, text="Antes realizar seu cadastro:\n1. Entre em sua loja de aplicativos.\n2. Baixe um autenticador de segurança.\n3. Após clicar em cadastrar, escaneie o QR code.\nOBS: Após isso, será gerado um código a \ncada 30 segundos para a nossa segurança.")
    comentario_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    cadastrar_button = tk.Button(cadastro_window, text="Cadastrar", command=lambda: cadastrar(cadastro_window, cadastro_login_entry.get(), cadastro_senha_entry.get()))
    cadastrar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    voltar_button = tk.Button(cadastro_window, text="Voltar", command=lambda: voltar_tela_autenticacao(cadastro_window))
    voltar_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

def cadastrar(cadastro_window, login, senha):
    if not login or not senha:
        messagebox.showerror("Erro de Entrada", "Por favor, insira o usuário e a senha.")
    else:
        with open('registrados.txt') as arq:
            registrados = arq.readlines()
            if f"{login}{senha}\n" in registrados:
                messagebox.showerror("Erro de Cadastro", "Usuário já em uso, por favor, tente outro nome!")
            else:
                with open('registrados.txt', 'a') as arq:
                    arq.write(f"{login}{senha}\n")
                messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
                exibir_qrcode_apos_cadastro()
                cadastro_window.destroy()
                root.deiconify()  # Reexibe a janela principal

def exibir_qrcode_apos_cadastro():
    qr_code_window = tk.Toplevel(root)
    qr_code_window.title("QR Code após Cadastro")
    qr_code_window.geometry("300x300")  # Definindo o tamanho da janela

    # Gerar e salvar o QR Code
    chave_mestre = "O7SP6KFFQTPBWMYR3HCSR52QXWX44CHN"
    link = pyotp.TOTP(chave_mestre).provisioning_uri(name="will", issuer_name="PI")
    meu_qrcode = qrcode.make(link)
    meu_qrcode.save("qrcode.png")

    # Carregar a imagem do QR Code
    qr_code_image = tk.PhotoImage(file="qrcode.png")

    # Exibir a imagem do QR
    qr_code_label = tk.Label(qr_code_window, image=qr_code_image)
    qr_code_label.image = qr_code_image
    qr_code_label.pack()

def abrir_tela_verificacao(login, senha):
    verificacao_window = tk.Toplevel(root)  # Define a janela principal
    verificacao_window.title("Verificação de Código")
    verificacao_window.geometry("300x150")  # Definindo o tamanho da janela

    codigo_label = tk.Label(verificacao_window, text="Código de Verificação:")
    codigo_label.grid(row=0, column=0, padx=5, pady=5)
    codigo_entry = tk.Entry(verificacao_window, show="*")
    codigo_entry.grid(row=0, column=1, padx=5, pady=5)

    verificar_button = tk.Button(verificacao_window, text="Verificar", command=lambda: verificar_codigo(verificacao_window, login, senha, codigo_entry.get()))
    verificar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    voltar_button = tk.Button(verificacao_window, text="Voltar", command=lambda: voltar_tela_autenticacao(verificacao_window))
    voltar_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

def voltar_tela_autenticacao(window=None):
    if window:
        window.destroy()
    root.deiconify()  # Reexibe a janela principal

def verificar_codigo(verificacao_window, login, senha, codigo_usuario):
    chave_mestre = "O7SP6KFFQTPBWMYR3HCSR52QXWX44CHN"
    with open('registrados.txt') as arq:
        registrados = arq.readlines()
        if f"{login}{senha}\n" in registrados:
            codigo = pyotp.TOTP(chave_mestre)
            if codigo.verify(codigo_usuario):
                messagebox.showinfo("Login", "SEJA BEM VINDO!!")
            else:
                messagebox.showerror("Erro de Verificação", "CÓDIGO DE VERIFICAÇÃO INCORRETO, INICIE O LOGIN NOVAMENTE")
        else:
            messagebox.showerror("Erro de Verificação", "Usuário ou Senha Incorretos!")

root = tk.Tk()
root.title("Sistema de Autenticação")
root.geometry("300x150")  # Definindo o tamanho da janela

# Ajustando a aparência dos widgets para simular o estilo do Windows
root.option_add('*Font', 'Verdana 8')
root.option_add('*Button*font', 'Verdana 8 bold')
root.option_add('*Label*font', 'Verdana 8 bold')
root.option_add('*Entry*font', 'Verdana 8')

login_label = tk.Label(root, text="Login:")
login_label.grid(row=0, column=0, padx=5, pady=5)
login_entry = tk.Entry(root)
login_entry.grid(row=0, column=1, padx=5, pady=5)

senha_label = tk.Label(root, text="Senha:")
senha_label.grid(row=1, column=0, padx=5, pady=5)
senha_entry = tk.Entry(root, show="*")
senha_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

cadastro_button = tk.Button(root, text="Cadastrar", command=abrir_tela_cadastro)
cadastro_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()



