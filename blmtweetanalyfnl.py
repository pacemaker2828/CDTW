# Read Twitter tweets and outputs results to a CSV file
# Georgetown CCPE Data Science Program
# Team CDWT
# Created:  May 2016
#
# Copyright (C) 2016
# For license information, see LICENSE.txt
#
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "CONSUMER YOUR KEY GOES HERE"
consumer_secret = "CONSUMER SECRET KEY GOES HERE"
access_key = "ACCESS KEY GOES HERE"
access_secret = "ACCESS SECRET KEY GOES HERE"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass


#pass in the username of the account you want to download
if __name__ == '__main__':


	cdtwactvs = ["SankofaBrown","MichaelEDyson","MalcolmJamalWar",
	"FoxNews","CNN","BET","MSNBC","NAACP"];

	for activist in cdtwactvs:
		print "***The activist hagtag is: %s" % activist
		get_all_tweets(activist)
		#get_all_tweets
