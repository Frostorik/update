from django.urls import path

from .views import PostList, PostDetail, PostCreate, PostSearch, PostEdit, PostDelete, CategoryList, subscribe
from .views import IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostList.as_view())),
    path('<int:pk>', cache_page(300)(PostDetail.as_view())),
    path('create/', cache_page(300)(PostCreate.as_view()), name='news_create'),
    path('search/', cache_page(300)(PostSearch.as_view())),
    path("<int:pk>/edit/", cache_page(300)(PostEdit.as_view())),
    path("<int:pk>/delete/", cache_page(300)(PostDelete.as_view())),
    path("categories/<int:pk>", cache_page(300)(CategoryList.as_view()), name="category_news"),
    path("categories/<int:pk>/subscribe", subscribe, name="subscribe"),
    path('', cache_page(60)(IndexView.as_view())),
]
