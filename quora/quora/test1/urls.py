from django.urls import path ,include
from . import views


app_name = 'test1'

urlpatterns = [
    path('home/',views.ques_list,name = 'ques_list'),
    path('ques/<int:id>/',views.ques_detail,name='ques_detail'),
    path('login/',views.user_login,name = 'user_login'),
    path('logout/',views.user_logout ,name = 'user_logout'),
    path('register/',views.register,name = 'register'),
    path('ask_question/',views.ask_question,name = 'ask_question'),
    path('update_ques/<int:id>/',views.update_ques ,name = 'update_ques'),
    path('delete_ques/<int:id>/', views.delete_ques, name='delete_ques'),
    path('likes/',views.ques_likes,name ='ques_likes'),
    path('comment_reply/<int:id>',views.comment_reply,name = 'comment_reply'),
    path('profilepage/<str:username>/',views.profilepage,name='profilepage'),
    path('delete_comment/<int:id>',views.delete_comment,name='delete_comment'),
    path('delete_reply/<int:id>', views.delete_reply, name='delete_reply'),
]