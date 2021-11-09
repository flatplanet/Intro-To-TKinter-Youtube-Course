import json

from ..base import BaseShortener
from ..exceptions import ShorteningErrorException, BadAPIResponseException


class Shortener(BaseShortener):
    """
    Po.st Shortener implementation

    Args:
        api_key (str): adf.ly API key.

    Example:
        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(api_key='YOUR_KEY')
        >>> s.post.short('http://www.google.com')
        'http://po.st/TEST'
        >>> s.post.expand('http://po.st/TEST')
        'http://www.google.com'

    """

    api_url = "http://po.st/api/shorten"

    def short(self, url):
        """Short implementation for Po.st.

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
        params = {"apiKey": self.api_key, "longUrl": url, "format": "txt"}
        response = self._get(self.api_url, params=params)
        if not response.ok:
            raise ShorteningErrorException(response.content)

        try:
            data = response.json()
            return data["short_url"]
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")
