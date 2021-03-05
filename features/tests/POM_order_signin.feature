# Created by Ratna Sinha at 3/1/2021
Feature:  Main page

  Scenario: Logged out user sees Sign in page when clicking Orders
  Given Open Amazonmain page
  When Click Amazon Orders link
  Then Verify Sign In page is opened

