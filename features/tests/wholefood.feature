# Created by Ratna Sinha at 2/15/2021
Feature: Test Scenarios for verifying presence of certain texts for products
  # Enter feature description here


  Scenario: Every product on the Wholefoods page has a text ‘Regular’ and a product name
    Given Open Wholefood page
    Then name of product is present
    And text "Regular" is present

