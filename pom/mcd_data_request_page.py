from utilities.browser_interactions import BrowserInteractions
from pom.locators.mcd_data_request_page_locators import McdDataRequestPageLocators
from pom.mcd_data_form_page import McdDataFormPage


class McdDataRequestPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def go_to_mcd_data_form_page(self):
        self.browser_interactions.click_element(McdDataRequestPageLocators.I_AGREE_BUTTON)
        return McdDataFormPage(self.browser_interactions)
