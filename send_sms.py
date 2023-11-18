from twilio.rest import Client

account_sid = 'ACfd47008f92aedbb64a6624337b6bea72'
auth_token = 'e624663675ecb7ee287be925c1d5645d'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16562163819',
  body='hello',
  to='+17809048091'
)

print(message.sid)