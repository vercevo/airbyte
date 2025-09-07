from typing import Any, Mapping, Optional
from airbyte_cdk.sources.streams.http import HttpStream
from .auth import PutSessionTokenAuthenticator


class MyApiBaseStream(HttpStream):
    url_base = "https://api-test.tripletex.tech/"

    def __init__(self, config, **kwargs):
        authenticator = PutSessionTokenAuthenticator(
            base_url=config["base_url"],
            consumer_token=config["consumer_token"],
            employee_token=config["employee_token"],
            expiration_date=config["expiration_date"],
        )
        super().__init__(authenticator=authenticator, **kwargs)

    def parse_response(self, response, **kwargs):
        yield from response.json()

    def next_page_token(
        self,
        response,
        previous_token: Optional[Mapping[str, Any]] = None
    ) -> Optional[Mapping[str, Any]]:
        """
        Implement pagination here. Returning None means no pagination.
        """
        return None

    @property
    def primary_key(self) -> Optional[str]:
        """
        The field in the records that acts as a unique ID.
        If unknown, return None.
        """
        return None


class CustomersStream(MyApiBaseStream):
    def path(self, **kwargs) -> str:
        return "customers"
