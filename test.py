from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

class Zombie():

    def __init__(self):
        self.driver = driver

    def open_site(self):
        driver = self.driver
        driver.get('http://www.zombieipsum.com/')
        sleep(1)
        assert "Zombie" in driver.title
        
    def check_link_home(self):
        driver = self.driver
        link = driver.find_element(By.ID, "menu-item-54")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        sleep(2)
        driver.back()
    
    def check_link_blog(self):
        driver = self.driver
        link = driver.find_element(By.ID, "menu-item-17")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        sleep(2)
        driver.back()
    
    def check_link_brains(self):
        driver = self.driver
        link = driver.find_element(By.ID, "menu-item-12")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        sleep(2)
        driver.back()
            
    # def search(self):
    #     driver = self.driver
    #     search_box = driver.find_element("name", "q")
    #     search_box.send_keys("SpaceX")
    #     search_box.send_keys(Keys.RETURN)
    #     driver.implicitly_wait(10)
    #     print("Page title:", driver.title)

        # driver.quit()


