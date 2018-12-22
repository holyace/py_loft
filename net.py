import os, stat
import urllib.request


def download(url, save_path, file_name):
    if not url:
        print("empty url")
        return
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        if "?" in url:
            index = url.index("?")
            base_url = url[:index]
        else:
            base_url = url
        file_suffix = os.path.splitext(base_url)[1]
        file_name = '{}{}{}{}'.format(save_path, os.sep, file_name, file_suffix)
        if os.path.exists(file_name):
            print("file already downloaded", file_name)
            return
        print("[download]:", url)
        print("[file name]:", file_name, "\n")
        urllib.request.urlretrieve(url, file_name)
        return
    except Exception as e:
        print("download fail", e, url)
        return
