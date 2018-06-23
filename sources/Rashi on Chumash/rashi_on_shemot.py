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
		return "<b>"+dh+".</b>"+comment
	except:
		return "<b>"+text+"</b>"
	
title = "Rashi_on_Shemot"
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
	for comment in comments:
		if len(comment)<3:
			continue
		left_p = comment.find("(")
		right_p = comment.find(")")
		poss_gematria = comment[left_p+1:right_p]
		if poss_gematria.find("-")>=0:
			poss_gematria = poss_gematria[0:poss_gematria.find("-")]	
		verse = getGematria(poss_gematria)
		comment = comment[right_p+1:]
		if verse in text[perek]:
			pdb.set_trace()
		text[perek][verse] = []
		while comment.find(":") != comment.rfind(":"):
			first_colon = comment.find(":")
			post_comment = comment[0:first_colon+1]
			post_comment = boldFirstSentence(post_comment)
			text[perek][verse].append(post_comment)
			comment = comment[first_colon+1:]
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
	post_text(title+"."+str(perek), send_text)
pdb.set_trace()
