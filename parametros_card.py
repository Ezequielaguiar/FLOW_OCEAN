from comandos import Comandos_selenium
from selenium.webdriver.common.by import By
import time

class configurar_card(Comandos_selenium):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        self.verificar_modelo = By.XPATH,'//*[@class="sc-bTllmR bxQcJH react-tabs__tab-panel--selected"]//*[contains(text(),"GUC")]'
        self.importar_modelo = By.XPATH,'//div[@id="idChildrenContainer"]//button[@type="submit"]'
        self.aplicar_modelo = By.XPATH,'//*[contains(text(),"Aplicar modelo")]'
        self.mensagem_aplicar_modelo = By.XPATH,'//h5[contains(text(),"Aplicar Modelo")]'
        self.confirmar_modelo = By.XPATH,'//button[contains(text(),"APLICAR")]'
        self.mensagem_aplicar_modelo_sair = By.XPATH,'//div[contains(text(),"Estamos preparando o item de trabalho com o modelo escolhido. Aguarde alguns instantes")]'
        self.verificar_email = By.XPATH,'//*[@class="nameCircle"]'
        self.inserir_email = By.CSS_SELECTOR,'[class="icones"][id="icone"][style = "width: 35px; height: 35px; display: block; cursor: pointer;"]' #Precisa arrumar isso
        self.janela_email = By.XPATH,'//*[contains(text(),"Responsável")]'
        self.aguardar_janela_email_sair = By.CLASS_NAME,'responsible-menu-heading'
        self.inserir_tag = By.XPATH,'//div[@id="aside-header"]//*[@data-test="show-tags"][@title="Atribuir ou excluir tags"]'
        self.confirma_tag = By.CSS_SELECTOR,'[data-test="search-tag"]'
        self.aguardar_tag = By.CSS_SELECTOR,'[id="tagMenu"]'
        self.fechar_janela_tag = By.XPATH,'//div[@id="tagMenu"]//div[2][@class="icones"]'
        self.aguardar_janela_tag_sair = By.XPATH,'//div[@id="tagMenu"]//div[2][@class="icones"]'
       
       
       
    
 
    def verificar_se_existe_modelo(self):
        time.sleep(2)
        print('Entrou na verificação do modelo')
        try:
            print('Modelo ja existe')
            self.aguardar_item_rapido(self.verificar_modelo)  
            return True
        except:
            print('MOdelo não existe')
            return False
        
    def selecionar_templete(self,modalidade):
        self.clique(self.importar_modelo)
        print(f'Aqui é a modalidade {modalidade}')
        match modalidade:
            case 'URBANISMO':
                selector_auxiliar_modalidade = By.XPATH , '//div[contains(text(),"GI_PXR URBANISMO E MULTIPROPRIED...")]'
                print('funcionou')
            case 'MULTIPROPRIEDADE':
                selector_auxiliar_modalidade = By.XPATH , '//div[contains(text(),"GI_PXR URBANISMO E MULTIPROPRIED...")]'
            case 'INCORPORAÇÃO':
                selector_auxiliar_modalidade = By.XPATH , '//div[contains(text() ,"GI_PXR INCORPORAÇÃO")]'
            case 'MARANHÃO':
                selector_auxiliar_modalidade = By.XPATH , '//div[contains(text(),"GI_PXR URB (MARANHÃO)")]'
        
        print(f'Esse é selector da modadelidade {selector_auxiliar_modalidade}')
        self.clique(selector_auxiliar_modalidade)
        self.clique(self.aplicar_modelo)
        self.aguardar_item(self.mensagem_aplicar_modelo)
        self.clique(self.confirmar_modelo)
        print('Aguardar mensagem sair')
        self.aguardar_sair_item(self.mensagem_aplicar_modelo_sair)
        print('Mensagem de aguardar templete saiu ')
    
    
    def verificar_se_existe_email(self):
        print('Entrou na verificação de e_mail')
        try:
            print('Email ja existe')
            self.aguardar_item_rapido(self.verificar_email)
            return True
        except:
            print('Email não existe')
            return False
            
                    
    def email_analista(self,e_mail):
        time.sleep(2)
        self.clique(self.inserir_email)
        self.aguardar_item(self.janela_email)
        selector_auxiliar_email = By.XPATH,f'//span[@class="responsible-option-email"][contains(text(),"{e_mail}")]'
        self.clique(selector_auxiliar_email)
        self.aguardar_sair_item(self.aguardar_janela_email_sair)

    def verificar_se_existe_tag(self,mes_anterior):
        print('Entrou na verificação de teg')
        try:
            print('Teg ja existe')
            self.verificar_tag = By.XPATH,f'//*[@style="display: block;"]//*[contains(text(),"{mes_anterior}")]'
            print(f'mes anterior é {mes_anterior}')
            self.aguardar_item_rapido(self.verificar_tag)
            return True
        except:
            print('Teg não existe')
            return False
        
    

                                      
    def inserir_tags(self,mes_anterior): 
        try:
            self.clique(self.inserir_tag)
            self.aguardar_item(self.aguardar_tag)
            selector_auxiliar_tag_mes = By.XPATH,f'//*[@style="display: block;"]//*[contains(text(),"{mes_anterior}")]'
            self.clique(selector_auxiliar_tag_mes)
            self.clique(self.fechar_janela_tag)
            self.aguardar_sair_item(self.aguardar_janela_tag_sair)
        except:
            incluir_tag = self.escrever(self.confirma_tag,mes_anterior)
            confirma = self.enter(self.confirma_tag)
            self.clique(self.fechar_janela_tag)
            self.aguardar_sair_item(self.aguardar_janela_tag_sair)