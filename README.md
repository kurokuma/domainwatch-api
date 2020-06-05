# domainwat.ch API wrapper for Python

[domainwat.ch](https://domainwat.ch/?lang=en)

- WHOIS
    - [Whois Query Sample](https://domainwat.ch/about?lang=en)
- Website Information

# Usage
```python
# -*- coding: utf-8 -*-
from domainwatch.domainwatch_search import DomainwatchSearch
from domainwatch.domainwatch_whois import DomainwatchWhois

def main():
    # whois search
    dms = DomainwatchSearch()
    res = dms.search(search_type="whois", query="softbank")
    print(res)
    
    # whois
    dmw = DomainwatchWhois()
    res = dmw.whois("softbank.jp")
    print(res)

if __name__ == '__main__':
    main()
```

- Whois Search

| Param       | Required/Option     | Default | Type   |
|-------------|---------------------|---------|--------|
| search_type | Required(whois/dns) | -       | string |
| query       | Option              | -       | string |
| size        | Option              | 100     | int    |
| page        | Option              | 1       | int    |
| return_type | Option(raw/results) | raw     | string |

- whois

| Param       | Required/Option     | Default | Type   |
|-------------|---------------------|---------|--------|
|    domain   | Required            | -       | string |
| return_type | Option(raw/records) | raw     | string |
|             |                     |         |        |
