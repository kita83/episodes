import requests
from django.shortcuts import render, redirect
from allauth.account import views


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


class LoginView(views.LoginView):
    template_name = 'feed/login.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(LoginView, self).dispatch(request, *args, **kwargs)
        return response

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)


login = LoginView.as_view()


class LogoutView(views.LogoutView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.logout()
        return redirect('/')


logout = LogoutView.as_view()


class SignupView(views.SignupView):
    template_name = 'feed/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context


signup = SignupView.as_view()
