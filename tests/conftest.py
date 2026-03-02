from django.core.cache import cache

import pytest

from .helpers import ReferentielijstenService

API_URL: str = "http://localhost:8004/api/v1"


@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()
    yield
    cache.clear()


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "match_on": ["method", "scheme", "host", "port", "path", "query"],
    }


@pytest.fixture()
def client():
    service = ReferentielijstenService(_api_url=API_URL)
    return service.client_factory()
