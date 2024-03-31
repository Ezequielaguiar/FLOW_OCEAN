from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Visao_intes():
    def __init__(self,driver):
        self.driver = driver
        self.campo_pesquisa = self.driver.find_element(By.CSS_SELECTOR,'[placeholder="Pesquisar"]')
        self.banco_card = self.driver.find_element(By.CSS_SELECTOR,'[data-rbd-droppable-context-id]')
        
    def pesquisar_item(self,campo_pesquisa):
        WebDriverWait(self.driver,120).until(EC.presence_of_element_located((self.campo_pesquisa)))
        self.campo_pesquisa.send_keys(campo_pesquisa)
        self.campo_pesquisa.send_keys(Keys.ENTER)
    
    def tem_banco_card(self):
            self.vericar_banco_card = WebDriverWait(self.driver,120).until(EC.visibility_of_element_located((self.banco_card)))
            self.vericar_banco_card = WebDriverWait(self.driver,120).until(EC.presence_of_element_located((self.banco_card)))