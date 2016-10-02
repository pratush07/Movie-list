from imdbpie import Imdb
import os
import os.path
import sys
import time
import itertools



def writeFile(file,titleList,threshhold):
	i = 1 
	for title in titleList:
		try :
			percent = int((i/float(len(titleList)))*100)
			print str(percent)+"%"+" done"
			titles = imdb.search_for_title(title)
		except Exception as e:
			os.remove(outputFileName)
			print "error occured.."+str(e)
			print "removing output file"
		if titles:
			title_id = titles[0]['imdb_id'] 
			rating = imdb.get_title_by_id(title_id).rating
			if rating >= threshhold:
				file.write(str(title)+" "+str(rating)+"\n")
		else:
			print "movie not found!"
		i = i+1

if __name__ == "__main__":

	threshhold=float(sys.argv[1])
	titles=sys.argv
	titles.pop(0)
	titles.pop(0)
	print titles
	outputFileName='movies.txt'
	# titles=["the dark knight","the dark knight rises","the notebook"]
	# path = "/Users/pratush/Downloads"
	# threshhold = 8

	# titles=set([])
	# for dirpath, dirnames, filenames in os.walk(path):
	#     for filename in [f for f in filenames if f.endswith(".mp4") or f.endswith(".mkv") or f.endswith(".avi")]:
	#         titles.add(filename)
	imdb = Imdb()
	imdb = Imdb(anonymize=True) # to proxy requests
	try:
	    with open(outputFileName,'r') as file:
	        print "deleting old output file.."
	        os.remove(outputFileName)
	        print "creating a new outputfile.."
	        with open(outputFileName,'a') as fa:
	        	writeFile(fa,titles,threshhold)

	except IOError as e:
		print "creating an output file"
		with open(outputFileName,'a') as fa:
			writeFile(fa,titles,threshhold)

