fimport csv
import time

# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

#nums = []

# Senator phone numbers
#with open('senator_phones.csv', 'rb') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        nums.append(row)

# Get these credentials from http://twilio.com/user/account
account_sid = "SID"
auth_token = "token"
client = TwilioRestClient(account_sid, auth_token)

#for number in nums:
# Make the call
call = client.calls.create(to='some_test_#',from_="your_twilio_number", url="https://handler.twilio.com/twiml/EH146e298181dcc2666f3729fc61e497b4")
print(call.sid)
#    time.sleep(3)
