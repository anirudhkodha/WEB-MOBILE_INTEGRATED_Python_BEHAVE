Feature: Member Actions in an Event

	@Login @Quickview @Logout
	Scenario: I Accept an event
		Given I am on the "Event" Tab for any LayoutView
		When I can tap on the plus button on top right corner to create an event
		Then I can fill the necerssary options to create an event and Assert it
		Then I am on the "Broadcast" Tab from any LayoutView
		Then I check and Assign


#  @Login @Quickviewa
#  Scenario: Accept an event
#    Given I am on the "Broadcast" Tab from Quickview
#    Then I can see my name under Attending
#    And I go back to the Quickview
#    When I tap on the event Option
#    Then I can see the option to assign to the team
#    And I Assign to my team
