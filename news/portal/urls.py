from django.urls import path
from .views import PostList, PostDetail, PostDelete, PostUpdate, PostCreate, SearchPosts

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),

   path('search/', SearchPosts.as_view(), name='search_posts'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),

]