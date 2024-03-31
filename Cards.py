from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from comandos import Comandos_selenium
import time


class Banco_card(Comandos_selenium):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        print(f'MEu driver é {driver}')
        print('Entrou no banco card')
        self.banco_card = By.XPATH,'//*[contains(text(),"#BANCO DE CARDS")]'
        self.campo_pesquisa = By.CSS_SELECTOR,'[placeholder="Pesquisar"]'
        self.ev_acompanhamento = By.XPATH, '//*[@id="card-main-section"]//*[contains(text(),"EV ACOMPANHAMENTO - PxR") or contains(text(), "EV ACOMPANHAMENTO - PXR")]'
        self.novo_item = By.XPATH,'//div[@role="button"]//span[contains(text(),"Item")]'
        self.criar_item_trabalho = By.CSS_SELECTOR,'[data-test*="item-type-menu-list"]'
        self.versao = By.XPATH,'//div[@role="button"]//*[@type="text"]'
        self.botao_criar = By.CSS_SELECTOR,'[type="button"][id="submit-text-input-button"]'
        
        
    def pesquisar_item(self,sigla):
        print('Entrou no pesquisar item')
        self.aguardar_item(self.banco_card)
        print('aguardar card')
        self.limpar(self.campo_pesquisa)
        self.escrever(self.campo_pesquisa,sigla)
        self.enter(self.campo_pesquisa)
        
    def tem_banco_card(self,nome_card):
        self.aguardar_item(self.banco_card)
        print(f'Aqui é o nome do meu card {nome_card}')
        selector_auxiliar_nome_card = By.XPATH,f'//span[@id="card-title" and contains(text(),"{nome_card}")]'
        self.clique(selector_auxiliar_nome_card)
        self.clique(self.ev_acompanhamento) 
        self.aguardar_sair_item(self.ev_acompanhamento)   
        
    def card_selecionado(self,cod_versao):
        print('Entrou no card_selecionado')
        self.clique(self.novo_item)
        self.clique(self.criar_item_trabalho)
        self.escrever(self.versao,cod_versao)
        self.enter(self.versao)
        selector_auxiliar_cod_versao = By.CSS_SELECTOR,f'[title="{cod_versao}"]'
        self.clique(selector_auxiliar_cod_versao)
        self.aguardar_sair_item(selector_auxiliar_cod_versao)
        print('Saiu do card_selecionado')
        
    def verificar_se_existe_card(self,cod_versao):
        try:
            
            print('Entrou verificar_card')
            selector_auxiliar_cod_versao = By.CSS_SELECTOR,f'[title="{cod_versao}"]'
            self.aguardar_item_rapido(selector_auxiliar_cod_versao)
            self.scroll_to_element(selector_auxiliar_cod_versao)
            self.clique_rapido(selector_auxiliar_cod_versao)
            self.aguardar_sair_item(selector_auxiliar_cod_versao)
            return True
        except:
            print('Saiur do verificar')
            return False
            
        
        