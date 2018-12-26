#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/24

"""
import os
import urllib.request


def download(url_list: list, save_path: str, file_name: str, success_url: list, failed_url: list):
    if not url_list:
        print("empty url")
        return
    print("\nstart download", file_name)
    for url in url_list:
        try:
            download_internal(url, save_path, file_name)
            success_url.append(url)
            break
        except Exception as e:
            print("download fail", e, url)
            failed_url.append(url)
    return


def download_internal(url: str, save_path: str, file_name: str):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    full_path = '{}{}{}'.format(save_path, os.sep, file_name)
    if os.path.exists(full_path):
        print("file already downloaded", full_path)
        return
    print("[download]:", url)
    print("[full_path]:", full_path)
    urllib.request.urlretrieve(url, full_path)
    return
