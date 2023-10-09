from utilities.browser_interactions import BrowserInteractions
from utilities.web_driver import WebDriverManager


def before_scenario(context, scenario):
    web_driver = WebDriverManager("Chrome").create_driver()
    context.browser_interactions = BrowserInteractions(web_driver, 10)