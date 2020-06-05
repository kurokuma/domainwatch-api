# -*- coding: utf-8 -*-
from domainwatch.base import DomainWatchAPIBase

class DomainwatchSearch(DomainWatchAPIBase):
    PATH = "search"

    def __init__(self, proxies=None):
        self.proxies = proxies
    
    def search(self, search_type, query=None, size=100, page=1, return_type="raw"):
        params = {
            "type": search_type,
            "query": query,
            "size": size,
            "page": page
        }
        res = self.get_query(params, proxies=self.proxies)
        if return_type == "raw":
            return res
        elif return_type == "result":
            return res["results"]
        else:
            return res