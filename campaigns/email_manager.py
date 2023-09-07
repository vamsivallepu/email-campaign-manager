import django_config
from django.core import mail
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Campaign, Subscriber

from Crypto.Cipher import AES

import multiprocessing

import os
from dotenv import load_dotenv

# load the stored environment variables
load_dotenv()


def send_campaign(campaign, recipient):

    # If we pass the direct email address in unsubscribe_url, it will be misused by others to unsubscribe
    # So we encrypt the email address and pass it in the unsubscribe_url
    key = str.encode(os.getenv("KEY"), 'utf-8')
    iv = str.encode(os.getenv("IV"), 'utf-8')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_email = iv + cipher.encrypt(recipient.encode('utf-8'))
    unsubscribe_url = f"http://127.0.0.1:8000/unsubscribe/{encrypted_email.hex()}/"

    # Render the email content from the template
    email_content = render_to_string(
        'campaign_email.html', {'campaign': campaign, 'unsubscribe_url': unsubscribe_url})

    subject = campaign.subject
    from_email = "baladurgeshv@gmail.com"

    message = mail.EmailMultiAlternatives(
        subject, "", from_email=from_email, to=[recipient])
    message.attach_alternative(email_content, 'text/html')

    try:
        message.send()
        print(f"Email sent for campaign: {campaign.subject} to {recipient}")
    except Exception as e:
        print(f"Error sending email for campaign: {campaign.subject} to {recipient}. Error: {str(e)}")


def send_daily_campaigns():

    # Get all the campaigns with published date as today
    campaigns = Campaign.objects.filter(published_date=timezone.now().date())
    if not campaigns:
        return "No campaigns to send today"

    # Get all the active subscribers
    subscribers = Subscriber.objects.filter(is_active=True)
    if not subscribers:
        return "No active subscribers"

    # Create a pool of worker processes
    # Can adjust the number of processes as needed
    pool = multiprocessing.Pool(processes=2)

    # Send the campaign to each subscriber
    for campaign in campaigns:
        for subscriber in subscribers:
            pool.apply_async(send_campaign, args=(campaign, subscriber.email))
    return (len(campaigns), len(subscribers))

    pool.close()
    pool.join()
