from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from comandos import Comandos_selenium
import time

class Compartilhar_esteira(Comandos_selenium):
    
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        self.botao_compartilha = By.XPATH,'//div[1]//div[2]//span/div[@class="icones"]'
        self.compartilhar_execucao = By.XPATH,'//button[contains(text(),"COMPARTILHAR EXECUÇÃO")]'
        self.aguardar_janela = By.XPATH,'//div[contains(text(),"Compartilhar execução de item")]'
        self.aguardar_Builders_na_tela = By.XPATH,'//div[@id = "idChildrenContainer"]//*[(text() ="Builders")]'
        self.selecionar_esteira = By.XPATH,'//div[@id="selectedItemWrapper"]//span[contains(text(),"Selecione")]'
        self.confirmar_esteira = By.XPATH,'//button//div[contains(text(),"Compartilhar")]'
        self.aguardar_janela_compartilhar_item = By.XPATH,'//button[@data-testid="cancel-button"][text()="Cancelar"]'
        self.confirmar_compartilhamento = By.XPATH,'//div/button[@id="confirm-button"][contains(text(),"Compartilhar")]'
        self.aguardar_janela_compartilhar_item_sair = By.XPATH,'//header//p[contains(text(),"Deseja compartilhar o item")]'
        self.aguardar_janela_compartilhar_sair = By.XPATH,'//button[@data-testid="cancel-button"][text()="Cancelar"]'
        #Precisa interar sobre cada intem da esteira para compartilhar

    
        
    def compartilhar(self,lista_compartilhamento):
        print('Entrou no compartilhamento')
        for i , item_compartilhamento in enumerate(lista_compartilhamento['Nome_esteira']):
            try:
                
                selector_auxiliar = By.XPATH,f'//*[contains(text(),"{item_compartilhamento}")]'                                                
                print(f'Verificar esteira compartilhada {selector_auxiliar}')
                self.aguardar_item_rapido(selector_auxiliar)
                continue
            except:                
                print(f'Aqui e a esteira de compartilhar com lideres : {i} é {item_compartilhamento}')
                self.clique(self.botao_compartilha)
                self.clique(self.compartilhar_execucao)
                self.aguardar_item(self.aguardar_Builders_na_tela)
                self.clique(self.selecionar_esteira)
                time.sleep(4)
                selector_auxiliar_compartilhar_esteira = By.XPATH,f'//*[@id="idChildrenContainer"]//*[contains(text(),"{item_compartilhamento}")]'  
                print(f'Selector esteira é {selector_auxiliar_compartilhar_esteira}')
                self.scroll_to_element(selector_auxiliar_compartilhar_esteira)
                self.clique(selector_auxiliar_compartilhar_esteira)
                print('Passou do elemento')
                self.clique(self.confirmar_esteira)
                self.aguardar_item(self.aguardar_janela_compartilhar_item)
                self.clique(self.confirmar_compartilhamento)
                self.aguardar_sair_item(self.aguardar_janela_compartilhar_item_sair)
                self.aguardar_sair_item(self.aguardar_janela_compartilhar_sair)