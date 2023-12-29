from django.urls import path
from . import views
urlpatterns =[
    path('chat',views.chat_home,name='chathome'),
    path('chatwith<str:username>/<str:id>',views.chat_area,name='chatarea'),
    path('blankchat',views.blankchat,name='blankchat'),
    path('testing',views.testing,name='testing'),
    path('image/chatwith<str:usernamereceiver>/<str:id>/<str:username>/<str:currentuserid>',views.imageupload,name='imageupload'),
    path('file/chatwith<str:usernamereceiver>/<str:id>/<str:username>/<str:currentuserid>',views.fileupload,name='fileupload'),
    path('groupchat',views.groupchat,name='groupchathome'),
    path('chatgroup/<str:uniquegroupid>',views.groupchat_area,name='groupchatarea'),  
    path('search',views.searchpeoplechathome,name='search'),
    path('profileupdate',views.profileupdate,name='profilesetup'),
    path('payment/<int:price>',views.create_payment)]