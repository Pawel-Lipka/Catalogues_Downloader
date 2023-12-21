import settings
import constants as const
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from file import File

class Frs(settings.Settings):

    # Load main FRS RO
    def load_frs_ro_page(self):
        self.driver.get('http://192.168.44.49/')

    # Log in to FRS page using credentials from constants.py
    def log_in(self,user=const.USER_FRS_RO,password=const.PASSWORD_FRS_RO):
        self.driver.find_element_by_id('UserName').send_keys(user)
        self.driver.find_element_by_id('Password').send_keys(password)
        self.driver.find_element_by_id('SubmitBtn').click()

    # open open orders window and switch to it. Need to be login in.
    def open_orders_download_page(self):
        self.driver.execute_script(
            '''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.SLS401&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])

    # open stock download window and switch to it, need to be login in.
    def open_stock_download_page(self):
        self.driver.execute_script(
            '''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.WRH101.CSR&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])

    # open bill of material download window and switch to it. Need to be login in.
    def open_bom_download_page(self):
        self.driver.execute_script(
            '''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.CSR902&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])


    # fill in what serial number You want to download. Need to be on BOM download window
    def fill_in_bom_download_form(self,serial_number):
        serial_number_from = self.driver.find_element_by_id("SERIALFROM")
        serial_number_from.clear()
        serial_number_from.send_keys(serial_number)
        serial_number_to = self.driver.find_element_by_id("SERIALTO")
        serial_number_to.clear()
        serial_number_to.send_keys(serial_number)
        production_date_from = self.driver.find_element_by_id("DATEFROM")
        production_date_from.clear()
        production_date_from.send_keys("01/01/2010")
        production_date_to = self.driver.find_element_by_id("DATETO")
        production_date_to.clear()
        production_date_to.send_keys("01/01/2022")

    # click submit button on open downlad page. Need to be on download page
    def click_submit_button(self):
        submit_button = self.driver.find_element_by_name("_ctl0")
        submit_button.click()

    # wait to page is loaded and click print button. Need to be on raport page window
    def click_print_button(self):
        print_button = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            "#CrystalReportViewer1 > tbody > tr > td > div > div:nth-child(1) > table > tbody > tr > td:nth-child(4) > img"))
        )
        print_button.click()

    # wait to downloading parameter page is open and switch to it
    def switch_to_export_report_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.new_window_is_opened)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(EC.title_is("Export the Report"),10)

    # Choose in what format report will be download
    def choose_export_type(self,select_from_list='RecordToMSExcel'):
        #chose from  list default: MS Excel 97-2000 (Data Only)

        select_list = Select(self.driver.find_element_by_id('exportFormatList'))
        select_list.select_by_value(select_from_list)

    # click ok button on export window
    def click_ok_button(self):
        #only for export window
        ok_button = self.driver.find_element_by_id('submitexport')
        ok_button.click()

    def switch_tabs(self,window_number):
        self.driver.switch_to_window(self.driver.window_handles[window_number])


