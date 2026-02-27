============================
Referentielijsten Api Client
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

Installation
============

.. code-block:: bash

    pip install referentielijsten-api-client



Usage
=====

Initialize the client with your API endpoint and token:

.. code-block:: python

    from referentielijsten_api_client.client import ReferentielijstenClient

    client = ReferentielijstenClient(
        base_url={{ base_url }},
        token={{ your_api_token}},
    )

List tables
-----------

.. code-block:: python

    # List all tables

    tables = client.get_all_tables()

List items for a specific table
-------------------------------

.. code-block:: python

    # List items

    table_code = "tabel_code"
    items = client.get_items_for_table(table_code)


Testing
=======

You can run the test suite using `tox`. To run tests for Python 3.12 and record all HTTP interactions (using `vcrpy`), execute:

.. code-block:: bash

    tox -r -e py312 -- --vcr-record=all


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
