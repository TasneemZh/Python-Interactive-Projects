from selenium import webdriver
from login import sign_in_instagram
from homepage import search_for_page

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")

sign_in_instagram(driver)
search_for_page(driver)
