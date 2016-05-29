# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def url_check(url):
    try:
        req = Request(url)
        response = urlopen(req)
        status = response.status
        if status == 200:
            return 'OK', status
        else:
            return 'NG', status
    except HTTPError as he:
        return "NG", he.code
    except URLError as ue:
        return "NG", str(ue.reason)
    except Exception as e:
        return "NG", str(e)

if __name__ == "__main__":
    # target = "http://yahoo.co.jp"
    target = "http://yahoohoageagagaega.co.jp"
    # target = "http://www.python.org/fish.html"
    result = url_check(target)
    print(result)
