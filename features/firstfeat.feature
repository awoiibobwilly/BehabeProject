Feature: Visualizing Refactory Academy Logo
  Scenario: The Presence of Refactory Academy Logo
    Given launch google chrome browser
    When open refactory academy homepage
    Then verify that the refactory logo is on the page
    And close the browser
