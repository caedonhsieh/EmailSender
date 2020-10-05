import smtplib
import getmx


def send(DOMAIN, SENDER, SENDNAME, RECIPIENT, SUBJECT, MESSAGE):
    HOST = getmx.get_host(DOMAIN)

    from_line = "From: {} <{}>\r\n".format(SENDNAME, SENDER)
    to_line = "To: <{}>\r\n".format(RECIPIENT)
    subject_line = "Subject: {}\r\n".format(SUBJECT)

    msg = from_line + to_line + subject_line + MESSAGE

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
