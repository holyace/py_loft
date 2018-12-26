#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/25

"""
from net import easy_net
from lofter.lofter_const import LfConst


def query_favorites(offset: int, page_size: int) -> str:
    headers = LfConst.get_headers()
    print(headers)

    body = LfConst.get_common_param()
    print(body)
    body[LfConst.key_method] = LfConst.method_fav
    body[LfConst.key_offset] = offset
    body[LfConst.key_limit] = page_size

    print(body)

    return easy_net.post(LfConst.batch_data_url, headers, body)
