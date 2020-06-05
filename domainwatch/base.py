# -*- coding: utf-8 -*-
import json
import requests

class DomainwatchException(Exception):
    def __init__(self, status_code, url, params):
        self.status_code = status_code
        self.url = url
        self.params = params
    
    def __repr__(self):
        return "Error -> status_code={status_code}, url: {url}, params: {params}".format(
            status_code=self.status_code,
            url=self.url,
            params=self.params
        )

    __str__ = __repr__

class DomainwatchInvalidParameterException(DomainwatchException):
    pass

class DomainwatchNotFoundDatabasesException(DomainwatchException):
    pass

class DomainWatchAPIBase(object):
    BASE_URL = "https://domainwat.ch/api/{path}"
    BASE_HEADER = {
        "User-Agent": "Domainwat.ch Python API",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    EXCEPTION = {
        400: DomainwatchInvalidParameterException,
        201: DomainwatchNotFoundDatabasesException
    }
    PATH = None
    
    def __init__(self):
        pass
    
    def get_query(self, params, proxies=None):
        r = requests.get(
            url=self.BASE_URL.format(path=self.PATH),
            params=params,
            headers=self.BASE_HEADER,
            proxies=proxies
        )
        r.encoding = r.apparent_encoding
        if r.status_code == 200:
            return r.json()
        else:
            ex = self.EXCEPTION.get(r.status_code, DomainwatchException)
            raise ex(
                status_code=r.status_code,
                url=self.BASE_URL.format(path=self.PATH),
                params=params
            )