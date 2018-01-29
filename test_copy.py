import sys
import multiprocessing
sys.path.append("/Users/admin/Desktop/youtube_tutorial/")

from get_Videos import youtube_search
from get_Videos import get_num_comment
from get_Videos import get_comment
from get_Videos import grab_comment
from get_Videos import ExceptionHandle
import json
import os


def break_func(video_set, start, end):

	for i in range(start, end):
		video_title = video_set[i]["snippet"]["title"]
		video_id = video_set[i]["id"]["videoId"]

		search_name = "data_{}_10.text".format(video_id) #file to be searched
		cur_dir = os.getcwd()
		file_list = os.listdir(cur_dir)
		if search_name in file_list:
			print "find old one"
			continue	
		
		print >>sys.stderr, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

		comment_list = []
		final = {}
		output = get_num_comment(video_id)
		# print >>sys.stderr, output

		has_comment = output[0]  	
		# total_num_comment.append(int(output[1]))

		if(has_comment and int(output[1]) != 0):
    		# return 2 res: first: normal || last_page 
			# second: "good" || "HttpError"

			res = grab_comment(comment_list, video_id)
			token = res[0]
			status = res[1]
			#exception handling
			if status == "HttpError":
				print >>sys.stderr, "first time, it throws expection"
				response = ExceptionHandle(status, 5, comment_list, video_id)
				if response[0] == "fail":
					print >>sys.stderr, "can't start prcoess this video, break"
					continue
			#no exception, status ==  "good"
			while token != "last_page":
				res = grab_comment(comment_list, video_id, token)
				token = res[0]
				status = res[1]
				if status == "HttpError":
					response_new = ExceptionHandle(status, 5, comment_list, video_id, token)
					print >>sys.stderr, "################################"
					print >>sys.stderr, response_new

					if response_new[0] == "fail":
						print >>sys.stderr, "can't continue to prcoess this video, break here"
						break
					else:
						token = response_new[1][0]
				if status == "OtherError":
					break
		# print >>sys.stderr, comment_list 

		final["category_title"] = "Music"
		final["category_id"] = "10"
		final["video_title"] = video_title
		final["video_id"] = video_id
		final["comment_lst"] = comment_list

		new_name = "data_{}_10".format(video_id)
		with open(new_name, 'w') as outfile:
			json.dump(final, outfile)
		# file_count += 1

# print >>sys.stderr, total_num_comment


#start - mid | mid - end
def process(start, end):
	
	print >>sys.stderr, "---------------------------------------------------------------------------------------------------------"
	category_title = "Music"
	category_id =  "10"

	print >>sys.stderr, category_title
	print >>sys.stderr, category_id

	test = youtube_search(category_id)

	video_set = test[1]
	print "@@@@@@@@@@@@@@ length"
	print len(video_set)

	break_func(video_set, start, end)

	    	

if __name__ == "__main__":

	p1 = multiprocessing.Process(target = process, args =(0, 13,))
	p2 = multiprocessing.Process(target = process, args =(13, 26,))
	p3 = multiprocessing.Process(target = process, args =(26, 39,))
	p4 = multiprocessing.Process(target = process, args =(39, 51,))		

	p1.start()
	p2.start()
	p3.start()
	p4.start()

	p1.join()
	p2.join()
	p3.join()
	p4.join()	
   




