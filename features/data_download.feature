Feature: Data download
  As a user
  I want to go to CDC page
  In order to download data

Background: Go to request form
  Given the user go to CDC page
  Given the user go to data request form

Scenario: Make a request to download data
  When the user fills the form
  When the user clicks on send button
  Then the data is downloaded
