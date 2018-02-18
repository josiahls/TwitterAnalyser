from datetime import datetime


class TweetHandler(object):
    def __init__(self):
        pass

    def get_username(self, line=str()):
        """
        Return the username of the tweet
        :param line: the tweet with params
        :return: only the username
        """
        return line.split(' ')[0]

    def get_num_followers(self,line=str()):
        """
        Return the number of followers of the tweet
        :param line: the tweet with params
        :return: only the number of followers
        """
        num_retweets_and_followers = line.split('"')[-1].strip()
        return num_retweets_and_followers.split(' ')[1]

    def get_num_retweets(self,line=str()):
        """
        Return the number of retweets of the tweet
        :param line: the tweet with params
        :return: only the number of retweets
        """
        num_retweets_and_followers = line.split('"')[-1].strip()
        return num_retweets_and_followers.split(' ')[0]

    def get_tweet_name(self,line=str()):
        """
        Return the tweet unique name.
        A combination of the time and the username
        :param line: the tweet with params
        :return: only custom defined tweet id
        """
        return line.split(']')[0] + ']'

    def get_tweet_dt(self,line=str()):
        """
        Return the datetime of the tweet
        :param line: the tweet with params
        :return: the datatime object
        """
        left = line.split('[')[1]
        time_only = left.split(']')[0]

        format_dt = '%d/%b/%Y:%H:%M:%S'
        tweet_dt = datetime.strptime(time_only.strip(), format_dt)

        return tweet_dt
