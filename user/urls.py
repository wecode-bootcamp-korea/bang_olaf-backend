from django.urls import path

from user.views import SignView, LoginView

urlpatterns = [
    path('', SignView.as_view()),
    path('/login', LoginView.as_view())
]