# Created by Ratna Sinha at 2/11/2021
Feature: Test Scenarios for Cancel functionality
  # Enter feature description here


  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input lego into search
    And click on the search icon
    And Select first lego on page
    And click on Add to Cart button
    Then number of items added in the cart is displayed