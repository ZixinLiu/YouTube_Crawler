from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import sys
import json
import time

DEVELOPER_KEY = "AIzaSyCjMXhetLNmpv3udNv0eGOWs2bZji1w9Kk"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(video_Category_Id,max_results=50,order="viewCount", token=None, region_Code="US"):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    type="video",
    videoCategoryId= video_Category_Id,
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    regionCode= region_Code,

  ).execute()

  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
  try:
      nexttok = search_response["nextPageToken"]
      return(nexttok, videos)
  except Exception as e:
      nexttok = "last_page"
      return(nexttok, videos)


def get_num_comment(video_id):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

	response = youtube.videos().list(
		id = video_id,
		part = "statistics",
	).execute()
	# print >>sys.stderr, "####################################"
	has_comment = True
	num_comment = 0
	if("commentCount" in response["items"][0]["statistics"]):
		num_comment = response["items"][0]["statistics"]["commentCount"]
		print >>sys.stderr, num_comment
	else:
		has_comment = False
	return (has_comment, num_comment)


# given a video_id, return a list of ids for all comments for this video
def get_comment(video_id, next_Page_Token=None):

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
	
	response = youtube.commentThreads().list(
		part = 'snippet',
		videoId = video_id,
		maxResults = 100,
		pageToken = next_Page_Token,
	).execute()

	# print >>sys.stderr, response
	
	thread = response["items"]
	print >>sys.stderr, "***********************************************************************"

	# print >>sys.stderr, thread

	# for comment_result in response.get("items",[]):
	# 	if comment_result["kind"] == "youtube#commentThread":
	# 		thread.append(comment_result)
	
	print >>sys.stderr, len(thread)
	if "nextPageToken" not in response:
		nextPageToken = "last_page"
	else:
		nextPageToken = response["nextPageToken"]

	return(nextPageToken,thread)





# return 2 res: first: normal || last_page 
# 			  second: "good" || "HttpError"




def grab_comment(comment_list, video_id, next_Page_Token=None):
	try:
		res = get_comment(video_id, next_Page_Token)
		next_Page_Token = res[0]
		print >>sys.stderr, next_Page_Token
		for i in res[1]:
			publish_time = i["snippet"]["topLevelComment"]["snippet"]["publishedAt"]		
			publisher_name = i["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
			comment_text = i["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
			if "authorChannelId" not in i["snippet"]["topLevelComment"]["snippet"]:
				# print >>sys.stderr, json.dumps(i)
				continue
			channel_id = i["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]
			comment_dict = {'publish_time':[], 'publisher_name':[], 'channel_id':[], 'comment_text':[]}

			comment_dict["publish_time"] = publish_time
			comment_dict["publisher_name"] =publisher_name
			comment_dict["channel_id"] = channel_id
			comment_dict["comment_text"] = comment_text

			# print >>sys.stderr, comment_dict
			# print >>sys.stderr, "\n"

			comment_list.append(comment_dict)

			#token: nexttok or "last_page"
		return (next_Page_Token, "good")

	except HttpError, e:
		print >>sys.stderr, "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
		return(next_Page_Token,"HttpError")
	except :
		return(next_Page_Token, "OtherError")
def ExceptionHandle(status, num_trail, comment_list, video_id, next_page_token=None, response=None):

	if status == "good":
		return("success", response)
	if num_trail == 0:
		return("fail", response)
	# status is still http error, but there are trails left
	time.sleep(10)
	res = grab_comment(comment_list, video_id, next_page_token)
	token = res[0]
	status = res[1]
	num_trail -= 1
	return ExceptionHandle(status, num_trail, comment_list, video_id, token, res)

