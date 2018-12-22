import blogParser
import thread


jsonPath = "/Users/chad/Desktop/mock_data/lfimg.json"
savePath = "/Users/chad/Desktop/PIC/loft"

downloaded = []
totalUrl = []

pic_list = blogParser.parse_response(jsonPath)
if pic_list:
    print("total", len(pic_list), "need download")
    thread.batch_download(pic_list, savePath)
else:
    print("empty list")

