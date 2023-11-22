import time
import constants as const
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from file_handler import File_handler

class Settings(File_handler):

    def __init__(self,driver_path=const.PATH,tear_down=False,page_load_strategy = 'eager'):
        caps = DesiredCapabilities().CHROME
        caps['pageLoadStrategy'] = page_load_strategy
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=caps)
        self.tear_down = tear_down
        self.driver.implicitly_wait(10)
        #self.driver.minimize_window()
        self.action = ActionChains(self.driver)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.driver.quit()
