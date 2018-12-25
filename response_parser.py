#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
create by:chad at 2018/12/24

"""
import json
from urllib.parse import urlparse

import constants


def parse_response(url_list: dict, file_path: str):
    try:

        with open(file_path, "r") as json_file:
            json_str = json_file.read()
            json_response = json.loads(json_str)

            items = json_response["response"]["items"]

            if not items:
                print("response items is empty")
                return

            for item in items:
                parse_item(url_list, item)

            return

    except IOError:
        print("open file faile")
    except KeyError:
        print("illegal json data")
    return


def parse_item(url_list: dict, item: dict):
    if not item:
        print("empty item")
        return

    post_json = item["post"]

    if not post_json:
        print("empty item.post")
        return

    __parse_first_image(url_list, post_json["firstImageUrl"])

    __parse_photo_link(url_list, post_json["photoLinks"])
    return


def __parse_first_image(url_list: dict, first_image: str):
    if not first_image:
        print("empty first image")
        return
    first_image_list = json.loads(first_image)
    if not first_image_list:
        print("empty first image")
        return
    for pic_url in first_image_list:
        url_key = get_key(pic_url)
        __check_url_and_add(url_list, url_key, pic_url)
    return


def __parse_photo_link(url_list: dict, photo_link: str):
    if not photo_link:
        return
    photo_link_json = json.loads(photo_link)
    if not photo_link_json:
        return
    for item in photo_link_json:
        if not item:
            continue
        if constants.key_raw in item:
            url = item[constants.key_raw]
            __check_url_and_add(url_list, get_key(url), url)
        if constants.key_origin in item:
            url = item[constants.key_origin]
            __check_url_and_add(url_list, get_key(url), url)

    return


def __check_url_and_add(url_list: dict, key: str, url: str):
    if not key or not url:
        print("illegal argument", key, url)
        return
    for invalid in constants.invalid_url:
        if invalid in url:
            print("found invalid url", url)
            return
    if key in url_list.keys():
        tem_list = url_list[key]
        if url in tem_list:
            print("found duplicate url", url)
            return
        else:
            tem_list.append(url)
    else:
        key_list = [url]
        url_list[key] = key_list
        return


def get_key(url: str):
    if "?" in url:
        base_url = url[:url.index("?")]
    else:
        base_url = url
    url_path = urlparse(base_url).path
    try:
        index = url_path.rindex(".")
        if index >= 0:
            url_path = url_path[index - constants.name_length:]
        if "/" in url_path:
            url_path = url_path.replace("/", "")
    finally:
        pass
    return url_path
