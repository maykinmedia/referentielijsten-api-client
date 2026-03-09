==========
Quickstart
==========

Installation
============

Install the package from PyPI using pip:

.. code-block:: bash

    pip install referentielijsten-api-client

Usage
=====

First, import and initialize the client with your API endpoint:

.. code-block:: python

    from referentielijsten_api_client.client import ReferentielijstenClient

    client = ReferentielijstenClient(
        base_url="https://api.example.com/api/v1/",  # replace with your API root url
    )

Listing all available tables
----------------------------

You can retrieve a list of all tables available in the Referentielijsten API:

.. code-block:: python

    tables = client.get_all_tables()

**Example output:**

.. code-block:: python

    [
        Table(
            code="tabel1",
            name="Tabel 1",
            expires_on=None,
        ),
        Table(
            code="tabel2",
            name="Tabel 2",
            expires_on=datetime.datetime(2026, 1, 1, 0, 0, 0),
        ),
    ]

Get a Table
-----------

You can retrieve a specific table from the Referentielijsten API by providing its table code:

.. code-block:: python

    table = client.get_table("table_code")


**Example output:**

.. code-block:: python

    Table(code='tabel1', name='Tabel1', expires_on=None)

Get Items from a Table
----------------------

You can retrieve all items from a specific table using the client:

.. code-block:: python

    items = client.get_items_for_table("table_code")


**Example output:**

.. code-block:: python

    [
        TableItem(code="option1", name="Option 1", expires_on=None),
        TableItem(code="option2", name="Option 2", expires_on=None),
    ]

Get Items from a Table (Cached)
-------------------------------

You can retrieve all items from a specific table using the cached version of the client method.

.. code-block:: python

    items = client.get_items_for_table_cached("table_code")

Reference
---------

See the :ref:`client-reference` for full details, method signatures, and usage examples.


Testing
=======

This library includes automated tests to ensure the client works correctly with the Referentielijsten API.
Tests cover retrieval of tables, items, cached behavior, and client initialization.

Running Tests with Tox
----------------------

You can run the test suite using **tox**, which allows testing across multiple Python versions and manages dependencies in isolated environments.

To run tests for Python 3.12, execute:

.. code-block:: bash

    tox -r -e py312

Updating VCR Cassettes
----------------------

If you want to update the VCR cassettes (used to record HTTP interactions), follow these steps:

1. **Remove existing cassette files** from the ``tests/cassettes`` directory:
2. **Start the Docker environment**:

.. code-block:: bash

    docker compose up --build

3. **Run the tests with VCR recording enabled**:

.. code-block:: bash

    tox -r -e py312 -- --vcr-record=all
