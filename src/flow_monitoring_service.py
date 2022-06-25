# validate input and then call datastore
from http import HTTPStatus

from datastore.in_mem_datastore import InMemoryDatastore
from constants import Constants
from flowlog.flowlog import Flowlog
from error import FlowMonitoringError
from validation import Validation

class FlowMonitoringService:

    def __init__(self) -> None:
        self.store = InMemoryDatastore()

    def get(self, query_params):
        error = Validation.validate_get_args(query_params)
        if error is not None:
            return None, FlowMonitoringError(error.error_msg, error.code)
        hour = int(query_params.get(Constants.HOUR))
        flowlogs_for_hour = self.store.get(hour)
        if flowlogs_for_hour is None:
            return [], None
        result = []
        for flowlog in flowlogs_for_hour:
            result.append(flowlog.serialize_to_json())
        return result, None

    def put(self, request):
        request_data = request.json
        if request_data is None:
            request_data = request.get_json(force=True)
        if request_data is None:
            return FlowMonitoringError("Missing request data", HTTPStatus.BAD_REQUEST)
        flowlogs = []
    
        for item in request_data:
            json_dict = item
            error = Validation.validate_input_flow(flowlog=json_dict)
            if error is not None:
                return error
            flowlog = Flowlog.deserialize_from_json(json_dict)       
            flowlogs.append(flowlog)
        if len(flowlogs) == 0:
            return FlowMonitoringError("No flowlog found", HTTPStatus.BAD_REQUEST)
        for flowlog in flowlogs:
            self.store.put(flowlog)
