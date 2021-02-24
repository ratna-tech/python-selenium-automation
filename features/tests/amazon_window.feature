# Created by Ratna Sinha at 2/22/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Applications
 Given Open Amazon T&C page
 When Store original windows
 And Click on Amazon applications link
 And Switch to the newly opened window
 Then Amazon app page is opened
 Then User can close new window and switch back to original