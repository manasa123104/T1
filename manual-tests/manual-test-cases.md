# Manual test cases (functional testing)

Domain: IoT | Application URL: http://localhost:8080 | Written from the user stories

Run each case by hand in the browser (or with a REST client). Record Pass or Fail and any notes. Do the preconditions first, then follow the numbered steps, then compare with the expected result.

| ID | Title | Result |
|---|---|---|
| TC-001 | Valid request is submitted | Pass / Fail |
| TC-002 | Missing details | Pass / Fail |
| TC-003 | Approve a request | Pass / Fail |
| TC-004 | Cannot approve my own request | Pass / Fail |
| TC-005 | Reject needs a reason | Pass / Fail |
| TC-006 | Actions are logged | Pass / Fail |

## TC-001: Valid request is submitted

**Story:** Submit a device provisioning (IoT) request

**Preconditions**
- I am a signed-in device owner

**Steps**
1. I submit a device provisioning (IoT) request with all required details

**Expected result**
- the request is saved with status SUBMITTED and a reference number
- I see a confirmation with the reference number

**Actual result / notes:** ____________________

## TC-002: Missing details

**Story:** Submit a device provisioning (IoT) request

**Preconditions**
- The application is running at http://localhost:8080

**Steps**
1. I submit the request without details

**Expected result**
- it is rejected with "Details are required"

**Actual result / notes:** ____________________

## TC-003: Approve a request

**Story:** Review and approve

**Preconditions**
- a SUBMITTED request raised by someone else

**Steps**
1. I approve it

**Expected result**
- its status becomes APPROVED and my name is recorded

**Actual result / notes:** ____________________

## TC-004: Cannot approve my own request

**Story:** Review and approve

**Preconditions**
- a SUBMITTED request that I raised

**Steps**
1. I try to approve it

**Expected result**
- it is rejected with "Requester cannot approve their own request"

**Actual result / notes:** ____________________

## TC-005: Reject needs a reason

**Story:** Review and approve

**Preconditions**
- The application is running at http://localhost:8080

**Steps**
1. I reject a request without a reason

**Expected result**
- it is rejected with "A reason is required to reject a request"

**Actual result / notes:** ____________________

## TC-006: Actions are logged

**Story:** Audit trail

**Preconditions**
- a request was submitted and approved

**Steps**
1. I open its audit trail

**Expected result**
- I see both actions with who did them and when

**Actual result / notes:** ____________________
