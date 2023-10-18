class McdDataFormPageLocators:
    FORM_TITLE = ("XPATH", "//div[@class='title']/h1")
    GROUP_RESULT_BY_SELECTOR = ("ID", "SB_1")
    RESIDENCE_STATE_OPTION = ("XPATH", "//select[@id='SB_1']/optgroup/option[@value='D176.V9-level1']")
    AND_BY_1 = ("ID", "SB_2")
    YEAR_OPTION = ("XPATH", "//select[@id='SB_2']/optgroup/option[@value='D176.V1-level1']")
    AND_BY_2 = ("ID", "SB_3")
    MONTH_OPTION = ("XPATH", "//select[@id='SB_3']/optgroup/option[@value='D176.V1-level2']")
    AND_BY_3 = ("ID", "SB_4")
    TEN_YEARS_OPTION = ("XPATH", "//select[@id='SB_4']/optgroup/option[@value='D176.V5']")
    AND_BY_4 = ("ID", "SB_5")
    RESIDENCE_STATES = ("ID", "RO_locationD176.V9")
    TEN_YEAR_AGE_GROUPS = ("ID", "RO_ageD176.V5")
    YEAR_MONTH = ("ID", "RO_datesYEAR")
    MCD_ICD_10_CODES = ("ID", "RO_mcdD176.V13")
    EXPORT_RESULTS_CB = ("ID", "export-option")
    SHOW_TOTALS_CB = ("ID", "CO_show_totals")
    SHOW_ZERO_VALUES_CB = ("ID", "CO_show_zeros")
    SHOW_SUPPRESSED_VALUES_CB = ("ID", "CO_show_suppressed")
    SEND_BUTTON = ("XPATH", "//div[@class='footer-buttons']/input[@value='Send']")
    PROGRESS_BAR = ("ID", "progress-bar")
    OPTION_2021 = ("XPATH", "//select[@id='codes-D176.V1']/option[@value='2021']")
    OPTION_2022 = ("CSS", "select[id='codes-D176.V1'] > option[value='2022']")
    OPTION_2023 = ("CSS", "select[id='codes-D176.V1'] > option[value='2023']")
    ALL_DATES_OPTION = ("CSS", "select[id='codes-D176.V1'] > option[value='*All*']")
    CENSUS_REGION = ("CSS", "select[id='SB_1'] > optgroup > option[value='D77.V10-level1']")
    STATES_OPTION = ("CSS", "input[id='RO_locationD77.V9']")
    URBANIZATION_2013 = ("CSS", "input[id='RO_urbanD77.V19']")
    TEN_YEARS_GROUP_1999_2020 = ("CSS", "input[id='RO_ageD77.V5']")
    ALL_DATES_OPTION_1999_2020 = ("CSS", "select[id='codes-D77.V1'] > option[value='*All*']")
    MCD_ICD_10_CODES_1999_2020 = ("CSS", "input[id='RO_mcdD77.V13']")
    YEAR_OPTION_1999_2020 = ("CSS", "select[id='SB_2'] > optgroup > option[value='D77.V1-level1']")
    MONTH_OPTION_1999_2020 = ("CSS", "select[id='SB_3'] > optgroup > option[value='D77.V1-level2']")
