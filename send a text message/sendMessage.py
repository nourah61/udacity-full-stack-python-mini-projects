from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa1ea2aa10eb4de0aeedf98b93e97b372"
# Your Auth Token from twilio.com/console
auth_token  = "5f98184a57304ef65e57826c0e480fd2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+966590005709",
    from_="+17122276846", 
    body="Hello from Python!")

print(message.sid)
