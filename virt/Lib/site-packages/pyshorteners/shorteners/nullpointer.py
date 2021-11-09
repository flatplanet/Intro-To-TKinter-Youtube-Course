from ..exceptions import ShorteningErrorException
from ..base import BaseShortener


class Shortener(BaseShortener):
    """The Null Pointer implementation

    Args:
        domain (str): Optional string for the null pointer instance to use. Default is
            'https://0x0.st'. Any URL to a Null Pointer instance is supported,
            for example:

                - ``https://0x0.st``
                - ``https://ttm.sh``

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(domain='https://0x0.st')
        >>> s.nullpointer.short('https://www.google.com')
        'https://0x0.st/jU'
    """

    def short(self, url):
        """Short implementation for The Null Pointer
        Args:
            url (str): the URL you want to shorten

        Returns:
            str: The shortened URL

        Raises:
            ShorteningErrorException: If the data is malformed or we got a bad
            status code on API response
        """
        url = self.clean_url(url)
        api_url = self.clean_url(getattr(self, "domain", "https://0x0.st"))
        payload = {"shorten": url}

        response = self._post(api_url, data=payload)

        if not response.ok:
            raise ShorteningErrorException(response.content)

        return response.text
