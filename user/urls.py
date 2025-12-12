from django.urls import path
from .views import registration, user_login, user_logout

urlpatterns = [
    path('reg-form/', registration, name='registr'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout' ), 
]
