# notifications/urls.py

from django.urls import path
from .views import notification_request_view, success_view

urlpatterns = [
    path('request-notification/', notification_request_view, name='request_notification'),
    path('success/', success_view, name='success_url'),
]
