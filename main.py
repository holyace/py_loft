import os
import constants
import response_parser
import batch_downloader

curr_dir = os.getcwd()
json_path = curr_dir + constants.path_json
save_path = curr_dir + constants.path_save_dir

success_url = []
failed_url = []
all_url = {}

# raw_url = {constants.key_path: []}

# total_url = {constants.key_origin: [], constants.key_raw: []}

# pic_list = blogParser.parse_response(jsonPath)

response_parser.parse_response(all_url, json_path)

if all_url:
    print("total", len(all_url), "need download")
    batch_downloader.batch_download(all_url, success_url, failed_url, save_path)
else:
    print("empty urls")

if failed_url:
    print("\nfailed", len(failed_url))
    print(failed_url)
else:
    print("all task success")
