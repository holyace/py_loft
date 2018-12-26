#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/25

"""
from urllib.request import Request
from urllib.request import urlopen
from urllib import parse

method_get = 0
method_post = 1


def post(url: str, headers: dict, params: dict) -> str:
    return execute(url, method_post, headers, params)


def get(url: str, headers: dict, params: dict) -> str:
    return execute(url, method_get, headers, params)


def execute(url: str, method: int, headers: dict, params: dict) -> str:
    if not url:
        print("illegal url")
        return None
    if not params:
        query = parse.urlencode(params).encode()
    if method_post == method and not query:
        http_req = Request(url, query)
    else:
        url = _add_param_to_url(url, params)
        http_req = Request(url)
    if headers:
        for header in headers.keys():
            http_req.add_header(header, headers[header])
    http_res = urlopen(http_req)
    ret_code = http_res.status
    http_content = http_res.read().decode("utf-8")
    if 200 != ret_code:
        print("request fail", ret_code, http_content)
        http_content = None
    return http_content


def _add_param_to_url(url: str, params: dict) -> str:
    if not url and not params:
        return url
    query = parse.urlencode(params)
    if "?" in url:
        url = url + "&" + query
    else:
        url = url + "?" + query
    return url
