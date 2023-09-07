from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from .email_manager import send_daily_campaigns
from .models import Subscriber
from Crypto.Cipher import AES
import binascii

import os
from dotenv import load_dotenv

# load the stored environment variables
load_dotenv()


# View to send campaigns
class SendCampaignsView(View):
    def get(self, request):
        num_campaigns_sent, num_subscribers = send_daily_campaigns()
        return HttpResponse(f"Sent {num_campaigns_sent} campaigns to {num_subscribers} subscribers")

# View to unsubscribe a subscriber
class UnsubscibeView(View):
    def get(self, request, encrypted_email):
        try:
            # Decrypt the email address
            key = str.encode(os.getenv("KEY"), 'utf-8')
            iv = str.encode(os.getenv("IV"), 'utf-8')
            cipher = AES.new(key, AES.MODE_CFB, iv)
            email = cipher.decrypt(binascii.unhexlify(encrypted_email))[
                len(iv):].decode('utf-8')

            # find the subscriber and unsubscribe them
            try:
                subscriber = Subscriber.objects.get(email=email)
                subscriber.is_active = False
                subscriber.save()
                return HttpResponse("You have been unsubscribed successfully")

            # If the subscriber does not exist
            except Subscriber.DoesNotExist:
                return HttpResponseNotFound("Subscriber does not exist")

        # If the unsubscribe link is invalid
        except Exception as e:
            return HttpResponseBadRequest("Invalid unsubscribe link")
