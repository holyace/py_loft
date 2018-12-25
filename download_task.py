from concurrent.futures import ThreadPoolExecutor
import time
import hashlib
import download_worker

pre_fix = "img_"


def batch_download(url_list, save_path):
    with ThreadPoolExecutor(16) as executor:
        for url in url_list:
            executor.submit(run(url, save_path))

    return


def run(url, save_path):
    download_worker.download(url, save_path, hashlib.md5(url.encode("utf-8")).hexdigest())
    return