from ..base import BaseShortener
from ..exceptions import ShorteningErrorException, ExpandingErrorException


class Shortener(BaseShortener):
    """
    Da.gd shortener implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener()
        >>> s.dagd.short('http://www.google.com')
        'http://da.gd/TEST'
        >>> s.dagd.expand('http://da.gd/TEST')
        'http://www.google.com'
    """

    api_url = "https://da.gd/"

    def short(self, url):
        """Short implementation for Da.gd
        Args:
            url (str): the URL you want to shorten

        Returns:
            str: The shortened URL.

        Raises:
            ShorteningErrorException: If the API Returns an error as response
        """
        url = self.clean_url(url)
        shorten_url = f"{self.api_url}shorten"
        response = self._get(shorten_url, params={"url": url})
        if not response.ok:
            raise ShorteningErrorException(response.content)
        return response.text.strip()

    def expand(self, url):
        """Expand implementation for Da.gd
        Args:
            url (str): The URL you want to expand.

        Returns:
            str: The expanded URL.

        Raises:
            ExpandingErrorException: If the API Returns an error as response.
        """

        url = self.clean_url(url)
        # da.gd's coshorten expects only the shorturl identifier
        # (i.e. the "stuff" in http://da.gd/stuff), not the full short URL.
        sanitized_url = url.split("da.gd/", 1)[-1]
        expand_url = f"{self.api_url}coshortern/{sanitized_url}"
        response = self._get(expand_url)
        if not response.ok:
            raise ExpandingErrorException(response.content)
        return response.text.strip()
