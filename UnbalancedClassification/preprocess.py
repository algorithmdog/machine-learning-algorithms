#!/bin/python
import random

f = open("TV_News_Channel_Commercial_Detection_Dataset/TIMESNOW.txt")
train_file = open("dataset/train","w")
test_file  = open("dataset/test","w")

n = 0;
for line in f:
	line  = line.strip()
	lines = line.split(" ")

	
	if(lines[0] == "1"):
		if random.random() < 0.05:
			train_file.write(line+"\n")
		else:
			test_file.write(line+"\n")

	else:
		if random.random() < 0.95:
			train_file.write(line+"\n")
		else:
			test_file.write(line+"\n")
	n += 1

print n
