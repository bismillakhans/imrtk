from django.shortcuts import render, get_object_or_404
from ckeditor.widgets import CKEditorWidget
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import CommentForm, ReplyForm
from .models import Post, Comment, Reply,Student,Document,Member,Link,Work,Gallery


class BlogListView(ListView):
    model = Post
    template_name = "blog/articles.html"
    paginate_by = 5
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=True)
    ordering = ['-post_update',]

class MemberListView(ListView):
    model = Member
    template_name = "blog/members.html"
    context_object_name = 'members'
    queryset = Member.objects.filter(status=True)
    ordering = ['rank',]

class DocumentListView(ListView):
    model = Document
    template_name = "blog/document.html"
    context_object_name = 'docs'
    queryset = Document.objects.filter(status=True)

class GalleryListView(ListView):
    model = Gallery
    template_name = "blog/gallery.html"
    context_object_name = 'galleries'
    queryset = Gallery.objects.filter(status=True)
    ordering = ['-g_date',]

class LinkListView(ListView):
    model = Link
    template_name = "blog/links.html"
    context_object_name = 'links'
    queryset = Link.objects.filter(status=True)

class WorkListView(ListView):
    model = Work
    template_name = "blog/works.html"
    context_object_name = 'works'
    queryset = Work.objects.filter(status=True)
    

class BlogRegView(CreateView):
    model = Post
    fields = ['title','tags','short_desc','body']
    success_url = '/post_reg_success'

class RegisterStudent(CreateView):
    model = Student
    fields = ['name', 'district', 'phone','email', 'organisation', 'address']
    success_url = '/reg_success'

def about(request):
    template = "blog/about.html"
    return render(request,template)

def index(request):
    template = "blog/index.html"
    return render(request,template)



class RegSuccess(TemplateView):
    template_name = "blog/reg_success.html"


class PostRegSuccess(TemplateView):
    template_name = "blog/post_reg_success.html"
    
def post_search(request):
    template = "blog/search.html"
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    context = {'posts': results, 'query': query}

    return render(request, template, context)


def post_view(request, year, month, slug):
    template = 'blog/post.html'
    post = get_object_or_404(Post, post_date__year=year,
                             post_date__month=month, slug=slug)
    comments = post.comment.all()
    comment_form, reply_form = CommentForm(), ReplyForm()

    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            data = comment.cleaned_data
            comment_post = data['comment']
            author_comment = data['author_comment']

            new_comment = Comment(fk_post=post,
                                  comment=comment_post, author=author_comment)
            new_comment.save()

    if request.method == 'POST':
        reply = ReplyForm(request.POST)
        if reply.is_valid():
            data = reply.cleaned_data

            fk_comment = data['fk_comment']
            reply_post = data['reply']
            author_reply = data['author_reply']
            comment_obj = Comment.objects.get(pk=fk_comment)

            new_reply = Reply(fk_comment=comment_obj,
                              reply=reply_post, author=author_reply)
            new_reply.save()

    context = {'post': post, 'comments': comments,
               'comment_form': comment_form, 'reply_form': reply_form}

    return render(request, template, context)
