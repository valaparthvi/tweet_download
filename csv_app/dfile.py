import tablib
from django.shortcuts import HttpResponse


def file_convert(file_type, screen_name, alltweets):

    tweet_file = tablib.Dataset()
    tweet_file.headers = ['text', 'id', 'created_at']
    print("here forming files")
    for tweet in alltweets:
        tweet_file.append([tweet.text, tweet.id_str, tweet.created_at])

    if file_type == 'CSV':
        response = HttpResponse(content=tweet_file.csv,
                                content_type='text/csv')
        response[
            'Content-Disposition'] = 'attachment; filename="%s_tweets.csv"' % screen_name
        # response.write(tweet_file.get_csv())
        return response

    else:
        response = HttpResponse(
            content=tweet_file.xls, content_type='application/vnd.ms-excel')
        response[
            'Content-Disposition'] = 'attachment; filename="% s_tweets.xls"' % screen_name
        return response
