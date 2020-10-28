from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from messageboard.accounts.views import UserSignupView

urlpatterns = [
    url(r"", include("messageboard.urls")),
    path("signup/", view=UserSignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"
    ),
]
