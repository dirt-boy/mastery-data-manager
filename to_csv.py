#raw data processor

#make new dict
#{coursename: {coursework: {student: [grades]}, ..}, ..}

#Get list of all unique course titles
#get list of each 

import os
from os import path
import json
import numpy as np
import csv

def unique(list):
	x = np.array(list)
	return np.unique(x)

def read(file):
	save_path = "/Users/gg/NerdStuff/mastery-data-manager/logs"
	completename = os.path.join(save_path, str(file))
	with open(completename, 'r') as f:
		data = f.read()
	data_r = data.replace("'", '"')
	data_j = json.loads(data)
	return data_j

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

raw = read('submissions.json')
classes = get_classes(raw)
courseworks = get_courseworks(raw, classes)
students = get_students(raw)

def pare(raw):
	x = []
	for i, g in enumerate(raw):
		y = []
		for j, t in enumerate(raw[i]['titles']):
			if j%2 == 0:
				y.append(raw[i]['titles'][j])
		x.append(y)
	return x	

def zip(raw, pared):
	for i, g in enumerate(raw):
		for j, t in enumerate(pared):
			raw[i]['titles'] = pared[j]
	return raw

def process(raw):
	return zip(raw, pare(raw))

def restructure(raw):
	x = []
	for i, g in enumerate(raw):
		print("x" * i)
		#print(g)
		for j, r in enumerate(raw[i]['grades']):
			print("\n")
			#print('\n\n'+str(len(raw[i]['grades'])))
			#print('\n\n'+str(raw[i]['grades']))
			#print('\n\n'+str(g['titles'][j]))
			x.append(
				[g['courseWork'], g['titles'][j], "", g['grades'][j][:-2], g['grades'][j][0], g['user'], 'TRUE', g['course']]
				)
	return x

def writecsv(restructured):
	restructured[:0] = [['title','criteria__tag','criteria__content__description','criteria__content__level__title','criteria__content__point__value','student','flag','class']]
	with open('grades.csv', 'w') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',')
		csvwriter.writerows(restructured)

def fullconvert():
	processed = process(raw)
	restructured = restructure(processed)
	return writecsv(restructured)

fullconvert()



	



	
	
