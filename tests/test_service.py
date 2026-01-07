import pytest

from referentielijsten_api_client.client import ReferentielijstenClient

from .helpers import NoServiceConfigured, ReferentielijstenService


def test_client(client):
    assert isinstance(client, ReferentielijstenClient)


def test_client_raises_if_no_settings():
    service = ReferentielijstenService(_api_root="", _api_path="", _api_token="")
    with pytest.raises(NoServiceConfigured) as excinfo:
        service.client_factory()
    assert "API service not configured" in str(excinfo.value)


@pytest.mark.vcr()
def test_client_connection(client):
    assert client.can_connect
