from html.parser import HTMLParser

from ..base import BaseShortener
from ..exceptions import ShorteningErrorException


class OHTMLParser(HTMLParser):
    def __init__(self):
        self.found = False
        self.val = None
        return HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if "id" in attrs and attrs["id"] == "surl":
            self.found = True

    def handle_data(self, data):
        if not self.found:
            return

        if data.startswith("http://osdb"):
            self.val = data


class Shortener(BaseShortener):
    """
    Os.db shortener implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener()
        >>> s.osdb.short('http://www.google.com')
        'https://osdb.link/TEST'
        >>> s.osdb.expand('http://osdb.link/TEST')
        'https://www.google.com'
    """

    api_url = "https://osdb.link/"

    def short(self, url):
        """Short implementation for Os.db

        Args:
            url: the URL you want to shorten

        Returns:
            A string containing the shortened URL

        Raises:
            ShorteningErrorException: If the API returns an error as response
        """
        url = self.clean_url(url)
        response = self._post(self.api_url, data={"url": url})
        if not response.ok:
            raise ShorteningErrorException(response.content)
        p = OHTMLParser()
        p.feed(response.text)

        if not p.val:
            raise ShorteningErrorException("Could not find osdb.link")

        return p.val
