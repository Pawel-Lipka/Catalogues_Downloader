from frs_page import Frs


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
    bot.rename_file(stock_file_name, 'Stock Romania')
