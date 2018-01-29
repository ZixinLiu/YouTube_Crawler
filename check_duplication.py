import json 
import collections

id_list =[]
for i in range(1, 51):
	with open("data_{}").format(i) as json_data:
		d = json.load(json_data)
		id_list.append(d["video_id"])


print id_list
print [item for item, count in collections.Counter(id_list).items() if count > 1]

