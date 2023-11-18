import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)




message = client.messages.create(
    from_="+14149821518", body="wood chuck chuck", to="+17804059975"
)

print(message.sid)
