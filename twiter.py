import tweepy
import time

if __name__ == '__main__':
    auth = tweepy.OAuthHandler('m7yOvFvCchSfRTbNXTLXnjwWB', 'FIytkBCfvefqIr7Ru1TULUTGuXFvqKSQ3gIfrOJpR8pZNMgSt5')
    auth.set_access_token('1314925517158531072-NktbC7Mv4y5bCYwgDzQePSbkXrA7Tf', 'egyupXKBo7feIxiyCTB1nKYX23CkbsTiBdMA39yMRzMQ9')

    api = tweepy.API(auth)
    user = api.me()
    print(user.name)
    print(user.screen_name)
    print(user.followers_count)
    diff_user = api.get_user('AndreiNeagoie')
    print(diff_user.name)
    print(diff_user.followers_count)
    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)

    def limit_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)
        except StopIteration:
            return

    for follower in limit_handler(tweepy.Cursor(api.user_timeline).items()):
        print(follower)

    # for follower in limit_handler(tweepy.Cursor(api.user_timeline).items()):
    #     if follower.followers_count > 100:
    #         follower.follow()
        


