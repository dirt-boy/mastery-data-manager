"""Raw data processor. Converts `submissions.json` to csv format."""

#make new dict
#{coursename: {coursework: {student: [grades]}, ..}, ..}

#Get list of all unique course titles
#get list of each

import csv
import json
import os
from datetime import date

import numpy as np
FILEDIR = "logs"
HEADERS = "title, criteria_tag, criteria_content_description, criteria_content_level_title, criteria_content_point_value, student, flag, class\n"
DATE = date.today().strftime('%m_%d_%y')

def unique(list):
	x = np.array(list)
	return np.unique(x)

def get_classes(raw):
	classes = []
	for i, grade in enumerate(raw):
		if not grade['course'] in classes:
			classes.append(grade['course'])
	return unique(classes)

def get_courseworks(raw, classes):
	#get unique courseworks
	courseWorks = []
	for c in classes:
		for i in raw:
			if c == i['course']:
				courseWorks.append(i['courseWork'])
	return unique(courseWorks)

def get_students(raw):
	students = []
	for i, grade in enumerate(raw):
		grade['user']
	return students

def pare(raw):
	x = []
	for i, g in enumerate(raw):
		y = []
		if type(raw[i]) == dict:
			for j, t in enumerate(raw[i]['titles']):
				if j%2 == 0:
					y.append(raw[i]['titles'][j])
			x.append(y)
	return x


def fullconvert():
	aggregate = []
	csv = ""
	for file in os.listdir(FILEDIR):
		if "submissions" in str(file):
			with open(FILEDIR+"/"+file, "r") as f:
				try:
					raw = f.read()
					name = str(file)
					name = name[:len(name)-5]+".csv"
					raw = json.loads(raw)
					aggregate.append(raw)
					#print("Data for: %s" % name, ": \n", raw)
				except:
					print("Error occurred.")
	for i, chunk in enumerate(aggregate):
		if i == 0:
			csv += HEADERS
		for j, grades in enumerate(chunk):
			for j, title in enumerate(grades["titles"]):
				if j < len(grades["grades"]):
					row = grades["courseWork"]+", "+title+" , ,"+grades["grades"][j]+" ,"+grades["grades"][j][:1]+" ,"+grades["user"]+" , TRUE,"+grades["course"]+"\n"
					csv += row
	with open("results/grades_"+DATE+".csv", "w") as f:
		f.write(csv)



if __name__ == "__main__":
	fullconvert()