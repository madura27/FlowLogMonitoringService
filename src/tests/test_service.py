from http import HTTPStatus
import pytest

from flow_monitoring_service import FlowMonitoringService
from constants import Constants
from error import FlowMonitoringError

@pytest.fixture
def service():
    return FlowMonitoringService()

def test_invalid_get_args(service):
    query_params = None
    response, error = service.get(query_params)
    assert response is None
    assert error is not None
    assert isinstance(error, FlowMonitoringError)
    assert error.error_msg == "No query parameters found"
    assert error.code == HTTPStatus.BAD_REQUEST

def test_hour_not_present(service):
    query_params = { Constants.HOUR : "1"}  # datastore is empty, so this doesn't exist
    response, error = service.get(query_params)
    assert response is not None
    assert error is None
    assert isinstance(response, list)
    assert len(response) == 0
 