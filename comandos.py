from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from Navegador import GerenciarNavegador
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class Comandos_selenium(GerenciarNavegador):
    def __init__(self):
        super().__init__()
        self.time = 30
        self.time_rapido = 8
        self.frequencia_verificação = 2
        
    def clique(self,selector):
        WebDriverWait(self.driver,self.time,poll_frequency= self.frequencia_verificação,ignored_exceptions=(TimeoutException)).until(EC.element_to_be_clickable((selector))).click()
    
    def clique_rapido(self,selector):
        WebDriverWait(self.driver,self.time_rapido).until(EC.element_to_be_clickable((selector))).click()
    
    def duplo_clique(self,selector):
        WebDriverWait(self.driver,self.time_rapido).until(EC.element_to_be_clickable((selector))).click()
        
    def escrever(self,selector,texto ):
        WebDriverWait(self.driver,self.time,poll_frequency= self.frequencia_verificação,ignored_exceptions=(TimeoutException)).until(EC.element_to_be_clickable((selector))).send_keys(texto)
        
        
    def limpar(self,selector):
        WebDriverWait(self.driver,self.time,poll_frequency= self.frequencia_verificação,ignored_exceptions=(TimeoutException)).until(EC.element_to_be_clickable((selector))).clear()
    
    def enter(self,select):
        WebDriverWait(self.driver,self.time,poll_frequency= self.frequencia_verificação,ignored_exceptions=(TimeoutException)).until(EC.element_to_be_clickable((select))).send_keys(Keys.ENTER)
            
    def aguardar_item(self,selector):
        WebDriverWait(self.driver,self.time,poll_frequency= self.frequencia_verificação,ignored_exceptions=(TimeoutException)).until(EC.visibility_of_element_located((selector)))
    
    def aguardar_item_rapido(self,selector):
        WebDriverWait(self.driver,self.time_rapido,poll_frequency= self.frequencia_verificação).until(EC.visibility_of_element_located((selector)))
    
    
    def aguardar_sair_item(self,selector):
        WebDriverWait(self.driver,self.time,poll_frequency= self.frequencia_verificação,ignored_exceptions=(TimeoutException)).until_not(EC.visibility_of_element_located((selector)))
    
    
    def select_by_text(self, locator, text):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_value(value)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    
    