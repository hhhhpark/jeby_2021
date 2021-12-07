from django.contrib import admin
from django.urls import path, include
from news import views as views_news

urlpatterns = [
    path("", views_news.index),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("news/", include("news.urls")),
]
