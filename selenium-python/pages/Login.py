from common.BasePageElement import BasePageElement
from selenium.webdriver.common.by import By

class Login(BasePageElement):

    def __init__(self):
        self.campo_usuario = (By.CSS_SELECTOR, '.input-usuario')
        self.campo_senha = (By.CSS_SELECTOR, '.input-senha')
        self.btn_login = (By.CSS_SELECTOR, '.btn-entrar')

    def loginWith(self, usuario, senha):
        self.fill(self.campo_usuario, usuario)
        self.fill(self.campo_senha, senha)
        self.click_element(self.btn_login)