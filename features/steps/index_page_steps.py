from behave import step
from dotenv import load_dotenv
from pom.index_page import IndexPage
import os

load_dotenv()


@step("the user go to CDC page")
def go_to_cdc_page(context):
    index_page = IndexPage(context.browser_interactions)
    index_page.open_index_page(os.getenv("URL"))


@step("the user clicks on Multiple Cause of Death (Provisional) option")
def click_on_mcd_provisional(context):
    index_page = IndexPage(context.browser_interactions)
    index_page.go_to_mcd_data_page()



