import json
import urllib2
import subprocess
import time
import datetime
import os
import re
import glob
import itertools


theme_prefix='theme*'
hashtag='kitty'
igurl = 'https://api.instagram.com/v1/tags/'+hashtag+'/media/recent?access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'



def listdirsfullpath(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]

def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]

def generateFrame(insertion,theme_use):
	subprocess.call(theme_use+".cmd " + insertion,shell=True)

def generateFrame_Unix(insertion,theme_use):
	subprocess.call("./" + theme_use + ".sh " + insertion + " >/dev/null",shell=True)	

def downloadJpg(url):
	uopen = urllib2.urlopen(url)
	stream = uopen.read()
	newfilename=url.replace("/","_")
	file = open((newfilename[7:]),'wb')
	file.write(stream)
	file.close
	#print newfilename[7:]
	return newfilename[7:]

def difference(a, b):
	return list(set(b).difference(set(a)))

def difference_super(a,b):
	newset = []
	first_set = set(map(tuple, a))
	second_set= set(map(tuple, b))

	for i in range(len(list(first_set))):
		dup_in_second=0
		for j in range(len(list(second_set))):
			subset_a=list(first_set)[i][2]
			subset_b=list(second_set)[j][2]
			if subset_a == subset_b:
				dup_in_second=1
		if dup_in_second == 0:
			newset.append(list(first_set)[i])
	return list(newset)

def showascii(filename):
	subprocess.call(["jp2a",filename,"--size=65x30"])

before_image_urls = []
for i in range(20):
	before_image_urls.append(str(i))
before_main_list = []
for i in range(20):
	before_main_list.append(list(str(i)))
main_list = []
before_complist = []
firstwhile=1;
infinite=1
dummy=0
time_before = datetime.datetime.now()


theme_list = [path for path in glob.glob(theme_prefix) if os.path.isdir(path)]
print theme_list
a = 0


while infinite == 1:


	try:
		response = urllib2.urlopen(igurl)

	except Exception as exception:
		while a < 10:
			print "HTTPError Exception, retrying 10 times"
			a = a + 1
			response = urllib2.urlopen(igurl)
			time.sleep(1)			

	info = json.load(response)
	
	main_list  = []	
	image_urls = []
	username   = []
	mediatype  = []
	full_name  = []
	profile_picture = []
	location     = []
	created_time = []
	likescount   = []
	captiontext  = []
	commenttext  = []
	utf8string   =" "

	for post in info['data']:
		image_urls.append(post["images"]["standard_resolution"]["url"])
		username.append(post["user"]["username"])
		mediatype.append(post["type"])
		full_name.append(post["user"]["full_name"])
		profile_picture.append(post["user"]["profile_picture"])
	#	location.append(post["location"]["latitude"])
		if str(post["location"])== "None":
			#print "No Location"
			location.append("null")
		else:
			try:
				if str(post["location"]['name']) <> "None":
					#This thing got name
					location.append(post["location"]["name"])
			except:
				#LatLong Only
				location.append("null")
		created_time.append(post["created_time"])
		likescount.append(post["likes"]["count"])
		
		try:
			if str(post["caption"]["text"]) <> "None":
				captiontext.append(post["caption"]["text"])
			else:
				captiontext.append("null")
		except:
				captiontext.append("null")

		if int(post["comments"]["count"]) == 0:
			dummy=0
		else:
			for commentpost in post['comments']['data']:
#				print str("write txt")
				utf8string=utf8string+(commentpost["from"]["username"]+u" "+commentpost["text"]+u"\n")
		commenttext.append(utf8string)
		utf8string=""
	

	for eachOne in range(len(username)):
		sublist = []
		sublist.append(username[eachOne])			#0
		sublist.append(mediatype[eachOne])			#1
		sublist.append(image_urls[eachOne])			#2
		sublist.append(profile_picture[eachOne])		#3
		sublist.append(created_time[eachOne])			#4
		sublist.append(location[eachOne])			#5
		sublist.append(likescount[eachOne])			#6
		sublist.append(captiontext[eachOne])			#7
		sublist.append(commenttext[eachOne])			#8
		main_list.append(sublist)

#	print "======"

	if firstwhile == 1:
		before_main_list = main_list

	
	list_diff=difference_super(main_list,before_main_list)
	before_main_list=main_list

#	print len(list_diff)
	if len(list_diff) > 0 and firstwhile == 0:
		print "Incoming Feed for:"+str(len(list_diff)) 
		for eachOne in range(len(list_diff)):
			picturedate=datetime.datetime.fromtimestamp(int(list_diff[eachOne][4]))
			print ("Username: "+str(list_diff[eachOne][0])+"\t"+picturedate.strftime("%I:%M%p"))
			print ("Likes :"+str(list_diff[eachOne][6]))
#			print ("Caption"+(list_diff[eachOne][7]))
#			print ("Created:",datetime.datetime.fromtimestamp(int(list_diff[eachOne][4])))
#			print str(list_diff[eachOne][5])
		
			try:		
				filename_profile=downloadJpg(list_diff[eachOne][3])
				filename_main=downloadJpg(list_diff[eachOne][2])

				if list_diff[eachOne][7].encode('utf8') <> "":
					captionfile=open(filename_main+".cap","wb")
					captionfile.write(list_diff[eachOne][7].encode('utf8'))
					captionfile.close()
				else:
					dummy=0

				if list_diff[eachOne][8].encode('utf8') <> "":
					print "[...]"

					commentlabel=open(filename_main+".txt","wb")
					commentlabel.write(list_diff[eachOne][8].encode('utf8'))
					commentlabel.close()
				else:
					dummy=0
				theme_use="default_theme"		
				for ii in range(len(theme_list)):
					#print "#"+theme_list[ii]
					#print list_diff[eachOne][7].encode('utf8')
					if "#"+theme_list[ii] in list_diff[eachOne][7].encode('utf8'):
						#print "<Theme Match>"
						theme_use=theme_list[ii]
						break
					else:
						dummy=0

					#print list_diff[eachOne][8].encode('utf8')
					if "#"+theme_list[ii] in list_diff[eachOne][8].encode('utf8'):
						theme_use=theme_list[ii]
						break
					else:
						dummy=0

				print theme_use

				generateFrame(	'\042' + str(list_diff[eachOne][0]) +'\042 '+
			       				'\042' + str(list_diff[eachOne][5]) +'\042 '+
	                          	'\042' + str(filename_profile)  +'\042 '+
	                         	'\042' + str(filename_main)     +'\042 '+
		       					'\042' + str(picturedate.strftime("%b-%d-%Y %I:%M%p")) + '\042 '+
								'\042' + str(list_diff[eachOne][6]) + '\042 ' +
								'\042' + str(filename_main+".cap") + '\042',theme_use)
								


			except:
				print "* Error Getting Images: Photo has been deleted or permission denied"
	else:
		print ".zzZ"
	
	print "-----------------------------------------------"

	time_now = datetime.datetime.now()

	print (time_now - time_before).total_seconds()

	if (time_now - time_before).total_seconds() < 6:
		time_before=time_now
		time.sleep(5)
	else:
		time_before=time_now
		time.sleep(1)
	firstwhile=0
#-- END WHILE



