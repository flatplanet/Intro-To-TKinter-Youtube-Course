from ..base import BaseShortener
from ..exceptions import ShorteningErrorException


class Shortener(BaseShortener):
    """
    Chilp.it shortener implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener()
        >>> s.chilpit.short('http://www.google.com')
        'http://chilp.it/TEST'
        >>> s.chilpit.expand('http://chilp.it/TEST')
        'http://www.google.com'
    """

    api_url = "http://chilp.it/api.php"

    def short(self, url):
        """Short implementation for Chilp.it

        Args:
            url: the URL you want to shorten

        Returns:
            A string containing the shortened URL

        Raises:
            ShorteningErrorException: If the API returns an error as response
        """
        response = self._get(self.api_url, params={"url": url})
        if response.ok:
            return response.text.strip()
        raise ShorteningErrorException(response.content)
