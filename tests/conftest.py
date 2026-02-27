import pytest

from .helpers import ReferentielijstenService

API_ROOT: str = "http://localhost:8004"
API_PATH: str = "/api/v1"
API_TOKEN: str = "b2eb1da9861da88743d72a3fb4344288fe2cba44"


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "match_on": [
            "method",
            "scheme",
            "host",
            "port",
            "path",
            "query",
            # "body",
        ],
    }


@pytest.fixture()
def client():
    service = ReferentielijstenService(
        _api_root=API_ROOT, _api_path=API_PATH, _api_token=API_TOKEN
    )
    return service.client_factory()
