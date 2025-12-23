import logging
from typing import Optional, TypedDict

from django.http import HttpRequest

from ape_pie.client import APIClient
from .typing import PaginatedResponseData

logger = logging.getLogger(__name__)


def pagination_helper(
    client: APIClient,
    paginated_data: PaginatedResponseData,
    max_requests: int | None = None,
    **kwargs,
):
    """
    Fetch results from a paginated API endpoint, and optionally limit the number of
    requests to perform when fetching new pages by specifying the ``max_requests`` argument
    """

    def _iter(_data, num_requests=0):
        yield from _data["results"]

        if next_url := _data.get("next"):
            if max_requests and num_requests >= max_requests:
                logger.info(
                    "Number of requests while retrieving paginated results reached "
                    "maximum of %s requests, returning results",
                    max_requests,
                )
                return
            response = client.get(next_url, **kwargs)
            num_requests += 1
            response.raise_for_status()
            data = response.json()
            yield from _iter(data, num_requests)

    return _iter(paginated_data)
