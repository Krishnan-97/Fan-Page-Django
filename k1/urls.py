from django.conf.urls import url
from django.urls import path
from k1 import views
from k1.views import signup, login1, logout_view, comment_table, add_comment1, todoedit, tododelete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',signup,name='signup'),
    path("login/",login1,name='login'),
    path("logout/",logout_view,name='logout'),
    path("comment/",comment_table,name='comment'),
    path("addcomment/",add_comment1,name='addcomment'),
    path("editcomment/<int:pk>/" ,todoedit, name="todoedit"),
    path("comment/<int:pk>/" ,tododelete, name="tododelete"),

]