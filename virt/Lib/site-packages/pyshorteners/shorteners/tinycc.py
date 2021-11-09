from ..exceptions import (
    ShorteningErrorException,
    ExpandingErrorException,
    BadAPIResponseException,
)
from ..base import BaseShortener


class Shortener(BaseShortener):
    """Tiny.cc implementation.

    Args:
        api_key (str): Tiny.cc API key.
        login (str): Tiny.cc username.

    Example:
        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(api_key='12345', login='user')
        >>> s.tinycc.short('http://www.google.com')
        'http://tiny.cc/6lbsez'

    """

    api_url = "http://tiny.cc/"
    params = {"c": "rest_api", "version": "2.0.3", "format": "json"}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux) Gecko/20100101 " "Firefox/61.0"
    }

    def short(self, url):
        """Short implementation for Tiny.cc.

        Args:
            url (str): The URL you want to shorten.

        Returns:
            str: The shortened URL.

        Raises:
            BadAPIResponseException: If the data is malformed or we got a bad
                status code on API response.
            ShorteningErrorException: If the API Returns an error as
                response.

        """
        url = self.clean_url(url)
        params = self.params.copy()
        params.update(
            {
                "m": "shorten",
                "longUrl": url,
                "login": self.login,
                "apiKey": self.api_key,
            }
        )
        response = self._get(self.api_url, params=params, headers=self.headers)
        if not response.ok:
            raise ShorteningErrorException(response.content)

        data = response.json()
        if not data.get("results"):
            raise ShorteningErrorException(data["errorMessage"])

        return data["results"]["short_url"].strip()

    def expand(self, url):
        """Expand implementation for Tiny.cc.

        Args:
            url (str): The URL you want to expand.

        Returns:
            str: The expanded URL.

        Raises:
            ExpandingErrorException: If the API Returns an error as response.

        """
        url = self.clean_url(url)
        params = self.params.copy()
        params.update(
            {"m": "expand", "longUrl": url, "login": self.login, "apiKey": self.api_key}
        )
        response = self._get(self.api_url, params=params, headers=self.headers)
        if not response.ok:
            raise ExpandingErrorException(response.content)

        data = response.json()
        if not data.get("results"):
            raise ExpandingErrorException(data["errorMessage"])

        return data["results"]["longUrl"].strip()

    def total_clicks(self, url):
        """How many times the shortened URL has been clicked on.

        Args:
            url (str): The shortened URL to examine.

        Returns:
            int: The number of times the shortened URL has been used.

        Raises:
            BadAPIResponseException: If the data is malformed or we got a bad
                status code on API response.

        """
        url = self.clean_url(url)
        params = self.params.copy()
        params.update(
            {
                "m": "total_visits",
                "shortUrl": url,
                "login": self.login,
                "apiKey": self.api_key,
            }
        )
        response = self._get(self.api_url, params=params, headers=self.headers)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        data = response.json()
        if not data.get("results"):
            raise BadAPIResponseException(data["errorMessage"])

        try:
            total_clicks = int(data["results"]["clicks"])
        except (KeyError, TypeError):
            return 0
        return total_clicks
