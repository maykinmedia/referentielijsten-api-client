============================
Referentielijsten API Client
============================

A Python client library for interacting with the `Referentielijsten API <https://github.com/maykinmedia/referentielijsten>`_.

:Version: 0.1.0
:Source: https://github.com/maykinmedia/referentielijsten-api-client
:Keywords: ``maykin, referentielijsten_api, referentielijsten api, referentielijsten api client, common ground, api client``
:PythonVersion: 3.12

|build-status| |code-quality| |ruff| |coverage|

|python-versions| |django-versions| |pypi-version|

.. contents::

.. section-numbering::

Overview
========

This client is built and tested to work with the ``0.2.0`` version of the **Referentielijsten API**,
ensuring reliable interaction with all supported endpoints.

It could potentially work with newer minor versions, but compatibility is not guaranteed.

Referentielijsten API
=====================

For more details about the Referentielijsten API, see the upstream repository on GitHub:
https://github.com/maykinmedia/referentielijsten

Installation
============

You can install the library via pip:

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


.. |build-status| image:: https://github.com/maykinmedia/referentielijsten-api-client/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/referentielijsten-api-client/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/referentielijsten-api-client/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/referentielijsten-api-client/actions?query=workflow%3A%22Code+quality+checks%22

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. |coverage| image:: https://codecov.io/gh/maykinmedia/referentielijsten-api-client/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/referentielijsten-api-client
    :alt: Coverage status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/referentielijsten-api-client.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/referentielijsten-api-client.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/referentielijsten-api-client.svg
    :target: https://pypi.org/project/referentielijsten-api-client/
