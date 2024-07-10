import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

load_dotenv(".env")
X_BASE_URL = "https://x.com"


class X:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(X_BASE_URL)

    def insert_password_value(self):
        password_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@autocomplete='current-password']"))
        )
        password_input.send_keys(os.environ.get("X_PASSWORD"))

        account_login_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@data-testid='LoginForm_Login_Button']"))
        )
        account_login_button.click()

    def login(self):
        close_welcome_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@data-testid='xMigrationBottomBar']"))
        )
        close_welcome_button.click()

        login_page = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//body[contains(@style, 'background-color: rgb(0, 0, 0)')]"))
        )
        login_page.send_keys(Keys.TAB)

        login_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@data-testid='loginButton']"))
        )
        login_button.click()

        email_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
        )
        email_input.send_keys(os.environ.get("X_EMAIL"))

        next_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH,
                                        '//button[contains(@style,"background-color: rgb(239, 243, 244);")]'))
        )
        next_button.click()

    def verify_account_if_locked(self):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']"))
            )
            username_field.send_keys(os.environ.get("X_USERNAME"))
        except TimeoutException as error:
            print(f"All is good in verifying account...\n{error}")
            return None
        username_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@data-testid='ocfEnterTextNextButton']"))
        )
        username_button.click()

    def check_if_homepage(self):
        try:
            close_secure_account_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//button[@data-testid='app-bar-close']"))
            )
            close_secure_account_button.click()
        except TimeoutException as error:
            print(f"All is good...\n{error}")
        # WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//div[@class='public-DraftEditorPlaceholder-inner']"))
        # )

    def post_internet_speed(self, download_speed, upload_speed):
        post_box = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@aria-label='Post text']"))
        )
        post_box.send_keys(f"Hi Internet Provider. My Internet speed is {download_speed}down/{upload_speed}up!")

        post_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButtonInline']"))
        )
        post_button.click()
