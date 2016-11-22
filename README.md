# SenateCaller

* Sign up for a Twilio account: https://www.twilio.com/try-twilio. You will need to pay if you want to remove the pre-recorded message at the beginning of the call. It's very cheap, about 1 cent per call.
* Configure your local environment. I used Python on OS X: https://www.twilio.com/docs/quickstart/python/devenvironment
* You'll have your own Twilio phone # and account SID and Token, which you should replace in the SenateCaller/make_calls.py file.
* Create your message using TwiML! https://www.twilio.com/console/dev-tools/twiml-bins. It's just a simple XML file. 
* Once everything is configured just navigate to the SenateCaller directory and run `python make_calls.py`

I'm happy to help anyone set this up on their own machine if you need additional help. Please help your non-technical friends if you can as well!
