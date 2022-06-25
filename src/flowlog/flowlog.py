import json

from constants import Constants

class Flowlog:

    def __init__(self) -> None:
        self.src_app = None
        self.dest_app = None
        self.vpc_id = None
        self.bytes_tx = None
        self.bytes_rx = None
        self.hour = None

    def __init__(self, src_app = "", dest_app = "", vpc_id = "", bytes_tx = 0, bytes_rx = 0, hour = 0):
        self.src_app = src_app
        self.dest_app = dest_app
        self.vpc_id = vpc_id
        self.bytes_tx = bytes_tx
        self.bytes_rx = bytes_rx
        self.hour = hour 

    def increment_tx_rx_bytes(self, bytes_tx, bytes_rx):
        self.bytes_tx += bytes_tx
        self.bytes_rx += bytes_rx

    def get_src_app(self):
        return self.src_app

    def get_dest_app(self):
        return self.dest_app

    def get_vpc_id(self):
        return self.vpc_id
    
    def get_bytes_tx(self):
        return self.bytes_tx

    def get_bytes_rx(self):
        return self.bytes_rx

    def get_hour(self):
        return self.hour

    def serialize_to_json(self):
        return {
            Constants.SRC_APP : self.src_app,
            Constants.DEST_APP: self.dest_app,
            Constants.VPC_ID  : self.vpc_id,
            Constants.BYTES_TX: self.bytes_tx,
            Constants.BYTES_RX: self.bytes_rx,
            Constants.HOUR    : self.hour
        }

    def deserialize_from_json(json_dict):
        return Flowlog(
            json_dict[Constants.SRC_APP],
            json_dict[Constants.DEST_APP],
            json_dict[Constants.VPC_ID],
            json_dict[Constants.BYTES_TX],
            json_dict[Constants.BYTES_RX],
            json_dict[Constants.HOUR]
        )
    