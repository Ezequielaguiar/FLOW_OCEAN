from selenium import webdriver

class BasePage(object):
    def __init__(self, driver=None):
        self.driver = driver

    def open_browser(self):
        if not self.driver:
            self.driver = webdriver.Chrome()
        self.page_timeout()
        
    def page_timeout(self):
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
    
    def go_to(self, url):
        self.driver.get(url)

    def closeBrownser(self):
        self.driver.quit()
