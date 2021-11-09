import json
from urllib.parse import urlparse
import logging

from ..base import BaseShortener
from ..exceptions import (
    BadAPIResponseException,
    ExpandingErrorException,
    ShorteningErrorException,
)

logger = logging.getLogger(__name__)


class Shortener(BaseShortener):
    """Bit.ly shortener Implementation

    Args:
        api_key (str): bit.ly API key

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(api_key='YOUR_KEY')
        >>> s.bitly.short('http://www.google.com')
        'http://bit.ly/TEST'
        >>> s.bitly.expand('https://bit.ly/TEST')
        'http://www.google.com'
        >>> s.bitly.total_clicks('https://bit.ly/TEST')
        10
    """

    api_url = "https://api-ssl.bit.ly/v4"

    def short(self, url):
        """Short implementation for Bit.ly
        Args:
            url (str): the URL you want to shorten

        Returns:
            str: The shortened URL.

        Raises:
            BadAPIResponseException: If the data is malformed or we got a bad
                status code on API response.
            ShorteningErrorException: If the API Returns an error as response
        """
        self.clean_url(url)
        shorten_url = f"{self.api_url}/shorten"
        params = {"long_url": url}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = self._post(shorten_url, json=params, headers=headers)
        if not response.ok:
            raise ShorteningErrorException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        return data["link"]

    def expand(self, url):
        """Expand implementation for Bit.ly
        Args:
            url (str): The URL you want to expand.

        Returns:
            str: The expanded URL.

        Raises:
            ExpandingErrorException: If the API Returns an error as response.
            BadAPIResponseException: If the API response can't be decoded.
        """
        self.clean_url(url)
        url = "".join(urlparse(url)[1:3])
        expand_url = f"{self.api_url}/expand"
        params = {"bitlink_id": url}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = self._post(expand_url, json=params, headers=headers)
        if not response.ok:
            raise ExpandingErrorException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        return data["long_url"]

    def total_clicks(self, url):
        """Total clicks implementation for Bit.ly
        Args:
            url (str): the URL you want to get the total clicks count

        Returns:
            int: The total clicks count

        Raises:
            BadAPIResponseException: If the API Returns an error as response
        """
        self.clean_url(url)
        url = "".join(urlparse(url)[1:3])
        clicks_url = f"{self.api_url}/bitlinks/{url}/clicks"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = self._get(clicks_url, headers=headers)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        total_clicks = 0
        try:
            for click in data["link_clicks"]:
                total_clicks += click["clicks"]
        except (KeyError, TypeError) as e:
            logger.warning("Bad value from total_clicks response: %s", e)
            return 0

        return total_clicks
