from run import Run
import time
import constants as const
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from file_handler import File_handler
from frigoshop import Frigoshop
from frs import Frs
from selenium.common.exceptions import NoSuchWindowException,NoSuchElementException,TimeoutException
import time
import os


intro_message = 'Welcome to AutoFrigo, choose Your action:\n' \
                '1) Download Catalogue with serial number\n' \
                '2) Download KPI\n' \
                '3) Download Romania warehouse stock\n' \
                '4) Download KPI and Romania warehouse stock\n' \
                '5) Download Grodzisk Maz. Stock\n' \
                '6) Download BOM file with serial number\n' \
                'exit) Exit'

run = Run()
user_choice = 0
serial_number = 'sn'
while user_choice != 'exit':
    print(intro_message)
    try:
        user_choice = input()
        if user_choice == 'exit':
            break
        user_choice = int(user_choice)


        if user_choice == 1:

            while len(serial_number) != 12 or serial_number != 'exit':
                serial_number = str(input("Type serial number or exit: "))
                if serial_number == 'exit':
                    break
                elif len(serial_number) < 12:
                    print("Serial number too short")
                elif len(serial_number) > 12:
                    print("Serial number too long")
                else:
                    print('wait until done')
                    run.run_frigoshop(serial_number)
                    print('done')
        elif user_choice == 2:
            print('wait until done')
            run.run_kpi()
            print('done')
        elif user_choice == 3:
            print('wait until done')
            run.run_stock()
            print('done')
        elif user_choice == 4:
            print('wait until done')
            run.run_stock_and_kpi()
            print('done')
        elif user_choice == 6:
            while len(serial_number) != 12 or serial_number != 'exit':
                serial_number = str(input("Type serial number or exit: "))
                if serial_number == 'exit':
                    break
                elif len(serial_number) < 12:
                    print("Serial number too short")
                elif len(serial_number) > 12:
                    print("Serial number too long")
                else:
                    print('wait until done')
                    run.run_bom_file(serial_number)
                    print('done')
    except ValueError:
        print('Wrong number!\n')



