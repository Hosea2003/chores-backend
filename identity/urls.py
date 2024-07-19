from django.urls import path
from dj_rest_auth.views import LoginView, LogoutView
from .views import UserDetailsView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("details/", UserDetailsView.as_view(), name="user-details"),
]
