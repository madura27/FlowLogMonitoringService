import pytest

from datastore.in_mem_datastore import InMemoryDatastore
from flowlog.flowlog import Flowlog

src_app = "src_app"
dest_app = "dest_app"
vpc_id = "vpc_id"
bytes_rx = 100
bytes_tx = 150
hour = 10

@pytest.fixture
def datastore():
    store = InMemoryDatastore()
    return store

def test_basic(datastore: InMemoryDatastore):
    flowlog = Flowlog(src_app, dest_app, vpc_id, bytes_tx, bytes_rx, hour)
    datastore.put(flowlog)
    result = datastore.get(flowlog.get_hour())
    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 1
    actual = result[0]
    assert actual == flowlog

def test_not_present(datastore: InMemoryDatastore):
    result = datastore.get("10")
    assert result is None

def test_put_twice(datastore: InMemoryDatastore):
    flowlog = Flowlog(src_app, dest_app, vpc_id, bytes_tx, bytes_rx, hour)
    datastore.put(flowlog)
    datastore.put(flowlog)
    result = datastore.get(flowlog.get_hour())
    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 1
    actual = result[0]
    assert actual.get_src_app() == src_app
    assert actual.get_dest_app() == dest_app
    assert actual.get_vpc_id() == vpc_id
    assert actual.get_bytes_rx() == 2 * bytes_rx
    assert actual.get_bytes_tx() == 2 * bytes_tx
    assert actual.get_hour() == hour