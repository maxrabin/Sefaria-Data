# -*- coding: utf-8 -*-
import urllib
import urllib2
from urllib2 import URLError, HTTPError
import json 
import pdb
import os
import sys
from bs4 import BeautifulSoup
import re
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, p)
sys.path.insert(0, '../Match/')
from match import Match
os.environ['DJANGO_SETTINGS_MODULE'] = "sefaria.settings"
from local_settings import *
from functions import *

sys.path.insert(0, SEFARIA_PROJECT_PATH)
from sefaria.model import *
from sefaria.model.schema import AddressTalmud	

def boldFirstSentence(text):
	try:
		dh, comment = text.split(".",1)
	except:
		words = text.split(" ")
		first_one = 0
		for count, word in enumerate(words):
			if wordHasNekudot(word):
				first_one = count
				break
		comment =  " ".join(words[first_one:])
		dh = " ".join(words[0:first_one])
		comment = " "+comment
	return "<b>"+dh+".</b>"+comment
	
title = "Rashi_on_"+sys.argv[1]
f = open(title+'.txt','r')
perek = 0
text = {}
for line in f:
	line = line.replace('\n','').replace('\r','')
	first_word = line.split(" ")[0]
	perek = getGematria(first_word.replace('@',''))
	text[perek] = {}
	line = line[len(first_word):]
	comments = line.split("#")
	for count, comment in enumerate(comments):
		orig_comment = comment

		if len(comment)<3:
			continue
		left_p = comment.find("(")
		right_p = comment.find(")")
		poss_gematria = comment[left_p+1:right_p]
		if poss_gematria.find("-")>=0: 
			poss_gematria = poss_gematria[0:poss_gematria.find("-")]
		if poss_gematria.find('\xe2\x80\x93')>=0:
			poss_gematria = poss_gematria[0:poss_gematria.find('\xe2\x80\x93')]	
		verse = getGematria(poss_gematria)
		comment = comment[right_p+1:]
		if comment.find('\xc2\xa0')==0:
			comment = comment[2:]
		if verse in text[perek] or verse > 100:
			pdb.set_trace()
		text[perek][verse] = []
		
		words = comment.split(" ")
		prev_word_colon = False
		last_loc = 0
		for count, word in enumerate(words):
			if prev_word_colon:
				if not wordHasNekudot(word):
					separate_comment = " ".join(words[last_loc:count])
					separate_comment= boldFirstSentence(separate_comment)
					text[perek][verse].append(separate_comment)
					comment = " ".join(words[count:])
					last_loc = count
				prev_word_colon = False
			if word.find(":")>=0:
				prev_word_colon = True
		comment = boldFirstSentence(comment)
		text[perek][verse].append(comment)
for perek in text:
	text_to_post = convertDictToArray(text[perek])
	send_text = {
		"versionTitle":  "Pentateuch with Rashi's commentary by M. Rosenbaum and A.M. Silbermann",
		"versionSource": "http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI&docId=NNL_ALEPH001969084",
		"text": text_to_post,
		"language": "he"
	}
	try:
		post_text(title+"."+str(perek), send_text)
	except:
		pdb.set_trace()
