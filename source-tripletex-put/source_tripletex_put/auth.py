import requests
from typing import Mapping, Any
import base64


class PutSessionTokenAuthenticator:
    def __init__(self, base_url: str, consumer_token: str, employee_token: str, expiration_date: str):
        self.base_url = base_url
        self.consumer_token = consumer_token
        self.employee_token = employee_token
        self.expiration_date = expiration_date
        self._token = None

    def refresh_token(self):
        url = f"{self.base_url}/v2/token/session/:create"
        params = {
            "consumerToken": self.consumer_token,
            "employeeToken": self.employee_token,
            "expirationDate": self.expiration_date,
        }
        response = requests.put(url, params=params, headers={"accept": "*/*"})
        response.raise_for_status()
        data = response.json()
        # Adjust this to your API’s actual response
        self._token = data.get("token") or data.get("value")


    def get_auth_header(self) -> Mapping[str, Any]:
        if not self._token:
            self.refresh_token()

        # Basic auth with username "0" and password = token
        user_pass = f"0:{self._token}"
        encoded = base64.b64encode(user_pass.encode()).decode()

        return {"Authorization": f"Basic {encoded}"}