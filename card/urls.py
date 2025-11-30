from django.urls import path
from .views.card_views import StartCardApplicationView, SubmitAccountNumberView
from .views.debit_views import CheckBalanceAndDebitView

urlpatterns = [
    path("start/", StartCardApplicationView.as_view()),
    path("<int:pk>/submit-account/", SubmitAccountNumberView.as_view()),
    path("<int:pk>/debit/", CheckBalanceAndDebitView.as_view()),
]
