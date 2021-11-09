import json
from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import BadAPIResponseException


class Shortener(BaseShortener):
    """
    Cutt.ly shortener implementation

    Args:
        api_key (str): cutt.ly API key

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(api_key='YOUR_KEY')
        >>> s.cuttly.short('http://www.google.com')
        'http://cutt.ly/TEST'
        >>> s.cuttly.expand('https://cutt.ly/TEST')
        'http://www.google.com'
    """

    api_url = "https://cutt.ly/api/api.php"
    STATUS_INVALID = 4

    def short(self, url):
        """Short implementation for Cutt.ly
        Args:
            url (str): the URL you want to shorten

        Returns:
            str: The shortened URL.

        Raises:
            BadAPIResponseException: If the data is malformed or we got a bad
                status code on API response.
            ShorteningErrorException: If the API Returns an error as response
        """
        url = self.clean_url(url)
        response = self._get(self.api_url, params={"key": self.api_key, "short": url})
        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException(
                "API response is invalid ,could not be decoded"
            )

        try:
            status = data["url"]["status"]
        except KeyError:
            raise BadAPIResponseException(
                "API response does not have the required field: status"
            )

        if status == self.STATUS_INVALID:
            """According to the API Docs when a status code of 4 is returned with
            json an Invalid API Key is provided"""
            raise BadAPIResponseException("Invalid API Key")

        try:
            short_link = data["url"]["shortLink"]
        except KeyError:
            raise BadAPIResponseException(
                "API response does not have the required field: shortLink"
            )

        return short_link
