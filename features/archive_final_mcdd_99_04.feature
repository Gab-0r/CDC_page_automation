Feature: Download data from archive final mcdd from 1999-2004
  As a user
  I want to go to CDC page
  In order to download data

  Background: Go to request form
    Given the user go to CDC page
    Given the user clicks on Multiple Cause of Death (Provisional) option
    Given the user clicks on Data request in Archive Final Multiple Case of Death 1999-2004 section
    Given the user clicks on I agree button in About section

  Scenario: Make a request to download
    When the user fills the form of 1999-2004
    When the user clicks on send button
    Then the data is downloaded
