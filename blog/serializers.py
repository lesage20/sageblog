from rest_framework import serializers
from . import models

class LikeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'
    
class LikeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'

class CommentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

class ArticleSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class TagSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'

class AuteurSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Auteur
        fields = '__all__'


