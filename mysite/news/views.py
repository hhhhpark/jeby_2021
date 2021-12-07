from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewsSearchForm


@login_required(login_url="common:login")
def index(request):
    """
    뉴스 검색 화면으로 리다이렉트한다.
    """
    return redirect("news:news_search")


@login_required(login_url="common:login")
def news_search(request):
    """
    뉴스 검색 화면을 반환한다.
    """

    if request.method == "GET":
        if len(request.GET):
            form = NewsSearchForm(request.GET)

            if form.is_valid():
                pass
        # 뉴스를 검색하지 않고 검색 페이지를 오픈할 때는
        # form 유효성 체크를 하지 않도록 한다.
        else:
            form = NewsSearchForm()

    return render(request, "news/news_search.html", {"form": form},)
