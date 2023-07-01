from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('api/online-users/', onlineUsers),
    path('api/login/', LoginAPI.as_view()),
    path('api/logout/', LogoutAPI.as_view()),
    path('api/register/', RegisterAPI.as_view()),
    path('api/chat/start/<int:pk>', ChatStartAPI.as_view()),
    path('api/suggested-friends/<int:user_id>', suggestFriend)

]