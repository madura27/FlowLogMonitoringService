from error import FlowMonitoringError
from http import HTTPStatus
from constants import Constants

class Validation:

    def __init__(self) -> None:
        pass

    def validate_input_flow(flowlog):

        if not isinstance(flowlog[Constants.SRC_APP], str):
            error = FlowMonitoringError("The src_app value must be a string", HTTPStatus.BAD_REQUEST)
            return error

        if not isinstance(flowlog[Constants.DEST_APP], str):
            error = FlowMonitoringError("The dest_app value must be a string", HTTPStatus.BAD_REQUEST)
            return error
        
        if not isinstance(flowlog[Constants.VPC_ID], str):
            error = FlowMonitoringError("The vpc_id value must be a string", HTTPStatus.BAD_REQUEST)
            return error

        try:
            bytes_tx = int(flowlog[Constants.BYTES_TX])
        except ValueError:
            error = FlowMonitoringError("The bytes_tx value must be an integer", HTTPStatus.BAD_REQUEST)
            return error
        
        if bytes_tx <= 0:
            error = FlowMonitoringError("The bytes_tx value must be positive", HTTPStatus.BAD_REQUEST)
            return error

        try:
            bytes_rx = int(flowlog[Constants.BYTES_RX])
        except ValueError:
            error = FlowMonitoringError("The bytes_rx value must be an integer", HTTPStatus.BAD_REQUEST)
            return error
        
        if bytes_rx <= 0:
            error = FlowMonitoringError("The bytes_rx value must be positive", HTTPStatus.BAD_REQUEST)
            return error

        try:
            hour = int(flowlog[Constants.HOUR])
        except ValueError:
             error = FlowMonitoringError("The hour value must be an integer", HTTPStatus.BAD_REQUEST)
             return error
        
        if hour <= 0:
            error = FlowMonitoringError("The hour value must be positive", HTTPStatus.BAD_REQUEST)
            return error

        return None

    def validate_get_args(query_params):
        if query_params is None:
            error = FlowMonitoringError("No query parameters found", HTTPStatus.BAD_REQUEST)
            return error
        if Constants.HOUR not in query_params:
            error = FlowMonitoringError("Missing hour parameter in the request query_params", HTTPStatus.BAD_REQUEST)
            return error
        hour = query_params.get(Constants.HOUR)
        # check if hour is integer; if not return error
        try:
            hour = int(hour)
        except ValueError:
             error = FlowMonitoringError("The hour value must be an integer", HTTPStatus.BAD_REQUEST)
             return error

        if hour <= 0:
            error = FlowMonitoringError("The hour value must be positive", HTTPStatus.BAD_REQUEST)
            return error





        

        


