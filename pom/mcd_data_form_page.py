import time

from utilities.browser_interactions import BrowserInteractions
from pom.locators.mcd_data_form_page_locators import McdDataFormPageLocators as locators
from pathlib import Path
from dotenv import load_dotenv
from utilities.functions import clean_downloaded_file
import os


load_dotenv()


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
        self.browser_interactions.click_element(locators.AND_BY_3)
        self.browser_interactions.click_element(locators.TEN_YEARS_OPTION)

        # For Section 2: Select location
        self.browser_interactions.click_element(locators.RESIDENCE_STATES)

        # For Section 3: Select demographics
        self.browser_interactions.click_element(locators.TEN_YEAR_AGE_GROUPS)

        # For Section 4: Select time period of death and select 2021, 2022 and 2023 years
        self.browser_interactions.click_element(locators.YEAR_MONTH)
        self.browser_interactions.click_element(locators.ALL_DATES_OPTION)
        self.browser_interactions.multi_select(locators.OPTION_2021, locators.OPTION_2022, locators.OPTION_2023)

        # For Section 7: Select multiple cause of death
        self.browser_interactions.click_element(locators.MCD_ICD_10_CODES)

        # For Section 8: Other Options
        self.browser_interactions.click_element(locators.EXPORT_RESULTS_CB)
        self.browser_interactions.click_element(locators.SHOW_ZERO_VALUES_CB)
        self.browser_interactions.click_element(locators.SHOW_SUPPRESSED_VALUES_CB)

    def download_request(self):
        title_name = self.browser_interactions.get_element(locators.FORM_TITLE).text
        file_name = title_name.replace(" Request", ".txt")
        self.browser_interactions.click_element(locators.SEND_BUTTON)
        self.browser_interactions.element_is_invisible(locators.PROGRESS_BAR)
        if self.browser_interactions.is_download_finished_in(60):
            user_home = os.path.expanduser("~")
            Path(f"{user_home}/Downloads/{file_name}").rename(
                os.getcwd() + f"/downloads/{file_name}"
            )
            file_name_without_spaces = file_name.replace(' ', '_')
            file_name_without_spaces = file_name_without_spaces.replace(',', '')
            clean_downloaded_file(file_name, file_name_without_spaces)
            return file_name_without_spaces
        else:
            return None

    def check_download(self, file_name):
        if os.path.exists(os.getcwd() + f"/downloads/{file_name}"):
            return True
        else:
            return False
