# -*- coding: utf-8 -*-
import os
import time
import sys
import re
from termcolor import colored

def isVowel(letter):
	vowels = ['a','e','i','o','u']
	if (letter in vowels):
		return True
	else:
		return False

def spritzText(text, speed, highlight):
	timeStarted = time.time()
	splitText = re.findall(r"[\w']+",text)
	wordCount = 0
	for word in splitText:
		redPos = 0
		letterReset = 1
		os.system("clear")
		wordArray = word.split()
		formattedWord = []
		letterCount = 0
		for letter in word:
			if (letterReset == 1 and isVowel(letter) and (letterCount > 1 or len(word) < 5)):
				letter = colored(letter,highlight)
				letterReset = 0
				redPos = letterCount
			formattedWord.insert(letterCount, letter)
			letterCount = letterCount + 1
		markerPosition = 12
		if (redPos < markerPosition):
			spacer = " " * (markerPosition-redPos-1)
		print "┌──────────┬──────────┐"
		print spacer + "".join(formattedWord)
		print "└──────────┴──────────┘"
		print "Time elapsed: " + str(round(time.time()-timeStarted)) +"s"
		if (wordCount == 0):
			time.sleep(1.5)
		else:
			time.sleep(speed)
		wordCount = wordCount + 1

os.system("clear")
speed = 0
file = sys.argv[1]
if (len(sys.argv) > 2):
	speed = sys.argv[2]
if (len(sys.argv) > 3):
	highlight = sys.argv[3]
else:
	highlight = "red"

if (file is None):
	print "Error: no file found!"
else:
	with open(file, "rb") as f:
		text = f.read().replace('\n',' ')
		text = str(text).strip()
		if (speed == 0):
			speed = raw_input("How many words per minute? ")
		speed = 1/(float(speed)/60)
		spritzText(text, speed, highlight)

exit()
