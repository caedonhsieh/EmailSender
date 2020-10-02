import smtplib
import getmx

DOMAIN = "google.com"
HOST = getmx.get_host(DOMAIN)
SENDER = "test@test.com"
SENDNAME = "test tester"
RECIPIENT = "ehhsiehfamily@gmail.com"
SUBJECT = "subject line"
MESSAGE = "this is a test message\nit is cool"

fromLine = "From: {} <{}>\r\n".format(SENDNAME, SENDER)
toLine = "To: <{}>\r\n".format(RECIPIENT)
subjectLine = "Subject: {}\r\n".format(SUBJECT)

msg = fromLine + toLine + subjectLine + MESSAGE

try:
    server = smtplib.SMTP(host=HOST)
    server.set_debuglevel(1)
    server.sendmail(SENDER, RECIPIENT, msg)
    server.quit()
except smtplib.SMTPConnectError:
    print('Error: Could not connect to server.')
except smtplib.SMTPRecipientsRefused:
    print('Error: Recipient refused.')
except smtplib.SMTPDataError:
    print('Error: Server refused data. Possible unauthenticated email.')
