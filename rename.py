import os
import json


files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	with open(f) as json_data:
		d = json.load(json_data)
		video_id = d["video_id"]
		cate_id = d["category_id"]
		new_name = "data_{}_{}".format(video_id, category_id)
		os.rename(f, new_name)

    