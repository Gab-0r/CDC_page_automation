from utilities.browser_interactions import BrowserInteractions
from pom.locators.index_page_locators import IndexPageLocators
from pom.mcd_data_page import McdDataPage


class IndexPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_index_page(self, url: str):
        self.browser_interactions.open_page(url)

    def go_to_mcd_data_page(self):
        self.browser_interactions.click_element(IndexPageLocators.MCD_PROVISIONAL_BUTTON)
        return McdDataPage(self.browser_interactions)


