import simplejson, urllib
import datetime
import sys, codecs
import re

url = "https://api.twitter.com/1/statuses/user_timeline.json?screen_name=apoakley&count=200&include_rts=t"
tweets = simplejson.load(urllib.urlopen(url))

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

print "Random things shared on Twitter from the week:"

for tweet in tweets:
	text = tweet['text']
        text = text.replace('[', '(').replace(']', ')')
        pattern = re.compile(r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\"]))")
        if not pattern.search(text):
                continue
        text = pattern.sub(r'[\1](\1)', text)

	created_at = datetime.datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")


	if (datetime.datetime.now() - created_at < datetime.timedelta(weeks=1)):
#		print created_at.strftime("%a %H:%M"),text
		if (not(text.startswith("Blog:") or text.startswith("@"))):
			print " * ", text
