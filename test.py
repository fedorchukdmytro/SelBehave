
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




chrome_options = Options()
# chrome_options.add_argument("--headless")
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
        assert "Zombie" in driver.title
        
    def test_element_home(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "menu-item-54")))
        assert element.is_displayed()
        assert element.is_enabled()
        element.click()
    
    def test_element_blog(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "menu-item-17")))
        assert element.is_displayed()
        assert element.is_enabled()
        element.click()
        driver.back()
    
    def test_element_brains(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "menu-item-12")))
        assert element.is_displayed()
        assert element.is_enabled()
        element.click()
        driver.back()
    
    def test_element_more(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "more")))
        assert element.is_displayed()
        assert element.is_enabled()
        element.click()
        driver.back()
    
    def test_element_regular(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID,  "regular")))
        assert element.is_displayed()
        assert element.is_enabled()
        element.click()
        driver.back()

    def test_element_lite(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lite")))
        assert element.is_displayed()
        assert element.is_enabled()
        element.click()
        driver.back()

    def test_close_driver(self):
        driver = self.driver
        driver.close()

    def options_count(self, expected_count):
        options = driver.find_element(By.ID, 'options')
        elements = options.find_element(By.TAG_NAME, 'li')
        assert options.size['height'] == expected_count
            


