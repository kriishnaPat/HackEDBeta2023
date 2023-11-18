from twilio.rest import Client

account_sid = 'ACa20945303efc874af274f6e9705a84a7'
auth_token = '2359e38d1b0d6a80e4ad9468c5cc82cf'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14149821518',
  body='how much wood would a wood chuck chuck if a wood chuck if a wood chuck chuck?',
  to='+17804059975'
)

print(message.sid)
