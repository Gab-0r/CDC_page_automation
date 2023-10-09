from behave import step
from dotenv import load_dotenv
from pom.mcd_data_page import McdDataPage
import os


@step("the user go to data request form")
def go_to_data_request_form(context):
    mcd_data_page = McdDataPage(context.browser_interactions)
    mcd_data_page.go_to_mcd_data_request_page()

