from django.urls import path, include
from .import views
from .apiviews import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('like',LikeView)
router.register('comment',CommentView)
router.register('article',ArticleView)
router.register('category',CategoryView)
router.register('tag',TagView)
router.register('auteur',AuteurView)


urlpatterns = [
    path('single/<int:pk>', views.single, name="single"),
    # path('like', views.like_view, name="like-article"),    
    path('', views.tech, name="tech"),
    path('api/', include('blog.apiurls')),
    
    path('search', views.search, name="search"),
    
]