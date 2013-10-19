import tweepy
from tweepy import OAuthHandler
import time
from operator import itemgetter
import sys
""" UserDetails() used to fetch twitter user Details"""
class UserDetails():
	def fetch(self,name):

		"""Twitter Application Details"""
		CONSUMER_KEY = "gd6v4B5e7Nu2PhjMbDY6FA"
		CONSUMER_SECRET = "fmmDFlUJQPe5eOfTAlVTYU69MCYgDoldPGNfelzpvU"
		ACCESS_TOKEN = "1050567372-i1RAINRtG7BLEf1kCFOgFhVI5v5Z2oKm7RcGNWN"
		ACCESS_TOKEN_SECRET = "J9uYV0kZTnIuhxvSSVopvjuYkIirHtLS247MNDSiwLY"

		"""Authentication"""
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)
		try:	

			"""Connect to user"""
			user =api.get_user(name)
			resultVar=[]

			"""Fetch user's 15 recent tweets"""	
			timeline = api.user_timeline(screen_name=name, count=15)
			for tweet in timeline:
				"""Get Retweets"""
				results = api.retweets(tweet.id)
				for re in results:
					resultVar.append([re.user.screen_name,re.user.id,re.user.followers_count,re.user.profile_image_url])

			"""Sorting resultVar based on follower counts"""
			tempResults=sorted(resultVar, key=itemgetter(2),reverse=True)
			finalResult=[]
			for tempResult in tempResults:
				if tempResult not in finalResult:
					finalResult.append(tempResult)
				if len(finalResult)==15:
					break
			del finalResult[1]

			"""retutn user profile and final Result"""
			return user.profile_image_url,finalResult
			
		except Exception,e:
			print e
			return "ratelimit"
			
if __name__ == "__main__":
	userDetails=UserDetails()
	print userDetails.fetch(sys.argv[1])
