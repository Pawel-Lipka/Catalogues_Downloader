from frigoshop import Frigoshop
from frs import Frs
from file_handler import File_handler

class Run():
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
                bot.rename_file()
            except NoSuchWindowException:
                return 'try again in few minutes'

    def run_kpi(self,):
        with Frs() as bot:
            bot.load_frs_ro_page()
            bot.log_in()
            bot.open_kpi_download_page()
            bot.fill_in_kpi_download_form()
            bot.click_submit_button()
            bot.click_print_button()
            bot.switch_to_export_report_window()
            bot.choose_export_type()
            bot.click_ok_button()
            bot.download_and_rename1()

'''a = Run()
a.run_kpi()
'''
