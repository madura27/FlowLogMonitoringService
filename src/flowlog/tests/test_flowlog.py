import pytest

from flowlog.flowlog import Flowlog
from constants import Constants

src_app = "src_app"
dest_app = "dest_app"
vpc_id = "vpc_id"
bytes_rx = 100
bytes_tx = 150
hour = 10

@pytest.fixture
def sample_flowlog() -> Flowlog:
    flowlog = Flowlog(src_app, dest_app, vpc_id, bytes_tx, bytes_rx, hour)
    return flowlog

def test_constructor():
    flowlog = Flowlog()
    assert flowlog.get_src_app() == ""
    assert flowlog.get_dest_app() == ""
    assert flowlog.get_vpc_id() == ""
    assert flowlog.get_bytes_rx() == 0
    assert flowlog.get_bytes_tx() == 0
    assert flowlog.get_hour() == 0

def test_constructor_with_args(sample_flowlog: Flowlog):
    assert sample_flowlog.get_src_app() == src_app
    assert sample_flowlog.get_dest_app() == dest_app
    assert sample_flowlog.get_vpc_id() == vpc_id
    assert sample_flowlog.get_bytes_rx() == bytes_rx
    assert sample_flowlog.get_bytes_tx() == bytes_tx
    assert sample_flowlog.get_hour() == hour

def test_increment(sample_flowlog: Flowlog):
    increment = 1000
    sample_flowlog.increment_tx_rx_bytes(increment, increment)
    assert sample_flowlog.get_bytes_rx() == bytes_rx + increment
    assert sample_flowlog.get_bytes_tx() == bytes_tx + increment

def test_serialize(sample_flowlog: Flowlog):
    serialized = sample_flowlog.serialize_to_json()
    assert isinstance(serialized, dict)
    assert Constants.SRC_APP in serialized and serialized.get(Constants.SRC_APP) == src_app
    assert Constants.DEST_APP in serialized and serialized.get(Constants.DEST_APP) == dest_app
    assert Constants.VPC_ID in serialized and serialized.get(Constants.VPC_ID) == vpc_id
    assert Constants.BYTES_RX in serialized and serialized.get(Constants.BYTES_RX) == bytes_rx
    assert Constants.BYTES_TX in serialized and serialized.get(Constants.BYTES_TX) == bytes_tx
    assert Constants.HOUR in serialized and serialized.get(Constants.HOUR) == hour

def test_deserialize():
    json_dict = {
        Constants.SRC_APP : "foo",
        Constants.DEST_APP: "bar",
        Constants.VPC_ID  : "vpc",
        Constants.BYTES_RX: "100",
        Constants.BYTES_TX: "100",
        Constants.HOUR    : "5"
    }
    flowlog: Flowlog = Flowlog.deserialize_from_json(json_dict)
    assert flowlog.get_src_app() == "foo"
    assert flowlog.get_dest_app() == "bar"
    assert flowlog.get_vpc_id() == "vpc"
    assert flowlog.get_bytes_rx() == "100"
    assert flowlog.get_bytes_tx() == "100"
    assert flowlog.get_hour() == "5"

def test_serialize_deserialize(sample_flowlog: Flowlog):
    serialized = sample_flowlog.serialize_to_json()
    deserialized = Flowlog.deserialize_from_json(serialized)
    assert sample_flowlog.get_src_app() == deserialized.get_src_app()
    assert sample_flowlog.get_dest_app() == deserialized.get_dest_app()
    assert sample_flowlog.get_vpc_id() == deserialized.get_vpc_id()
    assert sample_flowlog.get_bytes_rx() == deserialized.get_bytes_rx()
    assert sample_flowlog.get_bytes_tx() == deserialized.get_bytes_tx()
    assert sample_flowlog.get_hour() == deserialized.get_hour()