# -*- coding: utf-8 -*-
from domainwatch.base import DomainWatchAPIBase

class DomainwatchWhois(DomainWatchAPIBase):
    PATH = "whois"

    def __init__(self, proxies=None):
        self.proxies = proxies
    
    def whois(self, domain, return_type="raw"):
        self.PATH += "/" + domain
        res = self.get_query(params=None, proxies=self.proxies)
        if return_type == "raw":
            return res
        elif return_type == "records":
            return res["records"]
        return res