import logging
from dataclasses import dataclass
from urllib.parse import urljoin

from referentielijsten_api_client.client import ReferentielijstenClient

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class ReferentielijstenService:
    _api_root: str
    _api_path: str
    _api_token: str

    @property
    def _api_url(self):
        return urljoin(self._api_root, self._api_path)

    def client_factory(self) -> "ReferentielijstenClient":
        return ReferentielijstenClient(
            base_url=self._api_url,
            token=self._api_token,
        )
