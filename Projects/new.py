from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

# Lookup phone number
phone_number = '+1234567890'
number_info = client.lookups.phone_numbers(phone_number).fetch(type=['caller-name'])

print(number_info.caller_name)
