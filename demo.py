# -*- coding: utf-8 -*-
from domainwatch.domainwatch_search import DomainwatchSearch
from domainwatch.domainwatch_whois import DomainwatchWhois

def main():
    dms = DomainwatchSearch()
    res = dms.search("whois", query="softbank")
    print(res)
    
    dmw = DomainwatchWhois()
    res = dmw.whois("softbank.jp")
    print(res)

if __name__ == '__main__':
    main()