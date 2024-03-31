from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class GerenciarNavegador():
    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.url_inicial = 'https://login.microsoftonline.com/3e57d4dc-f016-4540-b3b8-d667b5cb9512/oauth2/v2.0/authorize?response_type=id_token&scope=user.read%20openid%20profile&client_id=642a14f3-7b12-458f-9e7c-8a0c1f7cf47e&redirect_uri=https%3A%2F%2Focean.trinus.co%2F&state=eyJpZCI6IjIzYmJjNzM1LTFlNTUtNGZlOS05ZWI2LWJhZDRmN2I1ZWNjYyIsInRzIjoxNzA0ODU0NDk4LCJtZXRob2QiOiJwb3B1cEludGVyYWN0aW9uIn0%3D&nonce=3257e416-541c-422e-ae61-89eadf1131205&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.4.18&client-request-id=aba0de3d-f9d9-4c5b-ad7a-91f7c2ed79ea&response_mode=fragment&sso_reload=true'
        self.url_workspace = 'https://ocean.trinus.co/ocean/workspaces/9/boards' #Precisa usa esse link 
                                
    def abrir_navegador(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.aguardar_carregamento()
    
    def aguardar_carregamento(self):
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
    
    def link1(self):
        self.driver.get(self.url_inicial)
        
    def link2(self):
        self.driver.get(self.url_workspace)
        
    def alterar_link(self,driver):
        driver.get('https://ocean.trinus.co/ocean/workspaces/9/boards/446/item-view/kanban')
        
    def fechar_navegador(self,driver):
        driver.quit()