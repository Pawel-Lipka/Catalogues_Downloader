
import constants as const
import frigoshop
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Frs(frigoshop.Frigoshop):



    def load_frs_ro_page(self):
        self.driver.get('http://192.168.44.49/')

    def log_in(self,user=const.USER_FRS_RO,password=const.PASSWORD_FRS_RO):
        self.driver.find_element_by_id('UserName').send_keys(user)
        self.driver.find_element_by_id('Password').send_keys(password)
        self.driver.find_element_by_id('SubmitBtn').click()


    def open_kpi_download_page(self):
        self.driver.execute_script(
            '''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.SLS401&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
    def open_stock_download_page(self):
        self.driver.execute_script(
            '''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.WRH101.CSR&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
    def open_bom_download_page(self):
        self.driver.execute_script(
            '''window.open("http://192.168.44.49/reportengine/rengine.aspx?ReportID=FG.CSR902&action=page");''')
        self.driver.switch_to.window(self.driver.window_handles[1])

    def fill_in_kpi_download_form(self,warehouse_number='025SCH'):
        from_warehouse_textbox = self.driver.find_element_by_id('WarehouseFrom')
        from_warehouse_textbox.send_keys(warehouse_number)
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
    def click_submit_button(self):
        submit_button = self.driver.find_element_by_name("_ctl0")
        submit_button.click()

    def click_print_button(self):
        print_button = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            "#CrystalReportViewer1 > tbody > tr > td > div > div:nth-child(1) > table > tbody > tr > td:nth-child(4) > img"))
        )
        print_button.click()

    def switch_to_export_report_window(self):
        WebDriverWait(self.driver, 20).until(
            EC.new_window_is_opened(self.driver.window_handles))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def choose_export_type(self,select_from_list='RecordToMSExcel'):
        #chose from  list default: MS Excel 97-2000 (Data Only)
        select_list = Select(self.driver.find_element_by_id('exportFormatList'))
        select_list.select_by_value(select_from_list)

    def click_ok_button(self):
        #only for export window
        ok_button = self.driver.find_element_by_id('submitexport')
        ok_button.click()

    def switch_tabs(self,window_number):
        self.driver.switch_to_window(self.driver.window_handles[window_number])




