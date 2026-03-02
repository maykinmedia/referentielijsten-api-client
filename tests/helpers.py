import logging
from dataclasses import dataclass

from referentielijsten_api_client.client import ReferentielijstenClient

logger = logging.getLogger(__name__)


class NoServiceConfigured(RuntimeError):
    pass


@dataclass(frozen=True, slots=True)
class ReferentielijstenService:
    _api_url: str

    def client_factory(self) -> ReferentielijstenClient:
        if not self._api_url:
            raise NoServiceConfigured("API service not configured")
        return ReferentielijstenClient(self._api_url)
