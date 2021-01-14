from django.urls import path

from user.views import SignView, LoginView

urlpatterns = [
    path('/signup', SignView.as_view()),
    path('/signin', LoginView.as_view())
]