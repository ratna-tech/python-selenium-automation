# Created by Ratna Sinha at 3/2/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can add product to the cart
    Given Open AmazonFirst page
    When Input lego in searchbox
    When click onthe search icon
    And Select first1 lego on the page
    And click on the Add to Cart button
    Then number of the items added in the cart is displayed
