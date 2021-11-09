import requests
import re

from .exceptions import BadURLException, ExpandingErrorException

URL_RE = re.compile(
    r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.]"
    r"[a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)"
    r"))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()"
    r'\[\]{};:\'".,<>?«»“”‘’]))'
)


class BaseShortener:
    """Base Class for all shorteners.

    Keyword Args:
        proxies (dict, optional): Web proxy configuration for :ref:`Requests
            Proxies <requests:proxies>`.
        timeout (int, optional): Seconds before request is killed.
        verify (bool, str, optional): SSL Certificate verification for
            :ref:`Requests Verification <requests:verification>`.

    Example:
        >>> class NewShortener(BaseShortener):
        ...     api_url = 'http://the/link/for/the/api'
        ...     def short(self, url):
        ...         pass
        ...     def expand(self, url):
        ...         pass
        ...     def custom_method(self):
        ...         pass

    """

    def __init__(self, **kwargs):
        for key, item in list(kwargs.items()):
            setattr(self, key, item)

        # safe check
        self.timeout = getattr(self, "timeout", 2)
        self.verify = getattr(self, "verify", True)
        self.proxies = getattr(self, "proxies", {})

    def _get(self, url, params=None, headers=None):
        """Wrap a GET request with a url check.

        Args:
            url (str): URL shortener address.

        Keyword Args:
            headers (dict): HTTP headers to add, `Requests Custom Headers`_.
            params (dict): URL parameters, `Requests Parameters`_.

        .. _Requests Custom Headers: http://requests.kennethreitz.org/en/master/user/quickstart/#custom-headers
        .. _Requests Parameters: http://requests.kennethreitz.org/en/master/user/quickstart/#passing-parameters-in-urls

        Returns:
            requests.Response: HTTP response.

        """
        url = self.clean_url(url)
        response = requests.get(
            url,
            params=params,
            verify=self.verify,
            timeout=self.timeout,
            headers=headers,
            proxies=self.proxies,
        )
        return response

    def _post(self, url, data=None, json=None, params=None, headers=None):
        """Wrap a POST request with a url check.

        Args:
            url (str): URL shortener address.

        Keyword Args:
            data (dict, str): Form-encoded data, `Requests POST Data`_.
            headers (dict): HTTP headers to add, `Requests Custom Headers`_.
            json (dict): Python object to JSON encode for data, `Requests
                POST Data`_.
            params (dict): URL parameters, `Requests Parameters`_.

        .. _Requests Custom Headers: http://requests.kennethreitz.org/en/master/user/quickstart/#custom-headers
        .. _Requests Parameters: http://requests.kennethreitz.org/en/master/user/quickstart/#passing-parameters-in-urls
        .. _Requests POST Data: http://requests.kennethreitz.org/en/master/user/quickstart/#more-complicated-post-requests

        Returns:
            requests.Response: HTTP response.

        """
        url = self.clean_url(url)
        response = requests.post(
            url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify,
            proxies=self.proxies,
        )
        return response

    def short(self, url):
        """Shorten URL using a shortening service.

        Args:
            url (str): URL to shorten.

        Raises:
            NotImplementedError: Subclass must override.

        """
        raise NotImplementedError

    def expand(self, url):
        """Expand URL using a shortening service.

        Only visits the link, and returns the response url.

        Args:
            url (str): URL to shorten.

        Raises:
            ExpandingErrorException: URL failed to expand.

        """
        url = self.clean_url(url)
        response = self._get(url)
        if response.ok:
            return response.url
        raise ExpandingErrorException

    @staticmethod
    def clean_url(url):
        """URL validation.

        Args:
            url (str): URL to shorten.

        Raises:
            BadURLException: URL is not valid.

        """
        if not url.startswith(("http://", "https://")):
            url = f"http://{url}"

        if not URL_RE.match(url):
            raise BadURLException(f"{url} is not valid")

        return url
