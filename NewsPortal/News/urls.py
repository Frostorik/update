from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostSearch, PostEdit, PostDelete, CategoryList, subscribe

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('search/', PostSearch.as_view()),
    path("<int:pk>/edit/", PostEdit.as_view()),
    path("<int:pk>/delete/", PostDelete.as_view()),
    path("categories/<int:pk>", CategoryList.as_view(), name="category_news"),
    path("categories/<int:pk>/subscribe", subscribe, name="subscribe")
]
