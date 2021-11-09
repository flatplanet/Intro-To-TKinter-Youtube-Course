from ..base import BaseShortener
from ..exceptions import ShorteningErrorException


class Shortener(BaseShortener):
    """
    Qps.ru shortener implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener()
        >>> s.qpsru.short('http://www.google.com')
        'http://qps.ru/TEST'
        >>> s.qpsru.expand('http://qps.ru/TEST')
        'http://www.google.com'

    """

    api_url = "http://qps.ru/api"

    def short(self, url):
        """Short implementation for Qps.ru

        Args:
            url: the URL you want to shorten

        Returns:
            A string containing the shortened URL

        Raises:
            ShorteningErrorException: If the API returns an error as response
        """

        url = self.clean_url(url)
        response = self._get(self.api_url, params={"url": url})
        if not response.ok:
            raise ShorteningErrorException(response.content)
        return response.text.strip()
