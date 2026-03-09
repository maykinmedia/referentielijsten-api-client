import datetime
from dataclasses import asdict

import pytest
from freezegun import freeze_time


@pytest.mark.vcr()
def test_get_all_tables(client):
    tables = client.get_all_tables()
    assert [asdict(t) for t in tables] == [
        {
            "code": "item-not-geldig-anymore",
            "name": "Tabel that contains item not geldig anymore",
            "expires_on": None,
        },
        {
            "code": "not-geldig-anymore",
            "name": "Tabel that is not geldig anymore",
            "expires_on": datetime.datetime(2020, 2, 3, 8, 48, 49, tzinfo=datetime.UTC),
        },
        {
            "code": "tabel-with-many-items",
            "name": "Tabel with many items",
            "expires_on": None,
        },
        {
            "code": "tabel1",
            "name": "Tabel1",
            "expires_on": None,
        },
    ]


@pytest.mark.vcr()
def test_get_table(client):
    table = client.get_table("tabel1")
    assert asdict(table) == {
        "code": "tabel1",
        "name": "Tabel1",
        "expires_on": None,
    }


@pytest.mark.vcr()
def test_get_table_does_not_exist(client):
    table = client.get_table("table_does_not_exist")
    assert table is None


@freeze_time("2020-02-04")
@pytest.mark.vcr()
def test_table_properties(client):
    # not is_expired and not is_nearly_expired
    table = client.get_table("tabel1")
    assert not table.is_expired
    assert not table.is_nearly_expired

    # is_expired and is_nearly_expired
    table = client.get_table("not-geldig-anymore")
    assert table.expires_on == datetime.datetime(
        2020, 2, 3, 8, 48, 49, tzinfo=datetime.UTC
    )
    assert table.is_expired
    assert table.is_nearly_expired
