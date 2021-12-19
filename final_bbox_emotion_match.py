# Created by Naman and Gaurav
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import json

emotion = []

with open('Final_face_to_emotion.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        emotion.append(row[1])

emotion = emotion[1:]

with open('bbox_master.json') as file:
    for line in file:
        jsonobj = line
jsonobj = json.loads(jsonobj)

img_size = len(jsonobj)

double = {}

counter = 0
for i in range(1,img_size+1):
    keyname = "image" + str(i)
    inner= {}
    for j in range(0,len(jsonobj[i-1])):
        bbox = jsonobj[i-1].values()
        for val in bbox:
            inner[str(val)] = emotion[counter]
        # bbox = "bbox" + str(j)
        counter += 1
    double[keyname] = inner

# print(double)

#saves file to json
with open("data_file.json", "w") as write_file:
    json.dump(double, write_file)