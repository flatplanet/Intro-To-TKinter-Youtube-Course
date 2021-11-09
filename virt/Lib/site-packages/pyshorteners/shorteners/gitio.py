from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class Shortener(BaseShortener):
    """Git.io shortener Implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(code='12345')
        >>> s.gitio.short('https://github.com/TEST')
        'https://git.io/12345'
        >>> s.gitio.expand('https://git.io/12345')
        'https://github.com/TEST'
    """

    api_url = "https://git.io"

    def short(self, url):
        """Short implementation for Git.io
        Only works for github urls

        Args:
            url (str): the URL you want to shorten
            code (str): (Optional) Custom permalink code: Eg.: test

        Returns:
            str: The shortened URL

        Raises:
            ShorteningErrorException: If the API returns an error as response
        """
        code = None
        try:
            code = self.code
        except AttributeError:
            pass

        shorten_url = self.api_url
        data = {"url": url, "code": code}
        response = self._post(shorten_url, data=data)
        if not response.ok:
            raise ShorteningErrorException(response.content)

        if not response.headers.get("Location"):
            raise ShorteningErrorException(response.content)

        return response.headers["Location"]
