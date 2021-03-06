"""

A simple Twitter bot using the Twitter Python library that finds users who tweet about "Christmas gift ideas," 
favorites their tweet, follows the users and sends them a friendly tweet with Amazon links of popular gift ideas.
 
"""

import urllib
import simplejson
import twitter

consumer_key = 'Y6dSH82jVCQvVzrkjk3JQ'
consumer_secret = '4XykXa3D2eqk6pTI8UDUKgjt3GBEV3GYqaKuFe0jD2A'
access_token_key = '983701741-kX9UNcOHw5nY2eDoW0vOJQdVRYtI6dwd2bzASCoD'
access_token_secret = 'eZyBJ5xSBrEZio3NX3Rf99wMlTWJheIhEezPu7BQ4s'

def searchTweets(query):
	search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
	dict = simplejson.loads(search.read())
	return dict

api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)
tweets = searchTweets("christmas+gift+ideas&rpp=100&result_type=recent")
msg = 'Internet neighbor! Saw your tweet - here are my Xmas gift ideas! Him: http://amzn.to/TDjghP Her: http://amzn.to/TEWDbY'

for i in range(len(tweets["results"])):
	tweeter = tweets["results"][i]["from_user"]
	status = twitter.Api.GetStatus(api, tweets["results"][i]["id"])
	api.CreateFavorite(status)
	api.CreateFriendship(tweeter)
	api.PostUpdate('@' + tweeter + ' ' + msg)
