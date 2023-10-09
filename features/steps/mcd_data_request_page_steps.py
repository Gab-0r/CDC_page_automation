from behave import step
from dotenv import load_dotenv
from pom.mcd_data_request_page import McdDataRequestPage
import os


@step("the user clicks on I agree button in About section")
def clicks_on_i_agree(context):
    mcd_data_request_page = McdDataRequestPage(context.browser_interactions)
    mcd_data_request_page.go_to_mcd_data_form_page()