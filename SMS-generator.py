import os

print("Twilio SMS Generator")
print("\r\n Send SMS to (include countrycode):  ")
smsTo = str(input())

print("\r\n Send text:  ")
smsContents = str(input())

print("\r\n Sender:  ")
smsSender = str(input())

print("""
-----------------------
SMS to:  %s
SMS from: %s
SMS Contents:
%s

""" % (smsTo,smsSender,smsContents))

CurlCommand = """curl 'https://api.twilio.com/2010-04-01/Accounts/AC***************************/Messages.json' -X POST \
--data-urlencode 'To=+47%s' \
--data-urlencode 'Body=%s' \
--data-urlencode 'From=%s' \
--data-urlencode 'MessagingServiceSid=********************' \
-u *********************:*************************************""" % (smsTo,smsContents,smsSender)

print("\r\n%s \r\n\r\n Send? (y):  " % CurlCommand)

doSend = input()
if doSend == 'y':
    os.system(CurlCommand)
else:
    print("\r\n Quitting  ")
    exit()
