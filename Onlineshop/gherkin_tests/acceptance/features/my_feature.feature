Feature: showing off behave

  Scenario: get a product by id
     Given create products
      When user gets product
    |id|
    |1 |
      Then validate results


  Scenario: get a list of orders
    Given prepare data
    When user gets orders
    Then validate orders