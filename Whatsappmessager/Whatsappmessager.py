from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
                                body=input("Message: "),
                                from_='whatsapp:+14155238886',
                                to='TO'
                            )
print("Message Sent")