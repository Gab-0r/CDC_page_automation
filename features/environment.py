from utilities.browser_interactions import BrowserInteractions
from utilities.web_driver import WebDriverManager
import os
from dotenv import load_dotenv

load_dotenv()


def before_scenario(context, scenario):
    web_driver = WebDriverManager(os.getenv("CHROME_NAME"), float(os.getenv("LOAD_TIMEOUT"))).create_driver()
    context.browser_interactions = BrowserInteractions(web_driver, 10)