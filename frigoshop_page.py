import time
import constants as const
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from file_handler import File_handler
import settings

class Frigoshop(settings.Settings, File_handler):


    def load_frigoshop_login_page(self):
        self.driver.get(const.FRIGO_SHOP_LOGIN_PAGE)

    def click_ok_button(self):
        ok_button = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//span[.='OK']"))
        )
        ok_button.click()

    def log_in_to_frigoshop(self,user=const.USER_FRG_SHOP,password=const.PASSSWORD_FRG_SHOP):
        time.sleep(2)
        login_password_fields =  self.driver.find_elements_by_class_name(
            'guitextfield'
        )
        login_password_fields[0].send_keys(user)
        login_password_fields[1].send_keys(password)
        time.sleep(2)
        login_password_fields[1].send_keys(Keys.RETURN)

    def switch_to_select_device_frame(self):
        WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it('shopMain'))

    def serial_number_input(self,sn):
        search_field = self.driver.find_element_by_class_name('guitextfield')
        search_field.send_keys(sn)
        search_field.send_keys(Keys.RETURN)

    def select_first_positon(self):
        search_results = self.driver.find_element_by_class_name('guitable_content_table')  # set driver at results lists
        first_result = search_results.find_element_by_class_name('guilabel')  # find first element in list
        self.action.double_click(first_result).perform()  # press first search result two times

    def click_on_print_button(self):
        print_button = self.driver.find_element_by_css_selector(
            'img[src="WEB-RES/resource/resource?id=class_image_de.docware.framework.modules.gui.a.c_defaultimages_flat_imgDesignGuiViewerPrinter_w.png"]')  # find print/download button
        print_button.click()  # click on print button

    def choose_what_to_download(self):
        print_window = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'guiwindow_child_content'))
        )  # wait until print window are pop up
        print_window = print_window.find_elements_by_css_selector(
            'button[class="guibutton_linkenabled"]')  # find two buttons on 'print window'
        print_window[1].click()  # click secound button on 'print window'

    def click_save_button(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[.='Save']"))  # wait until save buton can be click
        )
        save_button.click()  # click save button

    def log_out(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        log_out_button = self.driver.find_element_by_xpath("//span[.='Log out']")
        log_out_button.click()
        yes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[.='Yes']"))  # wait until yes button can be click
        )
        yes_button.click()
    def get_file_name(self):
        file_name = File_handler.getDownLoadedFileName(self,220,self.driver)
        return file_name

    def rename_file(self,file_name,new_name):
        File_handler.file_rename(self,file_name,new_name)



