# Created by Ratna Sinha at 3/2/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon_main page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present

