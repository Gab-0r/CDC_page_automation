import time

from behave import step
from dotenv import load_dotenv
from pom.mcd_data_page import McdDataPage
import os


@step("the user clicks on Data request in Provisional Multiple Cause of Death Data section")
def clicks_on_data_request(context):
    mcd_data_page = McdDataPage(context.browser_interactions)
    mcd_data_page.go_to_mcd_data_request_page()


@step("the user clicks on Data request in Archive Final Multiple Case of Death 1999-2004 section")
def clicks_on_data_request_1999_2004(context):
    mcd_data_page = McdDataPage(context.browser_interactions)
    mcd_data_page.go_to_mcd_data_99_04()
