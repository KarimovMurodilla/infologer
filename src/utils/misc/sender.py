from mailjet_rest import Client

from config import API_KEY_EMAIL as api_key
from config import API_SECRET as api_secret

from config import (
    SENDER_GMAIL, SENDER_NAME
)


class Email:
    def __init__(self):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def send_mail(self, subject, text_part, to_email):
        mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')

        data = {
        'Messages': [
            {
            "From": {
                "Email": SENDER_GMAIL,
                "Name": SENDER_NAME
            },
            "To": [
                {
                "Email": to_email,
                "Name": to_email
                }
            ],
            "Subject": subject,
            "TextPart": text_part,
            "HTMLPart": text_part,
            "CustomID": "AppGettingStartedTest"
            }
        ]
        }

        result = mailjet.send.create(data=data)
        return result