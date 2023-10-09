from utilities.browser_interactions import BrowserInteractions


class McdDataRequestPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_mcd_data_request_page(self, url: str):
        self.browser_interactions.open_page(url)
