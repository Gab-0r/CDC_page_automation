Feature: 1999 to 2020 data download
  As a user
  I want to go to CDC page
  In order to download data from 1999 to 2020

Background: Go to request form
  Given the user go to CDC page
  Given the user clicks on Multiple Cause of Death (Provisional) option
  Given the user clicks on Data request in 1999-2020 option in Current Final Multiple Cause of Death Data section
  Given the user clicks on I agree button in About section

@1999-2020
Scenario: Make a request to download data from 1999 to 2020
  When the user fills the 1999-2020 form
  When the user clicks on send button
  Then the data is downloaded