.. referentielijsten_api_client documentation master file, created by startproject.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=============================
Referentielijsten API Client
=============================

|build-status| |code-quality| |ruff| |coverage|

|python-versions| |django-versions| |pypi-version|

Welcome to the documentation of the **Referentielijsten API Client** library.

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

.. toctree::
   :maxdepth: 2
   :caption: Contents

   quickstart
   reference/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |build-status| image:: https://github.com/maykinmedia/referentielijsten-api-client/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/referentielijsten-api-client/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/referentielijsten-api-client/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/referentielijsten-api-client/actions?query=workflow%3A%22Code+quality+checks%22

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. |coverage| image:: https://codecov.io/gh/maykinmedia/referentielijsten-api-client/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/referentielijsten-api-client
    :alt: Coverage status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/referentielijsten-api-client.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/referentielijsten-api-client.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/referentielijsten-api-client.svg
    :target: https://pypi.org/project/referentielijsten-api-client/
