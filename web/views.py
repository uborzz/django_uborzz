from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from web.models import Board
from django.http import Http404

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})

def board_topics(request, pk):
    # try:
    #     #     board = Board.objects.get(pk=pk)
    #     # except Board.DoesNotExist:
    #     #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def user_profile(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})