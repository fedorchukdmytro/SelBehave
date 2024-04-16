from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        
    def test_link_home(self):
        driver = self.driver
        link = driver.find_element(By.ID, "menu-item-54")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        assert "Zombie" in driver.title
    
    def test_link_blog(self):
        driver = self.driver
        link = driver.find_element(By.ID, "menu-item-17")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        driver.back()
    
    def test_link_brains(self):
        driver = self.driver
        link = driver.find_element(By.ID, "menu-item-12")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        driver.back()
    
    def test_link_more(self):
        driver = self.driver
        link = driver.find_element(By.ID, "more")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        driver.back()
    
    def test_link_regular(self):
        driver = self.driver
        link = driver.find_element(By.ID, "regular")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        driver.back()

    def test_link_lite(self):
        driver = self.driver
        link = driver.find_element(By.ID, "lite")
        assert link.is_displayed()
        assert link.is_enabled()
        link.click()
        driver.back()

    def options_count(self, expected_count):
        options = driver.find_elements(By.ID, 'options')
        # links = options.find_element(By.TAG_NAME, 'li')
        
        print(len(options))
        print('hiiii')

z = Zombie()
z.open_site()
z.options_count(5)
            