import json

from ..exceptions import (
    ShorteningErrorException,
    BadAPIResponseException,
    ExpandingErrorException,
)
from ..base import BaseShortener


class Shortener(BaseShortener):
    """Adf.ly implementation.

    Args:
        api_key (str): adf.ly API key.
        user_id (str): adf.ly user id.
        domain (str, optional): Domain used upon shortening, options are:

            - ``ad.fly`` (default)
            - ``q.gs``
            - ``custom.com``
            - ``0`` (Random domain)

        type (int, optional): For advertising on the shortened link, options
            are:

            - ``1``, ``int``, ``interstitial`` - Interstitial advertising
            - ``2`` - No advertising
            - ``3``, ``banner`` - Framed Banner

        group_id (int, optional): API parameter `group_id`.

    Example:
        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(api_key='YOUR_KEY', user_id='USER_ID',
                                       domain='test.us', group_id=12, type='int')
        >>> s.adfly.short('http://www.google.com')
        'http://test.us/TEST'

    """

    api_url = "http://api.adf.ly/v1"

    def short(self, url):
        """Short implementation for Adf.ly.

        Args:
            url (str): The URL you want to shorten.

        Returns:
            str: The shortened URL.

        Raises:
            BadAPIResponseException: If the data is malformed or we got a bad
                status code on API response.
            ShorteningErrorException: If the API Returns an error as response.

        """
        url = self.clean_url(url)
        shorten_url = f"{self.api_url}/shorten"
        payload = {
            "domain": getattr(self, "domain", "adf.ly"),
            "advert_type": getattr(self, "type", "int"),
            "group_id": getattr(self, "group_id", None),
            "key": self.api_key,
            "user_id": self.user_id,
            "url": url,
        }
        response = self._post(shorten_url, data=payload)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        if data.get("errors"):
            errors = ",".join(i["msg"] for i in data["errors"])
            raise ShorteningErrorException(errors)

        if not data.get("data"):
            raise BadAPIResponseException(response.content)

        return data["data"][0]["short_url"]

    def expand(self, url):
        """Expand implementation for Adf.ly.

        Args:
            url (str): The URL you want to expand.

        Returns:
            str: The expanded URL.

        Raises:
            BadAPIResponseException: If the data is malformed or we got a bad
                status code on API response.
            ExpandingErrorException: If the API Returns an error as response.

        """
        url = self.clean_url(url)
        expand_url = f"{self.api_url}/expand"
        payload = {
            "domain": getattr(self, "domain", "adf.ly"),
            "advert_type": getattr(self, "type", "int"),
            "group_id": getattr(self, "group_id", None),
            "key": self.api_key,
            "user_id": self.user_id,
            "url": url,
        }
        response = self._post(expand_url, data=payload)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        if data.get("errors"):
            errors = ",".join(i["msg"] for i in data["errors"])
            raise ExpandingErrorException(errors)

        if not data.get("data"):
            raise BadAPIResponseException(response.content)

        return data["data"][0]["url"]
