from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post
from .forms import CommentForm, PostForm
from django.http import HttpResponseRedirect


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "upvoted": upvoted,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        upvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # msg.add_message(request, msg.SUCCESS, f'Thank you {request.user.username} for commenting')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "upvoted": upvoted,
                "comment_form": CommentForm()
            },
        )


class CreatePost(View):
    model = Post
    template_name = 'create_post.html'

    def get(self, request, *args, **kwargs):
        context = {'post_form': PostForm()}
        return render(request, 'create_post.html', context)

    def post(self, request, *args, **kwargs):
        # queryset = Post.objects
        # print(type(request.POST))
        # print(request)
        # post_form = PostForm(data=request.POST)
        # if post_form.is_valid():
        # post_form = PostForm()
        post = Post()
        post.category = request.POST.get('category', '')
        post.content = request.POST.get('content', '')
        post.excerpt = request.POST.get('excerpt', '')
        post.author = request.user
        # queryset.create(post)

            # msg.add_message(request, msg.SUCCESS, f'Thank you {request.user.username} for commenting')
        # else:
        #     post_form = PostForm()

        return render(
            request,
            "",
            {
                "post": post,
                # "post_form": PostForm()
            },
        )


class PostUpvote(View):
    def post(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(Post, slug=slug)

        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
