import pytest
import socket
from app import *


@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_root(client):
    """Test the default route."""

    res = client.get('/hello/Juan')
    assert 'Juan' in str(res.data) and str(socket.gethostname()) in str(res.data)
