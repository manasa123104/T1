"""pytest suite for app.device_provisioning (IoT)."""
from datetime import datetime, timezone

import pytest

from app.device_provisioning import MAX_DETAILS, DeviceProvisioningError, DeviceProvisioningService, DeviceProvisioningStatus

FIXED = datetime(2026, 1, 1, tzinfo=timezone.utc)


@pytest.fixture
def service():
    return DeviceProvisioningService(clock=lambda: FIXED)


def test_submit_creates_submitted_request_with_reference(service):
    # Proves a valid request is saved with status SUBMITTED and a reference number.
    request = service.submit("alice", "Need approval")
    assert request.status is DeviceProvisioningStatus.SUBMITTED
    assert request.reference == "IOT-000001"
    assert service.find(request.reference) is request


@pytest.mark.parametrize("who, details, message", [
    ("", "x", "Requester is required"),
    ("alice", "  ", "Details are required"),
    ("alice", "x" * (MAX_DETAILS + 1), "at most"),
])
def test_submit_validates_input(service, who, details, message):
    # Proves invalid submissions are rejected with a clear message.
    with pytest.raises(DeviceProvisioningError, match=message):
        service.submit(who, details)


def test_reviewer_can_approve(service):
    request = service.submit("alice", "Need approval")
    approved = service.approve(request.reference, "bob")
    assert approved.status is DeviceProvisioningStatus.APPROVED
    assert approved.decided_by == "bob"


def test_requester_cannot_approve_own_request(service):
    # Proves the four-eyes rule.
    request = service.submit("alice", "Need approval")
    with pytest.raises(DeviceProvisioningError, match="cannot approve their own request"):
        service.approve(request.reference, "ALICE")


def test_reject_needs_a_reason(service):
    request = service.submit("alice", "Need approval")
    with pytest.raises(DeviceProvisioningError, match="reason is required"):
        service.reject(request.reference, "bob", " ")
    rejected = service.reject(request.reference, "bob", "Missing documents")
    assert rejected.status is DeviceProvisioningStatus.REJECTED
    assert rejected.decision_note == "Missing documents"


def test_decisions_are_final(service):
    request = service.submit("alice", "Need approval")
    service.approve(request.reference, "bob")
    with pytest.raises(DeviceProvisioningError, match="already APPROVED"):
        service.reject(request.reference, "carol", "Too late")


def test_unknown_reference_is_reported(service):
    with pytest.raises(DeviceProvisioningError, match="Request not found"):
        service.find("NOPE")


def test_audit_trail_records_every_action(service):
    request = service.submit("alice", "Need approval")
    service.approve(request.reference, "bob")
    trail = service.audit_trail()
    assert len(trail) == 2
    assert "SUBMITTED by alice" in trail[0]
    assert "APPROVED by bob" in trail[1]
