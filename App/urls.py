from django.urls import path
from App.Api.article import article, ArticleUpdateDelete
from App.Api.register import register
from App.Api.auth import authis
from App.Api.banner import BannerView, BannerUpdateDelete
from App.Api.service import ServiceView
from App.Api.janji import Janji, JanjiUpdateDelete
from App.Api.review import ReviewView, ReviewUpdateDelete
from App.Api.service import ServiceUpdateDelete, ServiceView

urlpatterns = [
    path('article/', article.as_view()),
    path('articleupdate/<str:slug>/', ArticleUpdateDelete.as_view()),
    path('banner/', BannerView.as_view()),
    path('bannerupdate/<str:name>/', BannerUpdateDelete.as_view()),
    path('service/', ServiceView.as_view()),
    path('serviceupdate/<str:status>/', ServiceUpdateDelete.as_view()),
    path('janji/', Janji.as_view()),
    path('janjiupdate/<int:id>/', JanjiUpdateDelete.as_view()),
    path('review/', ReviewView.as_view()),
    path('reviewupdate/<str:slug>/', ReviewUpdateDelete.as_view()),
    path('datauser/', register.as_view()),
    path('auth/', authis.as_view()),

]
