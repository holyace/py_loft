import blogParser
import thread
import os

curr_dir = os.getcwd()
jsonPath = curr_dir + "/res/lfimg.json"
savePath = curr_dir + "/res/pic"

downloaded = []
totalUrl = []

pic_list = blogParser.parse_response(jsonPath)
if pic_list:
    print("total", len(pic_list), "need download")
    thread.batch_download(pic_list, savePath)
else:
    print("empty list")

