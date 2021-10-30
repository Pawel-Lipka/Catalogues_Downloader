from autofrigo import Autofrigo





with Autofrigo() as bot:

    bot.load_frigoshop_login_page()
    bot.skip_cookies()
    bot.log_in_to_frigoshop()
    bot.select_organisation()
    bot.switch_to_select_device_frame()
    bot.serial_number_input()
    bot.select_first_positon()
