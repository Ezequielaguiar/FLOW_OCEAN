# Importação das classes necessárias
from Login import Login_Ocean
from dados import BaseDados_tratamentos
from Cards import Banco_card
from parametros_card import configurar_card
from compartilhar import Compartilhar_esteira
import time
import pandas as pd
from Enviar_Email import email

class lista_roteiros:
    def __init__(self,usuario, senha,mes,ano,base,remetente,destinatario):
        print('Iniciar')
        self.usuario = usuario
        self.senha = senha
        self.mes = mes
        self.ano = ano
        self.base = base
        self.remetente = remetente
        self.destinatario = destinatario
        print(usuario)
        self.Etapa0()
        


    def Etapa0(self):
        # Inicialização e tratamento dos dados do SQL e Excel
        self.iniciar_dados = BaseDados_tratamentos()  
        self.iniciar_dados.importar_dados_sql()  # Importa dados do SQL
        self.iniciar_dados.importar_dados_excel(self.base)  # Importa dados do Excel
        self.mes_ano = self.iniciar_dados.definir_data(self.mes,self.ano)  # Define o mês e o ano
        self.dados = self.iniciar_dados.tratar_dados()  # Trata os dados
        self.Etapa1()

    def Etapa1(self):
        # Inicialização do processo de login
        self.iniciar_login = Login_Ocean(self.usuario,self.senha)
        self.iniciar_login.abrir_navegador()
        self.iniciar_login.link1()
        self.iniciar_login.faz_login()  # Realiza o login
        self.iniciar_login.link2() # Acessa o link 2
        self.driver = self.iniciar_login.entrar_ocean()  # Entra na aplicação Ocean
        self.Etapa2()
    
    def Etapa2(self):
        # Coleta de atributos relacionados ao Ocean
        atributos_ocean = self.iniciar_dados.itens_trabalho()
        self.sigla = atributos_ocean['SIGLA']
        self.nome_card = atributos_ocean['NOME_CARD']
        self.cod_versao = atributos_ocean['COD_VERSAO_PXR']
        self.modalidade = atributos_ocean['MODALIDADE']
        self.e_mail = atributos_ocean['E-MAIL']
        self.compartilhar_esteira = atributos_ocean['COMPARTILHAR_ESTEIRA']
        print('Terminou a 3')
        self.Etapa3()
 
    def Etapa3(self):       
        # Inicialização das classes relacionadas aos cards, parâmetros e compartilhamento
        self.iniciar_banco_card = Banco_card(self.driver)
        print('saiu do banco card')
        self.iniciar_parametros = configurar_card(self.driver)
        self.iniciar_compartilhamento = Compartilhar_esteira(self.driver)
        self.Etapa5()
    
    def Etapa4(self,i,datafreme):
        print('Entrou na Etapa 4 criação do dataframe')
        if datafreme == 0  :
            print('Saiu da criação datafreme zerado')
            return False
        else:
            print('Entrou na criação do dataframe')
            print(f'Aqui é o item da esteira a ser criado uma lista e compartilhar : {self.compartilhar_esteira[i]}')    
            lista_compartilhar_esteira = datafreme.split(';')
            self.df_lista_compartilhar_esteira = pd.DataFrame(lista_compartilhar_esteira,columns=['Nome_esteira'])
            print(f'Meu Datafreme é {self.df_lista_compartilhar_esteira}')
            return True
               
    def Etapa5(self):
        # Loop sobre os atributos relacionados aos cards
        with open(r'.\ARQUIVO_LOOP\Empresa.txt') as arquivo:
            i = int(arquivo.read())
        while i < len(self.sigla):
            
            print(self.nome_card[i])
            self.iniciar_banco_card.pesquisar_item(self.sigla[i])  # Pesquisa o item no banco de dados
            self.iniciar_banco_card.tem_banco_card(self.nome_card[i])  # Verifica se o card já existe
            
            if self.iniciar_banco_card.verificar_se_existe_card(self.cod_versao[i]):  # Verifica se o card já existe
                print('Entrou verificação de card card')
            else:
                print('Saiu verificar card')
                self.iniciar_banco_card.card_selecionado(self.cod_versao[i])  # Seleciona o card
            
            if self.iniciar_parametros.verificar_se_existe_modelo():  # Verifica se o templete existe
                print('Entrou verificar modelo')
            else: 
                print(self.modalidade[i])
                self.iniciar_parametros.selecionar_templete(self.modalidade[i])  # Seleciona o template
                
            if self.iniciar_parametros.verificar_se_existe_email():  # Verifica se o e_mail existe
                print('Entrou verificar Email')
            else:                        
                self.iniciar_parametros.email_analista(self.e_mail[i])  # Insere o e-mail do analista
            
            if self.iniciar_parametros.verificar_se_existe_tag(self.mes_ano):  # Verifica se o teg existe
                print('Entrou verificar Tag')
            else:                       
                self.iniciar_parametros.inserir_tags(self.mes_ano)  # Insere as tags
            print('Compartilhamento')
            
            if self.Etapa4(i,self.compartilhar_esteira[i]):
                self.iniciar_compartilhamento.compartilhar(self.df_lista_compartilhar_esteira)  # Compartilha o card na esteira
            print('Terminou de compartilhar esteira')
            with open(r'.\ARQUIVO_LOOP\Empresa.txt','w') as arquivo:
                arquivo.write(str((i+1)))
            i += 1 
            self.iniciar_login.alterar_link(self.driver)
        self.iniciar_login.fechar_navegador(self.driver)
        self.Etapa6()

    def Etapa6(self):
        self.iniciar_enviar_email = email(self.remetente,self.senha,self.destinatario)


