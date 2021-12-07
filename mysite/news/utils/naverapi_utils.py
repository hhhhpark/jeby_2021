import json, re
import urllib.request
import urllib.parse
from dateutil.parser import parse
from datetime import timedelta
from django.conf import settings
from django.utils import timezone


def call(keyword, display=10, start=1, sort="date"):
    """
    네이버 검색 API를 호출한다.
    """

    values = {
        "query": keyword,
        "display": display,
        "start": start,
        "sort": sort,
    }

    params = urllib.parse.urlencode(values, quote_via=urllib.parse.quote)
    url = "https://openapi.naver.com/v1/search/news.json?" + params

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", settings.NAVER_API_ID)
    request.add_header("X-Naver-Client-Secret", settings.NAVER_API_SECRET)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        result = json.loads(response_body.decode("utf-8")).get("items")
    else:
        print(rescode)
        result = None

    return result
