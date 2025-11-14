from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('post/',views.post,name='post'),
    path('post/<int:post_id>/',views.postid,name='post_detail'),
    path('personalblog/',views.render_index_template,name='indextemplate'),
    path('personalblog/<int:post_id>/',views.post_detail,name='post_detail_template'),
    path('personalblog/about/',views.render_about_template,name='abouttemplate'),
    path('author/<str:name>/', views.post_by_author, name='post_by_author'),
    path('myblog/', views.user_blog, name='user_blog'),
]

