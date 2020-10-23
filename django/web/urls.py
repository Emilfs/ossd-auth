import django_cas_ng.views
from django.urls import path

from .views import index, login, logout, oauth2_logout, profile, logout_success


app_name = "web"

urlpatterns = [
    path('login/', login, name="login"),
    path('login/cas/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('logout/cas/', django_cas_ng.views.LogoutView.as_view(),
         name='cas_ng_logout'),
    path('logout/', logout, name="logout"),
    path('logout/ouath2/', oauth2_logout, name='oauth2_logout'),
    path("profile/", profile, name='profile'),
    path('/logout_success', logout_success, name="logout_success"),
    path("", index),
]
