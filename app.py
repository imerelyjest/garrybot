import os
import json
import groupy

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, reqeuest

app = Flask(__name__)

@app.route('/', methods=['POST'])
def at_all(bot, group):
	members = group.members();

	user_ids = []
	loci = []
	text = ""
	pnt = 0

	for m in members:
		curm = m.identification()
		id = curm["user_id"]
		name = "@" + curm["nickname"] + " "

		user_ids.append(id)

n = [pnt, len(name)]
loci.append(n)
pnt += len(name)

text += name

mention = {}
mention["type"] = "mentions"
mention["user_ids"] = user_ids
mention["loci"] = loci

bot.post(text, mention)

def get_bot(groupID):
	for b in Bot.list():
		if b.group_id == groupID:
	return b



def log(msg):
	print(str(msg))
	sys.stdout.flush()