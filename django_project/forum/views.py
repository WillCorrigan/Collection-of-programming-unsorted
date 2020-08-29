from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Board, Comment, Topic
from django.db.models import Count


def home(request):

    context = {
        'boards': Board.objects.all()
    }
    return render(request, 'forum/home.html', context)


class BoardListView(ListView):
    model = Board
    template_name = 'forum/testforum.html'
    context_object_name = 'boards'
    ordering = ['-date_posted']
    paginate_by = 5


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_view.html'
    context_object_name = 'topics'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-date_posted').annotate(comment=Count('comments') -1)
        return queryset


class ThreadListView(ListView):
    model = Comment
    template_name = 'forum/thread_view.html'
    context_object_name = 'comments'
    ordering = ['created_at']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, pk=self.kwargs.get('pk2'))
        queryset = self.topic.comments.order_by('created_at').annotate(comment=Count('message') -1)
        return queryset



class CommentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Comment
    fields = ['message']
    permission_required = 'blog.create_new_blog_post'
    raise_exception = True





    def handle_no_permission(self):
        # add custom message
        messages.warning(self.request, 'You have no permission to view this forum!')
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())



    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.topic_id = self.kwargs.get('pk2')

        return super().form_valid(form)