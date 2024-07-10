from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SPEEDTEST_BASE_URL = "https://speedtest.net"


class SpeedTest:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(SPEEDTEST_BASE_URL)

    def start_internet_test(self):
        start_test_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//a[@aria-label='start speed test - connection type multi']"))
        )
        start_test_button.click()

    def check_internet_speed(self, is_download):
        if is_download:
            type_speed = "download"
        else:
            type_speed = "upload"
        internet_speed = "True"
        while internet_speed == "True" or not internet_speed or internet_speed == "NaN":
            print(f"Before {type_speed}_speed: {internet_speed}")
            internet_label = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, f"//span[contains(@class, '{type_speed}-speed')]"))
            )
            internet_speed = internet_label.get_attribute(f"data-{type_speed}-status-value")
            print(f"After {type_speed}_speed: {internet_speed}")
        print(f"{type_speed} Speed: {internet_label.get_attribute("innerText")}")
        return internet_label.get_attribute("innerText")
