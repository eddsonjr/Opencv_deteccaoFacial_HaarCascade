import os 
import subprocess as sbp 
import string

#Warning: Put this script into your pictures folder with D_N_Images program

#global vars 
listOfFiles = []


#function to load files in a list
def loadFilesOnList(path):
	for file in os.listdir(path):
		if file.endswith(".jpg"):
			listOfFiles.append(file)

	#print number of files
	print "Number of files loaded:" 
	print len(listOfFiles)



#recursive function to execute D_N_Images
def call_D_N_Images_MediamBlur(count):
	if count >= len(listOfFiles):
		print "Exiting... "
		return

	#get path of file
	filePath = os.path.abspath(listOfFiles[count])
	#get name of file and put in upper case
	fileName = os.path.splitext(listOfFiles[count])[0]
	fileName = fileName.upper()
	
	#prepare command line to call D_N_Images for MediamBlur
	sufix = fileName + '_mediamblur5'
	#call extern process D_N_Images to 
	sbp.call(['./D_N_Images',filePath,'10','1','5',sufix])

	


	#recursive call
	count = count+1
	call_D_N_Images_MediamBlur(count)




def call_D_N_Images_Bilateral(count):
	if count >= len(listOfFiles):
		print "Exiting... "
		return

	#get path of file
	filePath = os.path.abspath(listOfFiles[count])
	#get name of file and put in upper case
	fileName = os.path.splitext(listOfFiles[count])[0]
	fileName = fileName.upper()

	#prepare command line to call D_N_Images for bilateral filter
	sufix2 = fileName + '_bilateral25'
	#call extern process
	sbp.call(['./D_N_Images',filePath,'10','2','25',sufix2])


	#recursive call
	count = count+1
	call_D_N_Images_Bilateral(count)



def  call_D_N_Images_homogeneous(count):
	if count >= len(listOfFiles):
		print "Exiting... "
		return

	#get path of file
	filePath = os.path.abspath(listOfFiles[count])
	#get name of file and put in upper case
	fileName = os.path.splitext(listOfFiles[count])[0]
	fileName = fileName.upper()

	#prepare command line to call D_N_Images for homogeneousBlur
	sufix3 = fileName + '_homogeneous6'
	#call extern process
	sbp.call(['./D_N_Images',filePath,'10','3','6',sufix3])


	#recursive call
	count = count+1
	call_D_N_Images_homogeneous(count)





#function callback
pathOfPhotos = '.'
loadFilesOnList(pathOfPhotos)

call_D_N_Images_MediamBlur(0)
call_D_N_Images_Bilateral(0)
call_D_N_Images_homogeneous(0)


print "Pyton: All process terminated... "







