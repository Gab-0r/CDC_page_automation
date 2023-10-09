from behave import step
from dotenv import load_dotenv
from pom.mcd_data_form_page import McdDataFormPage
import os


@step("the user fills the form")
def fill_form(context):
    mcd_data_form_page = McdDataFormPage(context.browser_interactions)
    mcd_data_form_page.fill_fields()


@step("the user clicks on send button")
def click_send(context):
    pass

@step("the data is downloaded")
def check_downloaded_data(context):
    pass