Feature: Member Availibility Set and Check

  @Login @Quickview
  @test
  Scenario: Verify Member's Availability Set and Check on ACTIV MOBILE
    Given I click on the "Availability" icon at the bottom of the mobile screen
    When I see the "All Groups" option displays under the Availability title
    Then I can choose my availibility from the Top Nav Bar: SET
    Then I click on the Group Selector in the top right hand corner to view my assigned Groups
    Then I click on "Foundational Platforms" that assigned to me from the lis