from ..base import BaseShortener
from ..exceptions import (
    ShorteningErrorException,
    ExpandingErrorException,
    BadAPIResponseException,
)


class Shortener(BaseShortener):
    """
    Ow.ly url shortner api implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener()
        >>> s.owly.short('http://www.google.com')
        'http://ow.ly/TEST'
        >>> s.owly.expand('http://ow.ly/TEST')
        'http://www.google.com'
    """

    api_url = "http://ow.ly/api/1.1/url/"

    def short(self, url):
        """Short implementation for ow.ly.

        Args:
            url (str): The URL you want to shorten.

        Returns:
            str: The shortened URL.

        Raises:
            BadAPIResponseException: If the api response data could not get parsed.
            ShorteningErrorException: If the API Returns an error as response.
        """

        url = self.clean_url(url)
        shorten_url = f"{self.api_url}shorten"
        params = {"apiKey": self.api_key, "longUrl": url}
        response = self._get(shorten_url, params=params)
        if not response.ok:
            raise ShorteningErrorException(response.content)

        data = response.json()
        if "results" not in data:
            raise BadAPIResponseException(f"API Returned wrong response: " f"{data}")

        return data["results"]["shortUrl"]

    def expand(self, url):
        """Expand implementation for ow.ly.

        Args:
            url (str): The URL you want to expand.

        Returns:
            str: The expanded URL.

        Raises:
            BadAPIResponseException: Bad response from the API.
            ExpandingErrorException: If the API Returns an error as response.
        """

        url = self.clean_url(url)
        expand_url = f"{self.api_url}expand"
        data = {"apiKey": self.api_key, "shortUrl": url}
        response = self._get(expand_url, params=data)
        if not response.ok:
            raise ExpandingErrorException(response.content)

        data = response.json()
        if "results" not in data:
            raise BadAPIResponseException(f"API Returned wrong response: " f"{data}")

        return data["results"]["longUrl"]
