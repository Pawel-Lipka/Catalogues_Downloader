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
caps = DesiredCapabilities().CHROME # sets whether or not to wait for the page to load
PATH = r'C:\Users\plipka\Desktop\AutoFrigo\Catalogues_Downloader\chromedriver.exe' # chromedriver path

class Cataloge_downloader():

    def __init__(self,driver_patch):
        caps["pageLoadStrategy"] = "eager" # wait to page be interactive #disable
        self.driver = webdriver.Chrome(driver_patch)
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

    def frigo_shop_log_in(self):
        self.driver.get("https://parts.frigoserve.com/shop/app?__bk_&__windowid=CCS428213376&__rid=RIH1634113424794#'2V10C9D9248E4C6405")
        self.driver.implicitly_wait(6)



        login_password = self.driver.find_elements_by_class_name('guitextfield')#find login and password input windows
        login_password[0].send_keys('PL')#input login
        login_password[1].send_keys('PLFRGHULU$%^')#input password

        cookies_ok_button = self.driver.find_element_by_class_name(
            'guiwindow_child_container')  # find lower cookie politics bar
        cookies_ok_button.find_element_by_class_name('guibutton_enabled').click()  # click ok on cookie bar

        login_password[1].send_keys(Keys.RETURN)#hit enter keypad

        select_organisation_window = self.driver.find_element_by_class_name('guilayoutflow_container')#find upper button class on pop up window
        select_organisation_window.find_element_by_class_name('guibutton_enabled')#find ok button on pop up window
        select_organisation_window.click()#click ok button on pop up window

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
        self.driver.switch_to.frame('shopMain')
        search_by_serial = self.driver.find_element_by_class_name('guitextfield')#first guitextfield is serial input field
        search_by_serial.send_keys(sn) #send serial number
        search_by_serial.send_keys(Keys.RETURN) #hit enter to confirm


        search_results = self.driver.find_element_by_class_name('guitable_content_table')#set driver at results lists
        first_result = search_results.find_element_by_class_name('guilabel')#find first element in list
        self.action.double_click(first_result).perform()#press first search result two times

        #TO DO: poczekac az drugi guibutton sie zaladuje
        time.sleep(5)# wait until cookie button presenc
        cookies_ok_button = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CLASS_NAME,'guibutton_enabled')) #find ok cookie button
        )
        cookies_ok_button.click() #press ok on cookie button

        print_button = self.driver.find_element_by_css_selector('img[src="WEB-RES/resource/resource?id=class_image_de.docware.framework.modules.gui.a.c_defaultimages_flat_imgDesignGuiViewerPrinter_w.png"]') # find print/download button
        print_button.click() #click on print button

        print_window = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,'guiwindow_child_content'))
            ) # wait until print window are pop up
        print_window = print_window.find_elements_by_css_selector('button[class="guibutton_linkenabled"]') #find two buttons on 'print window'
        print_window[1].click() # click secound button on 'print window'

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//span[.='Save']")) #wait until save buton can be click
            )

        save_button.click() #click save button








a = Cataloge_downloader(PATH)

a.frigo_shop_log_in()
a.frigo_shop_catalogue_downloader_by_serial()




