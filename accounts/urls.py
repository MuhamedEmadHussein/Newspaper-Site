from django.urls import path
from .views import SignupView

urlpatterns = [
      path('signup/',view=SignupView.as_view(),name="signup"),
]