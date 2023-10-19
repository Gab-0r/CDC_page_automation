from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


class WebDriverManager:
    def __init__(self, driver_name: str):
        self.driver_name = driver_name

    def create_driver(self) -> Chrome:
        if self.driver_name == "Chrome headless":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            driver = Chrome(options=options)
            driver.set_page_load_timeout(500000)
            return driver

        elif self.driver_name == "Chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            driver = Chrome(options=options)
            driver.set_page_load_timeout(500000)
            return driver
