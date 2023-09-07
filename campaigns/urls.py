from django.urls import path
from . import views

urlpatterns = [
    # endpoint to send campaigns
    path('send-campaigns/', views.SendCampaignsView.as_view(), name='send_campaigns'),
    # endpoint to unsubscribe a subscriber
    path('unsubscribe/<str:encrypted_email>/', views.UnsubscibeView.as_view(), name='unsubscribe'),
]
