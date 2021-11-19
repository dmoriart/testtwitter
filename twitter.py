def main():
    # connect to twitter
    api = connect_to_twitter()

    # retrieve tweets
    tweets = get_tweets(api)

    # run sentiment analysis on tweets
    sentiment_analysis(tweets)


def connect_to_twitter():
    """
    connect to twitter using tweepy
    """
    # authenticate
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # connect to twitter
    api = tweepy.API(auth)

    return api


def get_tweets(api):
    """
    retrieve tweets addressed to @talktoboi
    """
    # get tweets
    tweets = api.search(q='@talktoboi', count=100)

    return tweets


def sentiment_analysis(tweets):
    """
    run sentiment analysis on tweets
    """
    # run sentiment analysis on tweets
    for tweet in tweets:
        # get text
        text = tweet.text

        # get sentiment
        sentiment = TextBlob(text).sentiment.polarity

        # print results
        print('\nTweet: {}'.format(text))
        print('Sentiment: {}'.format(sentiment))


if __name__ == '__main__':
    main()
