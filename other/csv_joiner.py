import csv
import os


dir = "S:/yayzhang/HSP_Verb_clips/HSP_code" #change


masterCsv = []

for root, dirs, files in os.walk(dir):
	for file in files:
		if "verbonset_cleaned" in file:
			filepath = os.path.join(root, file)
			with open(filepath, newline="") as csvfile:
				reader = csv.reader(csvfile, delimiter=",",quotechar="|")
				for row in reader:
					masterCsv.append(row)


with open("compiledValues.csv","w",newline="") as csvfile:
	writer = csv.writer(csvfile, delimiter=",",quotechar="|", quoting = csv.QUOTE_MINIMAL)
	for item in masterCsv:
		writer.writerow(item)