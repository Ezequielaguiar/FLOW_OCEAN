import customtkinter as ctk 
from PIL import Image
from pathlib import Path
import tkinter as tk
from tkinter import StringVar
from tkinter import filedialog
from tkinter import messagebox
from Lista_roteiros import lista_roteiros
import pyautogui
import os



ctk.set_default_color_theme('dark-blue')

class janela(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1920X1080')
        self.state("zoomed")
        self._set_appearance_mode('Dark')
        self.resizable(False,True)
        self.minsize(1366,768)
        self.maxsize(1366,768)
        self.title('RPA OCEAN')
        self.configura_planofundo()
        self.label = ctk.CTkLabel(master=self,image=self.image,text='')
        self.label.pack(fill=tk.BOTH,expand=True)
        #Inicia widgets
        self.variaveis()
        self.input_usuario()
        self.imagens_widgets()
        self.button()
        self.enviar_email()
        
    def configura_planofundo(self):
        caminho = Path('imagens','Fundo6.png')
        self.image = ctk.CTkImage(light_image=Image.open(str(caminho)),dark_image=Image.open(str(caminho)),size=(1366,768))
 
    def esconder_senha(self):
        if self.senha.cget('show') == '*':
            self.senha.configure(show='')
            abrir_imagen_olho = Path('imagens','olho_fechado.png')
        else:
            self.senha.configure(show='*') 
            abrir_imagen_olho = Path('imagens','olho.png')
        self.image_olho = ctk.CTkImage(light_image=Image.open(str(abrir_imagen_olho)),size=(50,50))
        self.abrir_senha.configure(image=self.image_olho) 

    def variaveis(self):
        self.text_usuario =  StringVar() 
        self.text_mes =  StringVar() 
        self.text_ano =  StringVar() 
        self.text_senha =  StringVar() 
        
    def input_usuario(self):
        self.usuario = ctk.CTkEntry(self.label,width=550,height=80,font=('segoe UI', 20), text_color='#002055', bg_color='#D9D9D9', fg_color='#D9D9D9', border_color='#D9D9D9')
        self.usuario.place(x=800,y=200)
        self.usuario.insert(0,'Usuario')
        self.mes = ctk.CTkEntry(self.label,textvariable=self.text_mes,width=254,height=80,font=('segoe UI', 20), text_color='#002055', bg_color='#D9D9D9', fg_color='#D9D9D9', border_color='#D9D9D9')
        self.mes.place(x=800,y=300)
        self.mes.insert(0,'Mês')
        self.ano = ctk.CTkEntry(self.label,textvariable=self.text_ano , width=254,height=80,font=('segoe UI', 20), text_color='#002055', bg_color='#D9D9D9', fg_color='#D9D9D9', border_color='#D9D9D9')
        self.ano.place(x=1095,y=300)
        self.ano.insert(0,'Ano')
        self.senha = ctk.CTkEntry(self.label,textvariable=self.text_senha,width=550,height=80,show='*',font=('segoe UI', 20), text_color='#002055', bg_color='#D9D9D9', fg_color='#D9D9D9', border_color='#D9D9D9')
        self.senha.place(x=800,y=400)
        self.senha.insert(0,'Senha')
        
    def importar_base(self):
        self.selecionar_arquivo = filedialog.askopenfilename()
        if self.selecionar_arquivo != '':
            messagebox.showinfo('Importar Arquivo','Arquivo importado com sucesso')
        else:
            messagebox.showerror('Importar Arquivo','Erro \nArquivo não foi selecionado')
        print(self.selecionar_arquivo)
        
    def cancelar(self):
        self.destroy()
    
    def imagens_widgets(self):
        abrir_imagen_usuario = Path('imagens','Pessoa.png')
        print(abrir_imagen_usuario)
        image_usuario = ctk.CTkImage(light_image=Image.open(str(abrir_imagen_usuario)),size=(50,50))
        label_imagem_usuario = ctk.CTkLabel(self.label,image=image_usuario,width=50,height=50,text='',bg_color='white',fg_color='white')
        label_imagem_usuario.place(x=750,y=210)
        abrir_imagen_olho_aberto = Path('imagens','olho.png')
        self.image_olho = ctk.CTkImage(light_image=Image.open(str(abrir_imagen_olho_aberto)),size=(50,50))
        abrir_cadeado = Path('imagens','Cadeado.png')
        cadeado = ctk.CTkImage(light_image=Image.open(str(abrir_cadeado)),dark_image=Image.open(str(abrir_cadeado)),size=(50,50))
        label_cadeado = ctk.CTkLabel(self.label,width=50,height=50,image=cadeado,bg_color='white',fg_color='white',text='')
        label_cadeado.place(x=750,y=420)
        
    def button(self):
        inserir_arquivo = ctk.CTkButton(self.label,width=168,height=80,text='Selecionar base',command=self.importar_base,font=('arial bold',14),text_color='#1A3EB5',fg_color='#5596FF',bg_color='white',border_color='blue',hover_color="#4FDDF0",corner_radius=10)
        inserir_arquivo.place(x=800,y=540)
        ligar = ctk.CTkButton(self.label,width=168,height=80,command=self.iniciar_codigo,text='Ligar',font=('arial bold',14),text_color='#5596FF',fg_color='#1A3EB5',bg_color='white',border_color='blue',hover_color="#4FDDF0",corner_radius=10)
        ligar.place(x=990,y=540)
        cancelar = ctk.CTkButton(self.label,width=168,height=80,text='Cancelar',command=self.cancelar,font=('arial bold',14),text_color='#181818',fg_color='#AACAFF',bg_color='white',border_color='black',hover_color="#4FDDF0",corner_radius=10)
        cancelar.place(x=1180,y=540)
        self.abrir_senha = ctk.CTkButton(self.label,image=self.image_olho,command=self.esconder_senha,text='', bg_color='#D9D9D9', fg_color='#D9D9D9',width=50,height=50)
        self.abrir_senha.place(x=1280,y=410)
    
    def dialog_email(self):
        email_notificacao = ctk.CTkInputDialog(title='Notificação',text='Inserir E-mail para ser notificado')
        self.email_para_receber_notificacao = email_notificacao.get_input()
        if self.email_para_receber_notificacao != '':
            pass
        else:
            self.selecionar_email.deselect()
        
    def enviar_email(self):
        self.selecionar_email = ctk.CTkCheckBox(self.label, command=self.dialog_email,checkbox_width=25, checkbox_height=25, onvalue=True, offvalue=False, text='Deseja receber notificação.',font=('segoe UI', 20), text_color='#002055',bg_color='white',fg_color='#002055',checkmark_color = '#D9D9D9')
        self.selecionar_email.place(x=800,y=495)
        
    def iniciar_codigo(self):
        usuario_ocean = self.usuario.get()
        senha_ocean = self.senha.get()
        mes = self.mes.get()
        ano = self.ano.get()
        base = self.selecionar_arquivo
        remetente = self.usuario.get()
        destinatario = self.email_para_receber_notificacao
        caminho_arquivo_loop = Path('ARQUIVO_LOOP','Empresa.txt')
        with open(caminho_arquivo_loop,'w') as Empresa:
            zerar_empresa = Empresa.write('0')
        print(zerar_empresa)

        if usuario_ocean and senha_ocean and mes and ano and base :
            # try:
            temporario = lista_roteiros(usuario_ocean,senha_ocean,mes,ano,base,remetente,destinatario)
            # except:
            # print('Deu erro')
            # print_tela = pyautogui.screenshot()
            # print_tela.save('Print_erro.png')
            # os.system("taskkill /im chrome.exe /f")
            # self.reiniciar()
        else:
            messagebox.showerror('Erro','Preecha as informações corretamente')
        messagebox.showinfo(title='Concluido',message='RPA_OCEAN finalizado')
        
    def reiniciar(self):
        self.iniciar_codigo()
        
App = janela()
App.mainloop()