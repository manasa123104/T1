"""UI tests for DeviceProvisioning: one test per acceptance-criteria scenario."""
from pages.device_provisioning_page import DeviceProvisioningPage


# Scenario: Valid request is submitted
def test_valid_request_is_submitted(driver, base_url):
    # Given I am a signed-in device owner
    # When I submit a device provisioning (IoT) request with all required details
    # Then the request is saved with status SUBMITTED and a reference number
    # And I see a confirmation with the reference number
    page = DeviceProvisioningPage(driver).open(base_url)
    assert page.title()  # TODO: drive the steps above through the page object


# Scenario: Missing details
def test_missing_details(driver, base_url):
    # When I submit the request without details
    # Then it is rejected with "Details are required"
    page = DeviceProvisioningPage(driver).open(base_url)
    assert page.title()  # TODO: drive the steps above through the page object


# Scenario: Approve a request
def test_approve_a_request(driver, base_url):
    # Given a SUBMITTED request raised by someone else
    # When I approve it
    # Then its status becomes APPROVED and my name is recorded
    page = DeviceProvisioningPage(driver).open(base_url)
    assert page.title()  # TODO: drive the steps above through the page object


# Scenario: Cannot approve my own request
def test_cannot_approve_my_own_request(driver, base_url):
    # Given a SUBMITTED request that I raised
    # When I try to approve it
    # Then it is rejected with "Requester cannot approve their own request"
    page = DeviceProvisioningPage(driver).open(base_url)
    assert page.title()  # TODO: drive the steps above through the page object


# Scenario: Reject needs a reason
def test_reject_needs_a_reason(driver, base_url):
    # When I reject a request without a reason
    # Then it is rejected with "A reason is required to reject a request"
    page = DeviceProvisioningPage(driver).open(base_url)
    assert page.title()  # TODO: drive the steps above through the page object


# Scenario: Actions are logged
def test_actions_are_logged(driver, base_url):
    # Given a request was submitted and approved
    # When I open its audit trail
    # Then I see both actions with who did them and when
    page = DeviceProvisioningPage(driver).open(base_url)
    assert page.title()  # TODO: drive the steps above through the page object
