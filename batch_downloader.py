#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/24

"""

from concurrent.futures import ThreadPoolExecutor
import downloader


def batch_download(url_map: dict, success_url: list, failed_url: list, save_path: str):
    with ThreadPoolExecutor(16) as executor:
        for url_key in url_map.keys():
            executor.submit(run(url_key, url_map[url_key], success_url, failed_url, save_path))

    return


def run(url_key: str, url_list: list, success_url: list, failed_url: list, save_path: str):
    if not url_list or not save_path:
        return
    downloader.download(url_list, save_path, url_key, success_url, failed_url)
    return
