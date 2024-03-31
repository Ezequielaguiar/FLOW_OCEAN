from BasePage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class BasePageElement(BasePage): 

    def fill(self, locator, text): 
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

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
