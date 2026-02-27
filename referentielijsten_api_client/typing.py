from typing import Any, NotRequired, Required, TypedDict


class APIAdministrator(TypedDict):
    naam: NotRequired[str]
    email: NotRequired[str]
    afdeling: NotRequired[str]
    organisatie: NotRequired[str]


class APITable(TypedDict):
    code: str
    naam: str
    beheerder: NotRequired[APIAdministrator]
    einddatumGeldigheid: NotRequired[str | None]  # ISO 8601 datetime string


class APITableItem(TypedDict):
    code: str
    naam: str
    begindatumGeldigheid: NotRequired[str]  # ISO 8601 datetime string
    einddatumGeldigheid: NotRequired[str | None]  # ISO 8601 datetime string
    aanvullendeGegevens: NotRequired[Any]


class PaginatedResponseData[T](TypedDict):
    count: Required[int]
    next: Required[str | None]
    previous: Required[str | None]
    results: Required[list[T]]
