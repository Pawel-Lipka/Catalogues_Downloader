# bot to download open orders of Romania warehouse

from frs_page import Frs
from file import File

with Frs(tear_down=True) as bot:
    bot.load_frs_ro_page()
    bot.log_in()
    bot.open_orders_download_page()
    bot.click_submit_button()
    bot.click_print_button()
    bot.switch_to_export_report_window()
    bot.choose_export_type()
    bot.click_ok_button()
    kpi_file_name = bot.getDownLoadedFileName(220,bot.driver)
    bot.file_rename(kpi_file_name, 'Otwarte zamówienia')

