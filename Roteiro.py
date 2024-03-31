from Lista_roteiros import lista_roteiros
import os
import pyautogui


class executar():
    def __init__(self):
        self.iniciar_codigo()
        
    def iniciar_codigo(self):
        try:
            temporario = lista_roteiros('usuario', 'senha','mes','ano','base','remetente','destinatario')
        except:
            print('Deu erro')
            print_tela = pyautogui.screenshot()
            print_tela.save('Print_erro.png')
            os.system("taskkill /im chrome.exe /f")
            self.reiniciar()
    
    def reiniciar(self):
        self.iniciar_codigo()


iniciar = executar()