#adapted from:
#https://github.com/SeedlingsBabylab/subregsplice/blob/master/subrsplice.py#L56
import csv
import os



csvInputFile = 'verbs_onsets.csv' #change to csv file name
#csv file format:
# column 1 - file name without extension, column 2 - utterance onset (not used), column 3 - utterance offset (not used), column 4 - verb, column 5 - verb onset

extension = ".mp4" #change to video file extension (.mov, .mp4, etc)
csvHolder = []

with open(csvInputFile, newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		csvHolder.append(row)
csvFinal = [[0 for x in range(4)] for y in range(len(csvHolder))]

counter = 1
for row in range(0,len(csvHolder)): 
	csvFinal[row][0] = str(csvHolder[row][0]) + extension #set file input name
	csvFinal[row][2] = str(float(csvHolder[row][4])-3)#set onset time
	csvFinal[row][3] = str(5) #set offset time or time difference
	template = "{}_{}_{}_{}{}"
	kidID = str(csvFinal[row][0]).replace(extension,'')
	verb = csvHolder[row][3]
	csvFinal[row][1] = template.format(verb,kidID,counter,"5sec",extension) #set file output name
	counter= counter+1


for row in range(0,len(csvFinal)):
	onsetTime = csvFinal[row][2] #grabs onset time
	timeDiff = csvFinal[row][3] #grabs time difference
	fileName = csvFinal[row][0] #sets input filename
	outputPath = csvFinal[row][1] #sets output path
	command = ["ffmpeg","-ss",str(onsetTime),"-t",str(timeDiff),"-i",str(fileName),str(outputPath),"-y"]
	#command = ["ffmpeg","-ss",str(onsetTime),"-t",str(timeDiff),"-i",str(fileName),"-an",str(outputPath),"-y"] #for muting
	command_string = " ".join(command)
	print(command_string)
	os.system(command_string)

#below for adding beep
'''
	beepString = str(outputPath).replace(".mov","_beep.mov")
	command2 = ["ffmpeg","-i", str(outputPath), "-itsoffset","3","-i","beep2.mp3", "-map","0:0","-map","1:0","-preset","ultrafast",beepString]
	command_string2 = " ".join(command2)
	os.system(command_string2)'''
