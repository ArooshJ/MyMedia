
from django.urls import path
from . import views
from . views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getPosts,name="getposts"),
    path('comments/',views.getComments,name="getComments" ),
    path('post/',views.newPost,name="getComments" ),
    path('deletepost/<int:pk>/', views.delete_post, name='delete_post'),
    path('<int:postpk>/likepost/<int:accountpk>/', views.likePost, name='like_post'),
    path('comments/<int:compk>/likecom/<int:accountpk>/', views.likeComment, name='like_comment'),
    path('replies/<int:reppk>/likerep/<int:accountpk>/', views.likeReply, name='like_reply'),
    path('replies/',views.getReplies,name="getReplies"),
    path('postreplies/',views.postreply,name="postreply"),
    path('postcomments/',views.postcomment,name="postcomment"),
    path('createuser/',views.createUser,name="createUser" ),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # jwt token auth stuff...
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # jwt stuf.....
]
