import base64
import paz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
PATH = r'C:\Users\plipka\Desktop\AutoFrigo\Catalogues_Downloader\chromedriver.exe'
class Cataloge_downloader():

    def __init__(self,driver_patch):
        self.driver = webdriver.Chrome(driver_patch)
        self.user = base64.b64decode(paz.uz).decode('utf-8')
        self.pas = base64.b64decode(paz.pas).decode('utf-8')
        self.caps = DesiredCapabilities().CHROME # config Selenium wait for page to be: 1)fully loaded, 2)interactive, 3)not wait for page load
    def sn_input(self):
        try:
            sn = str(input('Type cooler sn number: '))
            return sn
        except:
            print('unexpected error')


    def frs_russia_log_in(self):
        self.driver.get('http://192.168.44.49/')
        self.driver.find_element_by_id('UserName').send_keys('vlad')
        self.driver.find_element_by_id('Password').send_keys('vlad00')
        self.driver.find_element_by_id('SubmitBtn').click()


    def kpi_download(self):
        self.caps["pageLoadStrategy"] = "eager"
        self.driver.execute_script('''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.SLS401&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.find_element_by_id('WarehouseFrom').send_keys('025SCH')
        self.driver.find_element_by_name('_ctl0').click()
        self.driver.find_element_by_css_selector('#CrystalReportViewer1 > tbody > tr > td > div > div:nth-child(1) > table > tbody > tr > td:nth-child(4) > img').click()
        self.driver.switch_to_alert()


a = Cataloge_downloader(PATH)
a.frs_russia_log_in()
a.kpi_download()

