from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from web.forms import NewTopicForm
from web.models import Board, Post, Topic, User

# Create your views here.

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

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})