import time

from utilities.browser_interactions import BrowserInteractions
from pom.locators.mcd_data_form_page_locators import McdDataFormPageLocators as locators
from pathlib import Path

def wait_download(path: str):
    secs = 0



class McdDataFormPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def fill_fields(self):
        # For Section 1: Organize table layout
        self.browser_interactions.click_element(locators.GROUP_RESULT_BY_SELECTOR)
        self.browser_interactions.click_element(locators.RESIDENCE_STATE_OPTION)
        self.browser_interactions.click_element(locators.AND_BY_1)
        self.browser_interactions.click_element(locators.YEAR_OPTION)
        self.browser_interactions.click_element(locators.AND_BY_2)
        self.browser_interactions.click_element(locators.MONTH_OPTION)

        # For Section 2: Select location
        self.browser_interactions.click_element(locators.RESIDENCE_STATES)

        # For Section 3: Select demographics
        self.browser_interactions.click_element(locators.TEN_YEAR_AGE_GROUPS)

        #For Section 4: Select time period of death
        self.browser_interactions.click_element(locators.YEAR_MONTH)

        #For Section 7: Select multiple cause of death
        self.browser_interactions.click_element(locators.MCD_ICD_10_CODES)

        #For Section 8: Other Options
        self.browser_interactions.click_element(locators.EXPORT_RESULTS_CB)
        self.browser_interactions.click_element(locators.SHOW_ZERO_VALUES_CB)
        self.browser_interactions.click_element(locators.SHOW_SUPPRESSED_VALUES_CB)

    def download_request(self):
        title_name = self.browser_interactions.get_element(locators.FORM_TITLE).text
        file_name = title_name.replace(" Request", ".txt")
        print(file_name)
        self.browser_interactions.click_element(locators.SEND_BUTTON)
        time.sleep(5)
        Path(f"/Users/juan.orozco/Downloads/{file_name}").rename(
            f"/Users/juan.orozco/Desktop/Test automation/CDC_page_automation/downloads/{title_name}")
        return file_name