from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('register_user/',views.register_user,name='register_user'),
]
