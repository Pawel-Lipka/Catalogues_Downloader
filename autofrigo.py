import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
"""caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
driver = webdriver.Chrome(desired_capabilities=caps,"""


class Autofrigo(webdriver.Chrome,webdriver.DesiredCapabilities):

#TODO: ogarnąć desiredcapabilities - wtórym miejscu przekazuje sie driver??
    def __init__(self,driver_path=r'C:\Users\plipka\Desktop\AutoFrigo\Catalogues_Downloader\chromedriver.exe',tear_down=False):
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        caps = self.CHROME
        caps["pageLoadStrategy"] = "none"
        super(Autofrigo,self).__init__()
        self.tear_down = tear_down
        self.implicitly_wait(10)
        self.maximize_window()



    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit()

    def load_frigoshop_login_page(self):
        self.get(const.FRIGO_SHOP_LOGIN_PAGE)

    def skip_cookies(self):
        ok_button = self.find_element_by_xpath("//span[.='OK']")
        ok_button.click()


    def log_in_to_frigoshop(self,user=const.USER_FRG_SHOP,password=const.PASSSWORD_FRG_SHOP):
        login_password_fields = self.find_elements_by_class_name(
            'guitextfield'
        )
        login_password_fields[0].send_keys(user)
        login_password_fields[1].send_keys(password)
        login_password_fields[1].send_keys(Keys.RETURN)

    def select_organisation(self):
        ok_button = self.find_element_by_xpath("//span[.='OK']")
        ok_button.click()

    def switch_to_select_device_frame(self):
        self.switch_to.frame('shopMain')

    def serial_number_input(self,sn='RO2372586258'):
        search_field = self.find_element_by_class_name('guitextfield')
        search_field.send_keys(sn)
        search_field.send_keys(Keys.RETURN)





