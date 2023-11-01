from django.urls import path
from .views import SinUpView

urlpatterns = [
    path('signup/', SinUpView.as_view(), name='signup'),
]
