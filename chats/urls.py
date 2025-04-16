from django.urls import path, include

from chats import views

api_urlpatterns = [
    path('chats/', views.ChatListView.as_view(), name='chats-list'),
    path('chats/<uuid:chat_id>/messages/', views.ChatMessagesView.as_view(), name='chat-messages'),
    path('chats/<uuid:chat_id>/messages/<int:pk>/', views.MessageDetailView.as_view(), name='message-detail'),
    path('chats/<uuid:chat_id>/sendMessage/', views.SendMessageView.as_view(), name='message-send'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(api_urlpatterns))
]
