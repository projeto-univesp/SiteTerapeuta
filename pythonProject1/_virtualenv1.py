from ast import While
import time
import pyotp
import qrcode
import customtkinter
from tkinter import *
from tkinter import messagebox
import sqlite3


janela = customtkinter.CTk()

class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()


    def tema(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

    def tela(self):
        janela.geometry("700x400")
        janela.title("TELA DE LOGIN")
        janela.resizable(False, False)

    def tela_login(self):
        login_frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label = customtkinter.CTkLabel(master=login_frame, text='ENTRE COM O USUARIO')
        label.place(x=25, y=50)


        usuario_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="Nome do Usuario", width=300,).place(x=25, y=105)
        usuario_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="Usuario", width=300,).place(x=25, y=105)
        usuario_label = customtkinter.CTkLabel(master=login_frame, text="*Por Favor Insira o Nome do usuario."). place(x=25, y=135)

        senha_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="SENHA", width=300, show="*").place(x=25, y=175)
        senha_label = customtkinter.CTkLabel(master=login_frame, text="*Por Favor Insira a sua senha."). place(x=25, y=205)



        def tela_cadastro():
            login_frame.pack_forget()
            #tela cadastro

            rg_frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)
            label = customtkinter.CTkLabel(master=rg_frame, text='TELA DE CADASTRO')
            label.place(x=25, y=50)

            usuario_entry = customtkinter.CTkEntry(master=rg_frame, placeholder_text="NOME DO USUARIO",
                                                   width=300, ).place(x=25, y=95)
            senha_label = customtkinter.CTkLabel(master=rg_frame, text="*Digite seu usuario.").place(x=25,
                                                                                                               y=125)
            senha_entry = customtkinter.CTkEntry(master=rg_frame, placeholder_text="DIGITE A SUA SENHA", width=300,
                                                 show="*").place(x=25, y=160)
            senha_label = customtkinter.CTkLabel(master=rg_frame, text="*Por Favor insira a sua senha.").place(x=25,
                                                                                                               y=190)
            senha_entry = customtkinter.CTkEntry(master=rg_frame, placeholder_text="REPITA A SUA SENHA", width=300,
                                                 show="*").place(x=25, y=220)
            senha_label = customtkinter.CTkLabel(master=rg_frame, text="*Por Favor repita a sua senha.").place(x=25,y=250)



            def back():
            #retorno tela inicial

                rg_frame.pack_forget()

                login_frame.pack(side=RIGHT)

                pass

            back_button = customtkinter.CTkButton(master=rg_frame, text="VOLTAR", width=80,
                                                   command=back).place(x=150, y=300)
            def save_user():


                msg = messagebox.showinfo(title="CADASTRO", message="USUARIO CADASTRADO COM SUCESSO")
                pass
            save_button = customtkinter.CTkButton(master=rg_frame, text="CADASTRAR", width=80, command=save_user).place(x=25, y=300)


            pass

        cadastro_button = customtkinter.CTkButton(master=login_frame, text="CADASTRE-SE", width=80, command=tela_cadastro).place(x=25, y=250)

        def tela_codigo():
            #tela verificação de 2 etapas
            login_frame.pack_forget()
            rg_frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)
            label = customtkinter.CTkLabel(master=rg_frame, text='CODIGO DE VERIFICAÇÃO')
            label.place(x=25, y=50)
            senha_label = customtkinter.CTkLabel(master=rg_frame, text="*Digite seu codigo de verificação.").place(x=25,
                                                                                                     y=125)
            usuario_entry = customtkinter.CTkEntry(master=rg_frame, placeholder_text="CODIGO DE VERIFICAÇÃO",
                                                   width=300, ).place(x=25, y=95)

            #retornar a tela inicial tela de codigo
            def back():
                rg_frame.pack_forget()

                login_frame.pack(side=RIGHT)

                pass

            back_button = customtkinter.CTkButton(master=rg_frame, text="VOLTAR", width=80,
                                                  command=back).place(x=180, y=160)

            def save_user():
                msg = messagebox.showinfo(title="BEM VINDO", message="OLÁ!!!!!  SEJA BEM VINDO")
                pass

            save_button = customtkinter.CTkButton(master=rg_frame, text="VERIFICAR COD.", width=80, command=save_user).place(
                x=25, y=160)

            pass



        entrar_button = customtkinter.CTkButton(master=login_frame, text="ENTRAR", width=80, command=tela_codigo).place(x=180, y=250)

Application()






