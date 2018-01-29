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



def process(start, end):

	with open('videoCategories.json') as json_data:
	    d = json.load(json_data)
	    category_data = d["items"]

	    # total_num_comment = []
	    for i in range(start,end):
	    	print >>sys.stderr, "---------------------------------------------------------------------------------------------------------"
	    	category_title = category_data[i]["snippet"]["title"]
	    	category_id =  category_data[i]["id"]

	    	print >>sys.stderr, category_title
	    	print >>sys.stderr, category_id

	    	test = youtube_search(category_id)

	    	video_set = test[1]
	   
	    	video_id_list = []

	    	# for i in range(0, len(video_set)):
	    	# 	video_id_list.append(video_set[i]["id"]["videoId"])
	    	# print >>sys.stderr, video_id_list

	    	
	    	for i in range(0, len(video_set)):
	    		video_title = video_set[i]["snippet"]["title"]
	    		video_id = video_set[i]["id"]["videoId"]

	    		# search_name = "data_{}.text".format(video_id) #file to be searched
	    		# cur_dir = os.getcwd()
	    		# file_list = os.listdir(cur_dir)
	    		# if search_name in file_list:
	    		# 	print "find old one"
	    		# 	continue				

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

	    		final["category_title"] = category_title
	    		final["category_id"] = category_id
	    		final["video_title"] = video_title
	    		final["video_id"] = video_id
	    		final["comment_lst"] = comment_list

	    		new_name = "data_{}_{}".format(video_id, category_id)
	    		with open(new_name, 'w') as outfile:
	    			json.dump(final, outfile)
	    		# file_count += 1

	    # print >>sys.stderr, total_num_comment

if __name__ == "__main__":

	p1 = multiprocessing.Process(target = process, args =(6, 7,))
	p2 = multiprocessing.Process(target = process, args =(7, 8,))
	p3 = multiprocessing.Process(target = process, args =(8, 9,))

	p1.start()
	p2.start()
	p3.start()

	p1.join()
	p2.join()
	p3.join()	
    




