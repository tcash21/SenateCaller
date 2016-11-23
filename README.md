# SenateCaller

* Sign up for a Twilio account: https://www.twilio.com/try-twilio. You will need to pay if you want to remove the pre-recorded message at the beginning of the call. It's very cheap, about 1 cent per call.
* Configure your local environment. I used Python 2.7 on OS X: https://www.twilio.com/docs/quickstart/python/devenvironment
* Once you register for a Twilio account, you'll have your own Twilio phone #, account SID and token, which you should replace in the `SenateCaller/make_calls.py` file.
* Create your message using TwiML! It's a simple XML file. https://www.twilio.com/console/dev-tools/twiml-bins. 
* Once everything is configured, navigate to the SenateCaller/ directory and run `python make_calls.py`
* You can also record an mp3 of your voice and play that instead of an automated message. https://www.twilio.com/docs/quickstart/python/twiml/play-mp3-for-caller

I'm happy to help anyone set this up on their own machine if you need additional help. Please help your non-technical friends if you can as well!

# LEGAL
Use at your own risk. You should identify yourself on the call and provide a callback number for them to opt-out. Also be careful with the volume of the calls made.
