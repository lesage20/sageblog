from rest_framework import viewsets
from .serializers import *
from .models import  *
# API views

class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerialzer
    queryset = Like.objects.all()
    
    
class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerialzer
    queryset = Comment.objects.all()
    
    
class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerialzer
    queryset = Article.objects.all()
    
    
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerialzer
    queryset = Category.objects.all()

   

class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerialzer
    queryset = Tag.objects.all()
    
    
class AuteurView(viewsets.ModelViewSet):
    serializer_class = AuteurSerialzer
    queryset = Auteur.objects.all()

    
        

