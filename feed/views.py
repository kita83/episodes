import requests
from django.shortcuts import render


def index(request):
    """
    トレンド一覧画面
    :param request:
    :return: feeds:
    """

    # iTunesストアからPodcastランキング情報を取得
    url = 'https://itunes.apple.com/jp/rss/topaudiopodcasts/genre=1480/json'
    res = requests.get(url).json()

    context = {
        'feeds': res['feed']['entry']
    }

    return render(request, 'feed/index.html', context)
