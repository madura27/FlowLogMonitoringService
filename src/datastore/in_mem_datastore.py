from datastore.datastore import Datastore
from flowlog.flowlog import Flowlog

class InMemoryDatastore(Datastore):
    
    def __init__(self):
        self.store = dict()

    def get(self, time):
        if time not in self.store:
            return None
        inner_dict = self.store.get(time)
        flowlogs = []
        for k,v in inner_dict.items():
            flowlogs.append(v)
        return flowlogs

    def put(self, flowlog:Flowlog):
        existingMapForHour = self.store.get(flowlog.get_hour(), dict()) # map of [unique combi : flowlog]
        uniqueKey = flowlog.get_src_app()+flowlog.get_dest_app()+flowlog.get_vpc_id()
        if uniqueKey not in existingMapForHour:
            existingMapForHour[uniqueKey] = flowlog
        else:
            existingFlowLog: Flowlog = existingMapForHour.get(uniqueKey)
            existingFlowLog.increment_tx_rx_bytes(flowlog.bytes_tx, flowlog.bytes_rx)
            existingMapForHour[uniqueKey] = existingFlowLog
        self.store[flowlog.get_hour()] = existingMapForHour
