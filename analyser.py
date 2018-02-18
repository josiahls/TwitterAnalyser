from datetime import datetime
import heapq
from TweetHandler import TweetHandler


def analyze_date():
    print('Setting overall tweets...')
    # overall tweets
    q = []
    for entry, value in user_number_of_tweets_overall.items():
        heapq.heappush(q, (-1 * int(value), entry))

    write_date(q, "user total tweets", 'User: ', ' Total tweets: ')

    print('Setting overall tweets per hour...')
    # overall tweets per hour
    q = []
    for entry, value in user_number_of_tweets_per_hour.items():
        heapq.heappush(q, (-1 * int(value), entry))

    write_date(q, "user total per hour", 'User: ', ' Max Total tweets for one hour: ')

    print('Setting max user followers...')
    # max user followers
    q = []
    for entry, value in user_number_of_followers.items():
        heapq.heappush(q, ((-1 * int(value)), entry))
    # while q:
    #     next_item = heapq.heappop(q)
    #     print(next_item)

    write_date(q, "user max followers", 'User: ', ' Total followers: ')

    print('Setting max retweets...')
    # max retweets
    q = []
    for entry, value in number_of_retweets_per_tweet.items():
        heapq.heappush(q, (-1 * int(value), entry))

    write_date(q, "max retweets of tweets", 'Tweet: ', ' Total reweets: ')


def write_date(q=None, title=str(), detail1=str(), detail2=str(), is_reversed=True):
    if q is None or not q:
        print("q is empty. Exiting")
        return

    i = -1 if is_reversed else 1

    f = open(title + '.txt', mode='w')
    for j in range(0, N_USERS):
        next_item = heapq.heappop(q)
        f.write(detail1 + next_item[1] + detail2 + str((i * int(next_item[0]))))
        f.write('\n')

    f.close()


if __name__ == '__main__':
    # TweetHandler
    th = TweetHandler()

    # number of users to show
    N_USERS = input("Enter number of users to show data for: ")

    # data sets
    tweets = []
    user_number_of_tweets_overall = dict()
    user_number_of_tweets_per_hour = dict()
    user_number_of_followers = dict()
    number_of_retweets_per_tweet = dict()

    f = open('output.txt', 'r', encoding='utf-8')

    print('Reading output...')
    # go through each tweet
    for line in f.readlines():
        # print(line)
        # print("username: " + get_username(line))
        # print("tweet_name: " + get_tweet_name(line))
        # print("tweet_time: " + get_tweet_dt(line).__str__())
        # print("tweet_followers: " + get_num_followers(line))
        # print("tweet_retweets: " + get_num_retweets(line))
        tweets.append(line)
        username = th.get_username(line)
        tweet_id = th.get_tweet_name(line)
        tweet_dt = th.get_tweet_dt(line)

        # Add the user's number of tweets total
        if username in user_number_of_tweets_overall:
            user_number_of_tweets_overall[username] += 1
        else:
            user_number_of_tweets_overall[username] = 1

        # Add the user's followers
        # note, the else is removed
        # we want the MOST RECENT followers for that user
        if username not in user_number_of_followers:
            user_number_of_followers[username] = th.get_num_followers(line)

        # Add the tweets's retweets
        if tweet_id not in number_of_retweets_per_tweet:
            number_of_retweets_per_tweet[tweet_id] = th.get_num_retweets(line)

    # Add tweets per hour for each user
    print('Detecting for tweets per hour...')
    for i, tweet in enumerate(tweets):
        # get the current tweet date and username
        tweet_dt = th.get_tweet_dt(tweet)
        username = th.get_username(tweet)

        j = i - 1
        hours = 0
        hits = 1
        while j > 0 and hours <= 1:
            # get the next previous tweet's date and username
            previous_tweet_dt = th.get_tweet_dt(tweets[j])
            previous_tweet_username = th.get_username(tweets[j])

            # get the hours difference between the two
            difference = previous_tweet_dt - tweet_dt
            hours = difference.seconds / 60 / 60
            hits = hits + 1 if username == previous_tweet_username and hours <= 1 else hits
            j -= 1

        if username in user_number_of_tweets_per_hour:
            if user_number_of_tweets_per_hour[username] < hits:
                user_number_of_tweets_per_hour[username] = hits
        else:
            user_number_of_tweets_per_hour[username] = hits

    analyze_date()
