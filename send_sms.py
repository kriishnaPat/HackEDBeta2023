import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def message(number, body):
    message = client.messages.create(
    from_="+14149821518", body=body, to=number
    )

    print(message.sid)
