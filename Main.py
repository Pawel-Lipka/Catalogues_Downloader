import base64
import paz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
caps = DesiredCapabilities().CHROME
PATH = r'C:\Users\plipka\Desktop\AutoFrigo\Catalogues_Downloader\chromedriver.exe'

class Cataloge_downloader():

    def __init__(self,driver_patch):
        caps["pageLoadStrategy"] = "eager"
        self.driver = webdriver.Chrome(driver_patch,desired_capabilities=caps)
        self.user = base64.b64decode(paz.uz).decode('utf-8')
        self.pas = base64.b64decode(paz.pas).decode('utf-8')
        self.action = ActionChains(self.driver)
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
        self.driver.execute_script('''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.SLS401&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_id('WarehouseFrom').send_keys('025SCH')
        self.driver.find_element_by_name("_ctl0").click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#CrystalReportViewer1 > tbody > tr > td > div > div:nth-child(1) > table > tbody > tr > td:nth-child(4) > img"))
            )
        element.click()
        WebDriverWait(self.driver, 20).until(
            EC.new_window_is_opened(self.driver.window_handles))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        select = Select(self.driver.find_element_by_id('exportFormatList'))
        select.select_by_value('RecordToMSExcel')
        self.driver.find_element_by_id('submitexport').click()

    def frigo_shop_catalogue_downloader_by_serial(self):
        sn = "RO2372586258"
        self.driver.get("https://parts.frigoserve.com/shop/app?__bk_&__windowid=CCS428213376&__rid=RIH1634113424794#'2V10C9D9248E4C6405")
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/form/div/div/div/div[2]/div/div/div/div/div[2]/div/button'))
        )
        element.click()
        self.driver.find_element_by_xpath("/html/body/div[1]/form/div/div/div[3]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div/div/div/div/div/div[5]/div/input").send_keys("PL")
        self.driver.find_element_by_xpath('/html/body/div[1]/form/div/div/div[3]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div/div/div/div/div/div[7]/div/input').send_keys("PLFRGHULU$%^")
        self.driver.find_element_by_xpath("/html/body/div[1]/form/div/div/div[3]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div/div/div/div/div/div[8]/div/button").click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[1]/div[4]/form/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/button'))
                 )
        element.click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME,"guiwindow_child_container"))
                )
        element.click()
        time.sleep(5)
        self.driver.switch_to.frame('shopMain')

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,"/html/body/div[1]/div[2]/div[4]/form/div[2]/div/div[3]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr[2]/td/div/span/div/div/div[1]/div/div/div/div[5]/div/div/div/div/div[1]/div/input"))
        )
        element.send_keys(sn)
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div[2]/div[4]/form/div[2]/div/div[3]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr[2]/td/div/span/div/div/div[3]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[3]/table/tr/td[1]/div/div'))
        )
        element.click()
        self.action.double_click(element).perform()


a = Cataloge_downloader(PATH)
a.frigo_shop_catalogue_downloader_by_serial()




