import os
import json


vid_id_list = []

list_to_cmp = ['"kJQP7kiw5Fk"', '"RgKAFK5djSk"', '"JGwWNGJdvx8"', '"OPf0YbXqDm0"', '"nfWlot6h_JM"', '"YqeW9_5kURI"', '"0KSOMA3QBU0"', '"YQHsXMglC9A"', '"hT_nvWreIhg"', '"lp-EO5I60KA"', '"6Mgqbai3fKo"', '"PT2_F-1esPk"', '"kOkQ4T5WO9E"', '"2vjPBrBU-TM"', '"5GL9JoH4Sws"', '"RBumgq5yVrA"', '"pRpeEdMmmQ0"', '"3AtDnEC4zak"', '"wnJ6LuUFpMo"', '"60ItHLz5WEA"', '"YBHQbu5rbdQ"', '"lY2yjAdbvdQ"', '"PIh2xe4jnpk"', '"TapXs54Ah3E"', '"KQ6zr6kCPj8"', '"iOe6dI2JhgU"', '"34Na4j8AVgA"', '"fLexgOxsZu0"', '"rYEDA3JcQqw"', '"t_jHrUE5IOk"', '"SXiSVQZLje8"', '"pXRviuL6vMY"', '"QcIy9NiNbmo"', '"t4H_Zoh7G5A"', '"PMivT7MJ41M"', '"AMTAQ-AJS4Y"', '"gCYcHz2k5x0"', '"hXI8RQYC36Q"', '"iS1g8G_njx8"', '"LjhCEhWiKXk"', '"j5-yKhDd64s"', '"c73Cu3TQnlg"', '"VqEbCxg2bNI"', '"8UVNT4wvIGY"', '"nYh-n7EOtMA"', '"NGLxoKOvzu4"', '"aDCcLQto5BM"', '"7zp1TbLFPp8"', '"Io0fBr1XBUA"', '"k85mRPqvMbE"']

files = [f for f in os.listdir('.') if os.path.isfile(f)]
print files
try:
	for f in files:
		with open(f) as json_data:
			d = json.load(json_data)
			video_id = d["video_id"]
			print video_id
			vid_id_list.append(json.dumps(video_id))

except Exception as e:
	print f

print "\n"
print vid_id_list
print "\n"
print list_to_cmp



vid_id_list = ['"KQ6zr6kCPj8"', '"VqEbCxg2bNI"', '"QK8mJJJvaes"', '"5GL9JoH4Sws"', '"60ItHLz5WEA"', '"NGLxoKOvzu4"', '"papuvlVeZg8"', '"3AtDnEC4zak"', '"09R8_2nJtjg"', '"fLexgOxsZu0"', '"c73Cu3TQnlg"', '"OPf0YbXqDm0"', '"t_jHrUE5IOk"', '"8UVNT4wvIGY"', '"hXI8RQYC36Q"', '"7zp1TbLFPp8"', '"uxpDa-c-4Mc"', '"rYEDA3JcQqw"', '"QGJuMBdaqIw"', '"TapXs54Ah3E"', '"0KSOMA3QBU0"', '"pXRviuL6vMY"', '"LjhCEhWiKXk"', '"aDCcLQto5BM"', '"RgKAFK5djSk"', '"RBumgq5yVrA"', '"uO59tfQ2TbA"', '"pRpeEdMmmQ0"', '"PMivT7MJ41M"', '"YBHQbu5rbdQ"', '"PIh2xe4jnpk"', '"kJQP7kiw5Fk"', '"JGwWNGJdvx8"', '"lY2yjAdbvdQ"', '"QcIy9NiNbmo"', '"iOe6dI2JhgU"', '"nfWlot6h_JM"', '"nYh-n7EOtMA"', '"34Na4j8AVgA"']


for i in vid_id_list:
	try:
		list_to_cmp.remove(i)
	except Exception as e1:
		print i

print list_to_cmp
