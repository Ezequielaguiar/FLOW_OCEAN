from pages.common.BasePageElement import BasePageElement
from selenium.webdriver.common.by import By

class Tag(BasePageElement): 

    def __init__(self):
        self.icone_tags = ''
        self.campo_input = ''
        self.icone_cor = ''
        self.lista_tags = ''
        self.icone_remove_tag = ''
        self.icone_delete_tag = ''

    def adicionar_tag(self, nome): 
        self.click_element(self.icone_tags)
        self.fill(self.campo_input, nome)
        self.click_element(self.icone_cor)