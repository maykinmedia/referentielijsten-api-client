from dataclasses import asdict

from django.core.cache import cache

import pytest


@pytest.mark.vcr()
def test_get_items_for_table(client):
    table_code = "tabel1"
    items = client.get_items_for_table(table_code)
    assert [asdict(i) for i in items] == [
        {"code": "option2", "name": "Option 2", "expires_on": None},
        {"code": "option1", "name": "Option 1", "expires_on": None},
    ]


@pytest.mark.vcr()
def test_get_items_for_table_cached(client, vcr_cassette):
    table_code = "tabel1"
    cache_key = f"referentielijsten_lists|get_items_for_table|code:{table_code}"

    assert cache.get(cache_key) is None

    items = client.get_items_for_table_cached(table_code)

    assert [asdict(i) for i in items] == [
        {"code": "option2", "name": "Option 2", "expires_on": None},
        {"code": "option1", "name": "Option 1", "expires_on": None},
    ]

    cached_value = cache.get(cache_key)

    assert cached_value is not None
    assert [asdict(i) for i in cached_value] == [
        {"code": "option2", "name": "Option 2", "expires_on": None},
        {"code": "option1", "name": "Option 1", "expires_on": None},
    ]

    # test n requests
    client.get_items_for_table_cached(table_code)
    client.get_items_for_table_cached(table_code)
    client.get_items_for_table_cached(table_code)
    assert len(vcr_cassette.requests) == 1
