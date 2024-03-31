from selenium.webdriver.common.by import By
from comandos import Comandos_selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Ocean(Comandos_selenium):
    def __init__(self,usario,senha):
        super().__init__()
        self.usuario = usario
        self.senha  = senha
        self.digitar_usuário = By.CSS_SELECTOR, '[name="loginfmt"]'
        self.avançar = By.CSS_SELECTOR, '[id*="idSIButton"]'
        self.campo_senha = By.CSS_SELECTOR , '[name="passwd"]'
        self.botao_entrar = By.CSS_SELECTOR , '[value="Entrar"]'
        self.botao_sim = By.CSS_SELECTOR ,'[value="Sim"]'        
        self.Login_Conta_Microsoft = By.XPATH,'//*[contains(text(),"Login Conta Microsoft")]'
        self.espaco_trabalho = By.XPATH,'//*[contains(text(),"Espaços de Trabalho")]'
        self.workspace = By.CLASS_NAME ,'sc-fmzyuX.gCroip'
        self.pxp = By.XPATH,'//span[contains(text(), "7.2. PXR")]'

            
        
    def faz_login(self):
        self.escrever(self.digitar_usuário,self.usuario)
        self.clique(self.avançar)
        self.escrever(self.campo_senha,self.senha)
        self.clique(self.botao_entrar)
        self.clique(self.botao_sim)
        self.clique(self.Login_Conta_Microsoft)
        self.aguardar_item(self.espaco_trabalho)
        print('terminou')
    
    def entrar_ocean(self):
        self.clique(self.pxp)
        print('Entrou no ocean')
        return self.driver

   
    
  