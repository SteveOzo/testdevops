import pytest
from hello import *

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_root(client):
    """Test the default route."""

    res = client.get('/hello/hola')
    assert b'Hello' in res.data
