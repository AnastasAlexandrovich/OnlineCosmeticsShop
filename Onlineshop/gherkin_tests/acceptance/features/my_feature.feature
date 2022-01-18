Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
        | name      |
        | Loreal     |
        | Paris     |
      When we implement a test
      Then behave will test it for us!