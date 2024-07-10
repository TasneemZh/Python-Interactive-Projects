import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv

load_dotenv(".env")


def sign_in_instagram(driver):
    email_input = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    email_input.send_keys(os.environ.get("INSTAGRAM_EMAIL"))

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(os.environ.get("INSTAGRAM_PASSWORD"))

    login_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
