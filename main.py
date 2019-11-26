import praw
import json
import os
import sys
import re
from flask import Flask

reg_image = r"(https://)(i\.redd\.it|imgur\.com)(/[a-z0-9]{1,})(\.jpg|\.png)"

if not os.path.exists("config.json"):
    raw_data = {
        "client_id": "",
        "client_secret": "",
        "user_agent": ""
    }
    with open("config.json", "w") as raw_prawcfg:
        json.dump(raw_data, raw_prawcfg)

if os.path.exists("config.json"):
    with open("config.json", "r") as raw_prawcfg:
        prawcfg = json.load(raw_prawcfg)

# Can't think of a way to check if values are "None"
print(" [DEBUG] cfg len:", len(prawcfg['client_id']), len(prawcfg['client_secret']), len(prawcfg['user_agent']))

if len(prawcfg['client_id']) or len(prawcfg['client_secret']) or len(prawcfg['user_agent']) == 0:
    print(" [ERROR] Modify the config.")
    sys.exit(0)

reddit = praw.Reddit(client_id = prawcfg['client_id'],
                     client_secret = prawcfg['client_secret'],
                     user_agent = prawcfg['user_agent'])
for i in range(25):
    i = i + 1
    for submission in reddit.subreddit('random').hot(limit=1):
        if re.match(reg_image, submission.url):
            print(i, submission.url)
            #takeurl = submission.url
            #flask_export(takeurl)

#app = Flask(__name__)
#
#@app.route('/')
#def flask_export(takeurl):
#    return takeurl
#
#if __name__ == '__main__':
#    app.run(debug=True)