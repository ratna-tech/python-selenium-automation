# Created by Ratna Sinha at 2/11/2021
Feature: Test Scenarios for Cancel functionality
  # Enter feature description here


  Scenario: User can cancel a product
    Given Open Amazon cancel order page
    When Input Cancel order into search box
    And Tap on Enter key
    Then Page for Cancel Items or Orders is displayed
