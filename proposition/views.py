from django.shortcuts import render
from .models import Proposition, Upvote, Downvote
# Create your views here.
from rest_framework import viewsets
from .serializers import *


class PropViewset(viewsets.ModelViewSet):
    serializer_class = PropSerializer
    queryset = Proposition.objects.all()


class UpvoteViewset(viewsets.ModelViewSet):
    serializer_class = UpvoteSerializer
    queryset = Upvote.objects.all()


class DownvoteViewset(viewsets.ModelViewSet):
    serializer_class = DownvoteSerializer
    queryset = Downvote.objects.all()


def props(request):
    print(Proposition.objects.all())
    data = {
        "props": Proposition.objects.all()
    }
    return render(request, "votes.html", data)
