from django.urls import path
from app_blog import views
from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('articles', ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
    path('articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
]