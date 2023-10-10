# Only use time delays for debugging
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langdetect import detect_langs


def get_locator(raw_locator: tuple) -> tuple:
    """Function, takes a tuple with a locator

    :param raw_locator: A tuple with a locator. First position for a string with the strategy and the second
        with the selector
    :returns: A tuple with the strategy BY object and the selector
    """
    strategy, selector = raw_locator
    strategies = {"ID": By.ID, "XPATH": By.XPATH, "CSS": By.CSS_SELECTOR}
    return strategies[strategy], selector


def downloads_finished(driver: Chrome):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
    """)


# TODO: Exceptions and raises for methods that need them
class BrowserInteractions:
    def __init__(self, driver: Chrome, time_out: int):
        """Constructor, takes a chrome driver instance and time out in milliseconds
        :param driver: Instance of Chrome WebDriver
        :param time_out: Number of milliseconds before time out
        """
        self._driver = driver
        self.time_out = int(time_out)

    def open_page(self, url: str):
        """Takes a url and call method to visit the page
        :param url: String with the url to visit
        """
        self._driver.get(url)

    def click_element(self, raw_locator: tuple):

        element = WebDriverWait(self._driver, self.time_out).until(
            EC.element_to_be_clickable(get_locator(raw_locator))
        )
        element.click()

    def click_element_js(self, raw_locator: tuple) -> bool:
        """Takes a locator and click the element through a script executed by the web browser
        :param raw_locator: Tuple with two strings for the strategy and selector
        """
        try:
            element = WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            self._driver.execute_script("arguments[0].click()", element)
            return True

    def input_text(self, raw_locator: tuple, text: str) -> bool:
        """Fill a input field with a string

        :param raw_locator: Field to fill. Tuple contains two strings for the strategy and selector.
        :param text: String to put into field
        :return: True if the field was found and filled. False if field was not found.
        """
        try:
            element = WebDriverWait(self._driver, self.time_out).until(EC.visibility_of_element_located(
                get_locator(raw_locator)
            ))
        except:
            return False
        else:
            element.send_keys(text)
            return True

    def element_is_visible(self, raw_locator: tuple) -> bool:
        """Checks if an element is visible

        :param raw_locator: Tuple contains two strings for the strategy and selector for the element to check
        :returns: True if the element is visible. False if the element is not visible.
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.visibility_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            return True

    def get_elements(self, raw_locator: tuple) -> list[WebElement]:
        """Gets elements by a given locator
        :param raw_locator: Tuple contains two strings for the strategy and selector for the elements
            to found
        :returns: A list with the web elements that meet the locator. A empty list if elements were not found
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_all_elements_located(get_locator(raw_locator))
            )
        except:
            return []
        else:
            return self._driver.find_elements(*get_locator(raw_locator))

    def get_element(self, raw_locator: tuple) -> WebElement:
        """Gets an element given by a locator
        :param raw_locator: Tuple contains two strings for the strategy and selector for the elements
            to found
        :returns: A web element. A None value if the element was not found
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return None
        else:
            return self._driver.find_element(*get_locator(raw_locator))

    def clear_text(self, raw_locator: tuple):
        """Clears an input field

        :param raw_locator: Tuple contains two strings for the strategy and selector for the input field
            to clear
        :return: True if the element was found. False when the element was not found
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            return self._driver.find_element(*get_locator(raw_locator)).clear()
            return True

    def get_element_visible(self, raw_locator: tuple) -> WebElement:
        """Gets a web element only if it's visible
        :param raw_locator: Tuple contains two strings for the strategy and selector for the element
            to get
        :returns: A web element. A None value if the element was not found or is not visible
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.visibility_of_element_located(get_locator(raw_locator))
            )
        except:
            return None
        else:
            return self._driver.find_element(*get_locator(raw_locator))

    def attach_file(self, file: str, raw_locator: tuple):
        """Attach a file in an input field

        :param file: Rout of the file to attach
        :param raw_locator: Tuple contains two strings for the strategy and selector for the input field
        :return: True if the field was found and the filed was sent. False if the field was not found
        """
        try:
            element = WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            element.send_keys(file)
            return True

    def element_is_invisible(self, raw_locator: tuple):
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.invisibility_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            return True

    def is_download_finished_in(self, seconds: int):
        try:
            WebDriverWait(self._driver, seconds).until(downloads_finished)
        except:
            return False
        else:
            return True
