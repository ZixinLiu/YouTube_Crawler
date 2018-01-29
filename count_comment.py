import json
import os

sum = 0
for i in range(1, 50):
	str = "data{}.text".format(i)
	path = "/Users/admin/Desktop/Youtube_Crawler/data-output/Autos&Vehicles/Archive/" + str
	print path
	data = json.load(open(path))
	sum += len(data["comment_lst"])
print sum

