from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Google():

    def __init__(self):
        self.driver = webdriver.Chrome()
        

    def open_site(self):
        driver = self.driver
        driver.get('https://www.google.com.ua')
        sleep(1)
        assert "Google" in driver.title
        
    
    def check_link(self, link):
        driver = self.driver
        link = driver.find_element(By.XPATH, f"//a[contains(text(), '{link}')]")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        sleep(2)
        driver.back()
            
    def search(self):
        driver = self.driver
        search_box = driver.find_element("name", "q")
        search_box.send_keys("SpaceX")
        search_box.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        print("Page title:", driver.title)

        driver.quit()


