Feature: Data download
  As a user
  I want to go to CDC page
  In order to download data

Background: Go to request form
  Given the user go to CDC page
  Given the user clicks on Multiple Cause of Death (Provisional) option
  Given the user clicks on Data request in Provisional Multiple Cause of Death Data section
  Given the user clicks on I agree button in About section

Scenario: Make a request to download data
  When the user fills the form
  When the user clicks on send button
  Then the data is downloaded

