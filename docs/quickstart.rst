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

First, import and initialize the client with your API endpoint and token:

.. code-block:: python

    from referentielijsten_api_client.client import ReferentielijstenClient

    client = ReferentielijstenClient(
        base_url="https://api.example.com",  # replace with your API endpoint
        token="your_api_token_here"          # replace with your API token
    )

Listing all available tables
----------------------------

You can retrieve a list of all tables available in the Referentielijsten API:

.. code-block:: python

    tables = client.get_all_tables()

Getting items from a specific table
-----------------------------------

To get all items for a specific table:

.. code-block:: python

    table_code = "example_table_code"
    items = client.get_items_for_table(table_code)

Testing
=======

You can run the test suite using `tox`. To run tests for Python 3.12 and record all HTTP interactions (using `vcrpy`), execute:

.. code-block:: bash

    tox -r -e py312 -- --vcr-record=all
