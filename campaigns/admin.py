from django.contrib import admin
from .models import Subscriber, Campaign

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    # items to be displayed in the admin panel
    list_display = ('email', 'first_name', 'is_active')

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    # items to be displayed in the admin panel
    list_display = ('subject', 'published_date')
