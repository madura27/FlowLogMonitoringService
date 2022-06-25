from http import HTTPStatus
import pytest
from error import FlowMonitoringError
from validation import Validation
from constants import Constants

arg_input_valid = {
    Constants.HOUR : "1"
}
arg_input_invalid_non_int = {
    Constants.HOUR : "abc"
}
arg_input_invalid_negative = {
    Constants.HOUR : "-7"
}

@pytest.fixture
def flow_dict():
    flow_dict = {
        Constants.SRC_APP : "foo", 
        Constants.DEST_APP: "bar", 
        Constants.VPC_ID  : "vpc-0", 
        Constants.BYTES_TX: "100", 
        Constants.BYTES_RX: "300", 
        Constants.HOUR    : "1"
    }


    return flow_dict

def test_validation_valid_input(flow_dict):
    assert Validation.validate_input_flow(flow_dict) == None

def test_validation_invalid_bytes_rx(flow_dict):
    flow_dict[Constants.BYTES_RX] = "abc"
    result = Validation.validate_input_flow(flow_dict)
    assert  result != None
    assert isinstance(result, FlowMonitoringError)
    expected_err_msg = "The bytes_rx value must be an integer"
    expected_err_code = HTTPStatus.BAD_REQUEST
    assert result.error_msg == expected_err_msg
    assert result.code == expected_err_code

def test_validation_invalid_bytes_tx(flow_dict):
    flow_dict[Constants.BYTES_TX] = "abc"
    result = Validation.validate_input_flow(flow_dict)
    assert  result != None
    assert isinstance(result, FlowMonitoringError)
    expected_err_msg = "The bytes_tx value must be an integer"
    expected_err_code = HTTPStatus.BAD_REQUEST
    assert result.error_msg == expected_err_msg
    assert result.code == expected_err_code

def test_validation_invalid_hour(flow_dict):
    flow_dict[Constants.HOUR] = "abc"
    result = Validation.validate_input_flow(flow_dict)
    assert  result != None
    assert isinstance(result, FlowMonitoringError)
    expected_err_msg = "The hour value must be an integer"
    expected_err_code = HTTPStatus.BAD_REQUEST
    assert result.error_msg == expected_err_msg
    assert result.code == expected_err_code

def test_validate_get_args_valid_hour():
    result = Validation.validate_get_args(arg_input_valid)
    assert result == None

def test_validate_get_args_invalid_hour_non_int():
    result = Validation.validate_get_args(arg_input_invalid_non_int)
    expected_err_msg = "The hour value must be an integer"
    expected_err_code = HTTPStatus.BAD_REQUEST
    assert result != None
    assert result.code == expected_err_code
    assert result.error_msg == expected_err_msg

def test_validate_get_args_invalid_hour_negative():
    result = Validation.validate_get_args(arg_input_invalid_negative)
    expected_err_msg = "The hour value must be positive"
    expected_err_code = HTTPStatus.BAD_REQUEST
    assert result != None
    assert result.code == expected_err_code
    assert result.error_msg == expected_err_msg

def test_validate_get_args_invalid_hour_missing():
    arg_input = {}
    result = Validation.validate_get_args(arg_input)
    expected_err_msg = "Missing hour parameter in the request query_params"
    expected_err_code = HTTPStatus.BAD_REQUEST
    assert result != None
    assert result.code == expected_err_code
    assert result.error_msg == expected_err_msg




