import tweepy
from datetime import datetime
import pyjokes
import time

if __name__ == '__main__':
    auth = tweepy.OAuthHandler('ANOwYsIT9bCuiuPQ6wlq1DN7U', 'EJ3F4HVF212S1B9qZwl4rsUKgDkkKTlaWdNhQQjijHJmoSdbIL')
    auth.set_access_token('1314925517158531072-43qIo3pbRY7SiyWOqVW6cQzTluTTrG', 'mbNiDAQkLNavtod8CPoqYS0QIAKqr6kF6TppAj4Yrzxrp')

    api = tweepy.API(auth)
    user = api.me()
    def limit_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)
        except StopIteration:
            return
    jokes = pyjokes.get_jokes(category='all')
    # print(datetime.now())

    for item in jokes:
        api.update_status(f'{datetime.now()} - All Python Joke {item} ')




    # print(user.name)
    # print(user.screen_name)
    # print(user.followers_count)
    # diff_user = api.get_user('AndreiNeagoie')
    # print(diff_user.name)
    # print(diff_user.followers_count)
    # public_tweets = api.home_timeline()

    # for tweet in public_tweets:
    #     print(tweet.text)



    # for follower in limit_handler(tweepy.Cursor(api.user_timeline).items()):
    #     print(follower)

    # for follower in limit_handler(tweepy.Cursor(api.user_timeline).items()):
    #     if follower.followers_count > 100:
    #         follower.follow()

    # search_string = 'Nihar'
    # numberOfTweets = 5
    #
    # for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    #     try:
    #         tweet.favorite()
    #         print(f'{tweet.text} ----> has been liked')
    #     except tweepy.TweepError as e:
    #         print(e.reason)
    #     except StopIteration:
    #         break

