import pytest

from referentielijsten_api_client.client import ReferentielijstenClient

from .helpers import NoServiceConfigured, ReferentielijstenService


def test_client(client):
    assert isinstance(client, ReferentielijstenClient)


def test_client_raises_if_no_settings():
    service = ReferentielijstenService(_api_url="")
    with pytest.raises(NoServiceConfigured) as excinfo:
        service.client_factory()
    assert "API service not configured" in str(excinfo.value)


@pytest.mark.vcr()
def test_valid_client_connection(client):
    assert client.can_connect


def test_invalid_client_connection(client):
    client.base_url = "http://testserver"
    assert not client.can_connect

    client.base_url = None
    assert not client.can_connect

    client.base_url = ""
    assert not client.can_connect
