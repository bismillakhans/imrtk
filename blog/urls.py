from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('articles/', views.BlogListView.as_view(), name='articles'),
    path('<int:year>/<int:month>/<slug:slug>', views.post_view, name='post'),
    path('search/', views.post_search, name='search'),
    path('about/', views.about, name='about'),
    path('regstudent/', views.RegisterStudent.as_view(), name='regstudent'),
    path('reg_success/', views.RegSuccess.as_view(), name='reg_successview'),
    path('postreg/', views.BlogRegView.as_view(), name='postreg'),
    path('fileview/', views.DocumentListView.as_view(), name='fileview'),
    path('post_reg_success/', views.PostRegSuccess.as_view(), name='post_reg_success'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('', views.index, name='index'),
    path('links/',views.LinkListView.as_view(),name='links'),
    path('works/',views.WorkListView.as_view(),name='works'),
    path('gallery/',views.GalleryListView.as_view(),name='gallery'),



]