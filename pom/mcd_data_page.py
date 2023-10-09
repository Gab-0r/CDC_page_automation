from utilities.browser_interactions import BrowserInteractions
from pom.locators.mcd_data_page_locators import McdDataPageLocators
from pom.mcd_data_request_page import McdDataRequestPage


class McdDataPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_mcd_page(self, url: str):
        self.browser_interactions.open_page(url)

    def go_to_mcd_data_request_page(self):
        self.browser_interactions.click_element(McdDataPageLocators.DATA_REQUEST_BUTTON)
        return McdDataRequestPage(self.browser_interactions)