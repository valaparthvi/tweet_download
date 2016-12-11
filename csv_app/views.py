from django.shortcuts import render
from twito_csv.settings import CONSUMER_KEY, CONSUMER_SECRET
import tweepy
from .forms import tweetForm
from .dfile import file_convert
from celery.decorators import task


@task
def index(request):
    if request.method == 'POST':
        form = tweetForm(request.POST)
        if form.is_valid():
            screen_name = form.cleaned_data['user_name']
            file_type = form.cleaned_data["file_type"]
            form = tweetForm()
            consumer_key = CONSUMER_KEY
            consumer_secret = CONSUMER_SECRET
            access_token = "765174214777249792-SUPa58z6NvnxbACwexOTtYPfDVxYcSz"
            access_secret_token = "mOWQiCjQzVXuFd0gmc1hkQh0iBGB0Biu37VvfV5eGSrPz"
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_secret_token)
            tweepy_user = tweepy.API(auth)

            print(file_type)
            print(screen_name)

            alltweets = []
            try:
                new_tweets = tweepy_user.user_timeline(
                    screen_name=screen_name, count=200)
            except tweepy.TweepError:
                return render(request, 'csv_app/no_user.html', {'form': form})
            # except tweepy.RateLimitError:
            #     pass

            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1

            while len(new_tweets) > 0:
                print("getting tweets before " + str(oldest))
                new_tweets = tweepy_user.user_timeline(
                    screen_name=screen_name, count=200, max_id=oldest)

                alltweets.extend(new_tweets)
                oldest = alltweets[-1].id - 1
                print("..." + str(len(alltweets)) +
                      ' tweets downloaded so far')

            f = file_convert(file_type, screen_name, alltweets)
            print("Back in views")
            return f
    else:
        form = tweetForm()

    return render(request, 'csv_app/base.html', {'form': form})


# from django.shortcuts import render, HttpResponse

# # import tablib
# import tweepy
# # import requests
# from .forms import tweetForm
# from .dfile import file_convert
# # Create your views here.


# def index(request):
#     if request.method == 'POST':
#         form = tweetForm(request.POST)
#         if form.is_valid():
#             screen_name = form.cleaned_data['user_name']
#             file_type = form.cleaned_data["file_type"]
#             fil = get_tweets(screen_name, file_type)
#             print("Back in index")
#             return fil
#     else:
#         form = tweetForm()
#     return render(request, 'csv_app/base.html', {'form': form})


# def get_tweets(screen_name, file_type):
#     consumer_key = "JCxBbbGjvC5qIneTUJUMUQSzY"
#     consumer_secret = "vYDlU2JDXtSe5AtqHdZ1Pc2tf20ZGxU2AQvE1WD5ODIwGYrB01"
#     access_token = "765174214777249792-SUPa58z6NvnxbACwexOTtYPfDVxYcSz"
#     access_secret_token = "mOWQiCjQzVXuFd0gmc1hkQh0iBGB0Biu37VvfV5eGSrPz"
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_secret_token)
#     tweepy_user = tweepy.API(auth)
#     print(file_type)
#     print(screen_name)

#     # form = tweetForm()

#     # screen_name = form.cleaned_data['user_name']
#     # file_type = form.cleaned_data["file_type"]

#     alltweets = []

#     new_tweets = tweepy_user.user_timeline(
#         screen_name=screen_name, count=200)
#     alltweets.extend(new_tweets)
#     oldest = alltweets[-1].id - 1

#     while len(new_tweets) > 0:
#         print ("getting tweets before " + str(oldest))
#         new_tweets = tweepy_user.user_timeline(
#             screen_name=screen_name, count=200, max_id=oldest)

#         alltweets.extend(new_tweets)
#         oldest = alltweets[-1].id - 1
#         print ("..." + str(len(alltweets)) + ' tweets downloaded so far')

#     f = file_convert(file_type, screen_name, alltweets)
#     print("Back in views")
#     return f
