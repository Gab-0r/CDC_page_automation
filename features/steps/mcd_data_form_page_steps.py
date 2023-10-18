import time

from behave import step
from dotenv import load_dotenv
from pom.mcd_data_form_page import McdDataFormPage
import os
from utilities.functions import *


@step("the user fills the form")
def fill_form(context):
    mcd_data_form_page = McdDataFormPage(context.browser_interactions)
    mcd_data_form_page.fill_fields()


@step("the user clicks on send button")
def click_send(context):
    mcd_data_form_page = McdDataFormPage(context.browser_interactions)
    context.file_name = mcd_data_form_page.download_request()


@step("the data is downloaded")
def check_downloaded_data(context):
    mcd_data_form_page = McdDataFormPage(context.browser_interactions)
    assert mcd_data_form_page.check_download(context.file_name), "file downloaded not found"
    upload_file_to_blob(context.file_name)


@step("the user fills the form of 1999-2004")
def fill_form_1999_2004(context):
    mcd_data_form_page = McdDataFormPage(context.browser_interactions)
    mcd_data_form_page.fill_fields_1999_2004()
