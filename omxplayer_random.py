#!/usr/bin/env python
import os, random

def randomVideos ():
	randomfile = random.choice(os.listdir("/mnt/FHD/"))
	file = '/mnt/FHD/' + randomfile
	os.system ('omxplayer -b ' + file)

while True:
	randomVideos() #videoplayer
