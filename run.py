#!.\venv\Scripts\python.exe
from frigoshop import Frigoshop
from frs import Frs
from selenium.common.exceptions import NoSuchWindowException,NoSuchElementException,TimeoutException


class Run:
    def run_frigoshop(self,sn):
        with Frigoshop(sn=sn) as bot:
            bot.load_frigoshop_login_page()
            bot.click_ok_button()
            bot.log_in_to_frigoshop()
            bot.click_ok_button()
            try:
                bot.switch_to_select_device_frame()
                bot.serial_number_input()
                bot.select_first_positon()
                bot.click_ok_button()
                bot.click_on_print_button()
                bot.choose_what_to_download()
                bot.click_save_button()
                sn_file_name = bot.get_file_name()
                bot.rename_file(sn_file_name,sn)
                bot.log_out()
            except NoSuchWindowException:
                return 'try again in few minutes'
            except TimeoutException:
                return 'try again in few minutes'
            except NoSuchElementException:
                return 'no such catalogue yet created'


    def run_kpi(self):
        with Frs(tear_down=True) as bot:
            bot.load_frs_ro_page()
            bot.log_in()
            bot.open_kpi_download_page()
            bot.click_submit_button()
            bot.click_print_button()
            bot.switch_to_export_report_window()
            bot.choose_export_type()
            bot.click_ok_button()
            kpi_file_name = bot.get_file_name()
            bot.rename_file(kpi_file_name,'Otwarte zamówienia')

    def run_stock(self):
        with Frs(tear_down=True) as bot:
            bot.load_frs_ro_page()
            bot.log_in()
            bot.open_stock_download_page()
            bot.click_submit_button()
            bot.click_print_button()
            bot.switch_to_export_report_window()
            bot.choose_export_type()
            bot.click_ok_button()
            stock_file_name = bot.get_file_name()
            bot.rename_file(stock_file_name,'Stock Romania')


    def run_stock_and_kpi(self):
        with Frs(tear_down=True) as bot:
            bot.load_frs_ro_page()
            bot.log_in()
            bot.open_stock_download_page()
            bot.open_kpi_download_page()
            bot.click_submit_button()
            bot.click_print_button()
            bot.switch_tabs(2)
            bot.click_submit_button()
            bot.click_print_button()
            bot.switch_to_export_report_window()
            bot.choose_export_type()
            bot.click_ok_button()
            kpi_file_name = bot.get_file_name()
            bot.switch_tabs(-3)
            bot.choose_export_type()
            bot.click_ok_button()
            stock_file_name = bot.get_file_name()
            bot.rename_file(stock_file_name, 'Stock Romania')
            bot.rename_file(kpi_file_name, 'KPI')

    def run_bom_file(self,serial_number):
        with Frs(tear_down=True) as bot:
            bot.load_frs_ro_page()
            bot.log_in()
            bot.open_bom_download_page()
            bot.fill_in_bom_download_form(serial_number)
            bot.click_submit_button()
            bot.click_print_button()
            bot.switch_to_export_report_window()
            bot.choose_export_type()
            bot.click_ok_button()
            stock_file_name = bot.get_file_name()
            bot.rename_file(stock_file_name,serial_number)

run = Run()
run.run_kpi()