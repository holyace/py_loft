#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/25

"""


class LfConst:
    key_method = "method"
    key_offset = "offset"
    key_limit = "limit"

    method_fav = "favorites"

    batch_data_url = "http://api.lofter.com/v1.1/batchdata.api?product=lofter-android-6.1.2"

    key_raw = "raw"
    key_origin = "orign"
    key_path = "key_path"

    invalid_url = ["aFYrZlVtbllRa3Uvbmk2WS9HdHNvKzhBQTlNQ3VrS0JXT2VtdnYxaWwrTlFSb2Fmb2JZVlFnPT0",
                   "cGhURHJqUEtFbWI1TmI0a0hOdldTeDBuYWFXcit1TlUybGVKMFdRSnlFKzh5SFR5dnBkdkJ3PT0",
                   "cGhURHJqUEtFbWJlcEFmY2kvUGg3b2RrRWR6U205aVBma3VkMWd5aUdxQWF6WjlKQlpsV1RRPT0",
                   "cGhURHJqUEtFbWJlcEFmY2kvUGg3cWkvSjVLK1JrNFpkN0J5K3BTWlIyaXJwTzlvdElEKzFBPT0",
                   "cGhURHJqUEtFbWJlcEFmY2kvUGg3cWR2R3VhNFY3anJHdVVhcW5MRjUxajBZb01GQU9MZ1B3PT0",
                   "dkM5K2lCcUZ5TzJ6Zi9QWHpJeW1aS05zbUlBV0tuV093N1BUUkhnYTlGS05ISjIxVU9VRktnPT0",
                   "eU55Z0xoR0hva0pIN3Nlc3c2amRVY0Y3YnFsVDQ4ZGV3Z2ZPaDdpclFrbE1zcTdQeWN2c0x3PT0",
                   "M2dvaTZVaXZDb0NzNU9hbjdVdmZyckswdjIvbndlb3ZvMXVWYktDQVRrVWRHRWJaS0xzc3dBPT0",
                   "M2dvaTZVaXZDb0NzNU9hbjdVdmZycUhnaDZCV2tnd3ZnSGJlNkJ1aU1pYjNvajZGbWk4Qi9nPT0",
                   "NE82V3lFUXJ1YUVlL2dveWhHMDFBb0R3MnJjd0VrcGY4b1pyaVZvK3B2dDd6d3IvYTE2dnFnPT0",
                   "NTl2VnVJU2lSdkNiS25DdkNKT1p2VmU5MGxxN1ZYS0VJdVVZMHppUXlPSkw3U29TbjNRYzVBPT0",
                   "NTl2VnVJU2lSdkNiS25DdkNKT1p2YjBrajdMRDlaMEVNUUZhSDRqKyt0OEhJWTJkMU55dG5BPT0",
                   "NTl2VnVJU2lSdkNiS25DdkNKT1p2YVhkWlU0czRyWXczZDFpK1ZYYk4waFBOaHRNZCtXd013PT0",
                   "Sk5OZVhRaUZtSFZTLytXOTE1MXNtU2hCWFljeURFaWJFOEhVbWRyRXpZc3hJNGFXUFBJQzh3PT0",
                   "SytsM3dmZkI2b1JkQnQxMngzc1lFa0l3MlJtakJLYXdxZ2k5RUNCRC8vdFh5Q1dTc0xUcTJRPT0"]

    __headers = {"User-Agent": "LOFTER-Android 6.1.2 (HUAWEI NXT-AL10; Android 8.0.0; null) WIFI",
                 "URSMobToken": "dff1d044908d2213c17d8c9b72f89874fb49a8",
                 "URSMobID": "7631661DBBFD4C968C50C25E7E354EDB4E24F9A30D9A54D1584D14FAE0C03DA98AD7B61E6487583CB8F2E9137B66FF7B",
                 "secruityinfo": "{\"datatype\":\"aimt_datas\",\"id_ver\":\"Android_1.0.1\",\"rdata\":\"hp2naAHC4kCtZr8wIFbvXcV0YT+yAmuTxfofaEz8p/GHKATMBUFU1p8oTF60WSqPMSb6uPiBXx9zhcELb74oxJBS4nrNjAUai8C21EaKFWrkqOPCooWRi9MNP4/A2yVodRQWaBcNxjcgCNw58meFGJOmZQNggHFaouRxsPYDHd5rOrHkcfDZIn3h9dmt0Xvpd0gw9GSqIMxsQKD3n42TSY9AMfX77F4U4DiGiECgg5g8pzTBWqGgjX2ZHuVeVn1wBkLpITBo9A9H1dc4UV6ShtNo++cMzR/GkUHYKuej9ILQdKWCxGLnRsigvmHL71zRfkoHznNxHbtT8M0mqcABZdY6JmSQoij5oXIh4EdL5H63gp7kJto8wOkQUOQu9Xq4UYOasxZaH26mbMtH1Wfq4u5NEN5o+v74e5L31EH3cQf4g8C8gV6QunSLPkxZIorerrpdCljTCgAPgzyf4Gh+3AZo5OcQrEjFvjR63cL/BJ6O9RKV4dddGkJ01yuTyvX5zoek3J21BFU+0YwockrMIb8KdF6RmlnY5YW+SmeGDyEF6sS/drPrCioCrA5L/PUjFWAwZf9IP4Vg+Jo+95KCQJm1rLHmq7BsXY0wsdMFSegYxgawT13joWBrrEi8VUwc8FmPC6C3WX/1EBK1XTG/4n2pfEsNByb88J14Y0AHJWE=\",\"rk\":\"YiteuBay1Qt1rLg2dr1VyMZSMn6U+yrZ3I8W8cbqw7SjyvrGP4/COIGLwR/zaxTpQA5ClI98ZrwduS/lmuhmdDJl7Q3dFQTRn33stp6QOaJmVIxGq+3FdgmZbyMFJrV6WCemzG//skhFwighHFqJylmGbQZKRgccnGQ+K036X68=\"}",
                 "market": "huawei",
                 "deviceid": "ffffffff-a021-c75d-38c6-17c30033c587",
                 "dadeviceid": "b9b5ca2f8dbc77ca9f0929e658c512101442083",
                 "cookie": "NTESwebSI=C8A168C5124C98EDD148F6FB6495D4CE.hzabj-lofter-new13.server.163.org-8010; Path=/; HttpOnly",
                 "Content-Type": "application/x-www-form-urlencoded"
                 }

    __body = {"supportposttypes": "1,2,3,4,5,6",
              "blogdomain": "sharlyfu.lofter.com",
              "postdigestnew": "1",
              "returnData": "1",
              }

    @classmethod
    def get_headers(cls) -> dict:
        return cls.__headers.copy()

    @classmethod
    def get_common_param(cls) -> dict:
        return cls.__body.copy()
