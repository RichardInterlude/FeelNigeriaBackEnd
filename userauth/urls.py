from django.urls import path
from . views import *


urlpatterns = [
    path('register/',RegistrationView.as_view()),
    path('verify/',VerifyRegistrationView.as_view(),name='verify'),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    # path('dashboard/',DashboardView.as_view())
]