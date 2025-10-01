from django.urls import path
from . views import *

urlpatterns = [
    path("step1/", Step1View.as_view(), name="step1"),
    path("step2/<str:id>/", Step2View.as_view(), name="step2"),
    path("step3/<str:id>/", Step3View.as_view(), name="step3"),
    path("step4/<str:id>/", Step4View.as_view(), name="step4"),
    path("review/<str:id>/", ReviewView.as_view(), name="review"),
    path("submit/<str:id>/", SubmissionView.as_view(), name="submit"),
]