#!/usr/bin/env python

from __future__ import print_function
import os, sys, re, requests
from config import *

def get_message():
    files = [os.path.join('/var/spool/gammu/inbox/', m) for m in sys.argv[1:]]
    files.sort() # make sure we get the parts in the right order
    number = re.match(r'^IN\d+_\d+_\d+_(.*)_\d+\.txt', os.path.split(files[0])[1]).group(1) 
    text = ''
    for f in files:
        text += open(f, 'r').read()
    try:
        text = text.decode('UTF-8', 'strict')
    except UnicodeDecodeError:
        text = text.decode('UTF-8', 'replace')
    return number, text

number, text = get_message()

request = requests.post("https://api.telegram.org/bot"+tg_bot_api_key+"/sendMessage", data={
    'chat_id': tg_chat_id,
    'text': number + ": " + text
})

