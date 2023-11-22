import re
from selenium.common.exceptions import NoSuchWindowException,NoSuchElementException,TimeoutException
from frigoshop_page import Frigoshop

while True:

    sn = input("Serial number:").strip().lower()
    if re.match("[r][ou]\d{10}",sn):

        with Frigoshop(tear_down=True) as bot:
            bot.load_frigoshop_login_page()
            bot.click_ok_button()
            bot.log_in_to_frigoshop()
            bot.click_ok_button()
            try:
                bot.switch_to_select_device_frame()
                bot.serial_number_input(sn)
                bot.select_first_positon()
                bot.click_ok_button()
                bot.click_on_print_button()
                bot.choose_what_to_download()
                bot.click_save_button()
                sn_file_name = bot.get_file_name()
                bot.rename_file(sn_file_name, sn)
                bot.log_out()
            except NoSuchWindowException:
                print('try again in few minutes')
            except TimeoutException:
                print('try again in few minutes')
            except NoSuchElementException:
                print('no such catalogue yet created')