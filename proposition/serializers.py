from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class DownvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downvote
        fields = "__all__"


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username
    queryset = User.objects.all()

    def to_internal_value(self, data):
        return data


class PropSerializer(serializers.ModelSerializer):
    downvotes = DownvoteSerializer(many=True, read_only=True)
    upvotes = UpvoteSerializer(many=True, read_only=True)
    author = UserField()

    class Meta:
        model = Proposition
        fields = "__all__"

    def create(self, validated_data):
        username = validated_data.pop('author')
        print('create', username)
        user = get_object_or_404(User, username=username)

        return Proposition.objects.create(
            **validated_data, author=user)
