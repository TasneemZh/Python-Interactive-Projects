from selenium import webdriver
from x import X
from speedtest import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

speed_test = SpeedTest(driver)
speed_test.start_internet_test()
download_speed = speed_test.check_internet_speed(True)
upload_speed = speed_test.check_internet_speed(False)

x = X(driver)
x.login()
x.verify_account_if_locked()
x.insert_password_value()
x.check_if_homepage()
x.post_internet_speed(download_speed, upload_speed)
