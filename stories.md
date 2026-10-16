# Feature: Device provisioning (IoT)
Domain: IoT

## Story 1: Submit a device provisioning (IoT) request
As a device owner, I want to raise a device provisioning (IoT) request online, so that it is handled quickly without paperwork.

### Acceptance criteria
Scenario: Valid request is submitted
  Given I am a signed-in device owner
  When I submit a device provisioning (IoT) request with all required details
  Then the request is saved with status SUBMITTED and a reference number
  And I see a confirmation with the reference number

Scenario: Missing details
  When I submit the request without details
  Then it is rejected with "Details are required"

## Story 2: Review and approve
As a IoT platform operator, I want a supervisor to approve or reject each request, so that we meet the IoT approval and audit requirements.

### Acceptance criteria
Scenario: Approve a request
  Given a SUBMITTED request raised by someone else
  When I approve it
  Then its status becomes APPROVED and my name is recorded

Scenario: Cannot approve my own request
  Given a SUBMITTED request that I raised
  When I try to approve it
  Then it is rejected with "Requester cannot approve their own request"

Scenario: Reject needs a reason
  When I reject a request without a reason
  Then it is rejected with "A reason is required to reject a request"

## Story 3: Audit trail
As a IoT platform operator, I want every action on a device provisioning (IoT) request to be logged, so that we can answer audits and disputes.

### Acceptance criteria
Scenario: Actions are logged
  Given a request was submitted and approved
  When I open its audit trail
  Then I see both actions with who did them and when

## Assumptions
- Requirement as given: "Device provisioning (IoT)
- A device owner starts the 'device provisioning' journey by entering the required details and receives a unique reference number.
- Mandatory fields, valid ranges and domain limits are validated; invalid requests are rejected with a clear reason.
- A IoT platform operator reviews the request and approves, rejects or asks for more information, with a comment; the person who raised it cannot approve it.
- Business rules to respect: device provisioning, telemetry ingestion, firmware updates (OTA), alerts and rules, device security.
- The device owner can follow the status and is notified at each change; cancelling is allowed until approval.
- Every action is written to an audit trail with user, time and outcome.
- Related flows to consider later: Sensor alert rule; Firmware update rollout.".
- Only SUBMITTED requests can be approved or rejected; decisions are final.
- Details are limited to 500 characters.
