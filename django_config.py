import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_campaign_manager.settings")

# Initialize Django
django.setup()
