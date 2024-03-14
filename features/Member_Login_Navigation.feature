@web
Feature: Activ onboard
	@Login
	Scenario: Member Login and Logout
		Given I login to rfs activ as a member
		Then I logout as a member


#
#  @Login @Quickview
#  Scenario: Contact validations
#    Given I can see Group Member contacts on as Activ user
#    Then I verify the contact details for any Member