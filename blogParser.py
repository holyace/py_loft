import json
from urllib.parse import urlparse

errorKey = ["M2dvaTZVaXZDb0NzNU9hbjdVdmZyaUZ4MXJXMENpYmNoRUJhSFJPVFhNQ2ZZR09HZmlqOFR3PT0",
            "eU55Z0xoR0hva0pIN3Nlc3c2amRVY0Y3YnFsVDQ4ZGV3Z2ZPaDdpclFrbE1zcTdQeWN2c0x3PT0",
            "NE82V3lFUXJ1YUVlL2dveWhHMDFBb0R3MnJjd0VrcGY4b1pyaVZvK3B2dDd6d3IvYTE2dnFnPT0",
            "NTl2VnVJU2lSdkNiS25DdkNKT1p2YVhkWlU0czRyWXczZDFpK1ZYYk4waFBOaHRNZCtXd013PT0",
            "aFYrZlVtbllRa3Uvbmk2WS9HdHNvKzhBQTlNQ3VrS0JXT2VtdnYxaWwrTlFSb2Fmb2JZVlFnPT0"]

key_list = []
url_list = []


def parse_response(file_path):
    try:

        key_list.clear()
        url_list.clear()

        with open(file_path, "r") as jsonFile:
            json_str = jsonFile.read()
            json_response = json.loads(json_str)

            items = json_response["response"]["items"]

            if not items:
                print("response items is empty")
                return None

            for item in items:
                item_pic_list = parse(item)
                if item_pic_list:
                    url_list.extend(item_pic_list)

            return url_list

    except IOError:
        print("open file faile")
    except KeyError:
        print("illegal json data")


def parse(item):
    if not item:
        print("empty item")
        return None

    item_pic_list = []

    post_json = item["post"]

    if not post_json:
        print("empty item.post")
        return None

    ret = __parse_first_image(post_json["firstImageUrl"])
    if ret:
        item_pic_list.extend(ret)
    ret = __parse_photo_link(post_json["photoLinks"])
    if ret:
        item_pic_list.extend(ret)
    return item_pic_list


def __check_url(tem_list, url):
    if not url:
        return -1
    for err in errorKey:
        if err in url:
            print("found error url", url)
            return -1
    if url in tem_list:
        print("found duplicate url", url)
        return -1
    if url in url_list:
        print("found duplicate url", url)
        return -1
    path = urlparse(url).path
    if path in key_list:
        print("found duplicate key", url)
        return -1
    key_list.append(path)
    return 1


def __parse_first_image(first_image):
    if not first_image:
        return None
    first_image_list = json.loads(first_image)
    if not first_image_list:
        return None
    ret_list = []
    for pic_url in first_image_list:
        if not __check_url(ret_list, pic_url):
            continue
        ret_list.append(pic_url)
    return ret_list


def __parse_photo_link(photo_link):
    if not photo_link:
        return None
    photo_link_json = json.loads(photo_link)
    if not photo_link_json:
        return
    link_list = []
    for item in photo_link_json:
        if not item:
            continue
        if "raw" in item:
            url = item["raw"]
        elif "orign" in item:
            url = item["orign"]
        if not __check_url(link_list, url):
            continue
        link_list.append(url)
    return link_list
