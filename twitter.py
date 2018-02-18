import tweepy
import time

ACCESS_TOKEN = '964996958283816960-BSFfv4POCwkjBZFM3nODVMsGm6afjVP'
ACCESS_SECRET = 'ZVg2i4QoJprEQvik4f1n9TLEPf4yezM8hMNz8DY2157ZR'
CONSUMER_KEY = 'HaIZ2Gev3AoZSud3sMVYoncqk'
CONSUMER_SECRET = 'D5HRf1Sm0KOTBvMDT9jnm1ZYZnNri3cBu39hLP7wkFZ3VZxbtr'
SEARCH = 'trump'  # input("Enter the search string ")
FROM = '2018-01-01'  # input("Enter the from date (YYYY-MM-DD format) ")
TO = '2018-02-17'  # input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH = './' + 'output.txt'  # SEARCH + '.txt'

num = 500  # int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i = 0

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since=FROM, until=TO,
                         include_entities=True, lang="en").items(num):
    i += 1
    f.write(res.user.screen_name)
    f.write(' ')
    f.write('[')
    f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
    f.write(']')
    f.write(" ")
    f.write('"')
    f.write(res.text.replace('\n', ''))
    f.write('"')
    f.write(" ")
    f.write(str(res.user.followers_count))
    f.write(" ")
    f.write(str(res.retweet_count))
    f.write('\n')
f.close
print("Tweets retrieved ", i)
