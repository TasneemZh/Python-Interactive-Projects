from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Form:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://forms.gle/aK7Q8ut9RB7A5a5k7")

    def fill_form(self, apartment):
        xpath = "//input[@type='text' and @autocomplete='off']"
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, xpath))
        )
        answer_fields = self.driver.find_elements(By.XPATH, xpath)

        answer_fields[0].send_keys(apartment["address"])
        answer_fields[1].send_keys(apartment["price"])
        answer_fields[2].send_keys(apartment["link"])

        send_button = self.driver.find_element(By.XPATH, "//div[@role='button']")
        send_button.click()

        another_reply_link = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/viewform?usp=form_confirm')]"))
        )
        another_reply_link.click()
