from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

INSTAGRAM_PAGE = "quranmethod"


def scroll_down(driver):
    followers_popup = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//div[contains(@style, 'max-height: 400px')]/div[3]"))
    )
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)


def get_follower_buttons(driver):
    followers_section = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: auto;')]"))
    )
    follower_buttons = followers_section.find_elements(By.XPATH, ".//button")
    return follower_buttons


def search_for_page(driver):
    search_icon = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//a[@href='#'][1]"))
    )
    search_icon.click()

    search_field = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Search input']"))
    )
    search_field.send_keys(INSTAGRAM_PAGE)

    instagram_page = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, f"//a[@href='/{INSTAGRAM_PAGE}/']"))
    )
    instagram_page.click()

    instagram_followers = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, f"//a[@href='/{INSTAGRAM_PAGE}/followers/']"))
    )
    instagram_followers.click()

    index = 0
    while index < 30:
        if index != 0:
            scroll_down(driver)
        follower_buttons = get_follower_buttons(driver)
        print(f"follower_buttons: {len(follower_buttons)}")
        while index < len(follower_buttons):
            try:
                follower_buttons[index].click()
            except StaleElementReferenceException as error:
                print(f"This error is expected...\n{error}")
                follower_buttons = get_follower_buttons(driver)
                follower_buttons[index].click()
            index += 1
