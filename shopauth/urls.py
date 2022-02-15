from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import shopauth.views as shopauth

app_name = 'shopauth'

urlpatterns = [
    path('user/create/',
         shopauth.ShopUserCreateView.as_view(),
         name='user_create'),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
    # path('logout/', shopauth, name='logout'),

]