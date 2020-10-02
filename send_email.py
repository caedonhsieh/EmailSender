import smtp

domain = input("Specify a domain or leave empty and press enter: ")
if not domain:
    domain = "google.com"
sender = input("From what email address should the email be sent? ")
while not sender:
    sender = input("Please specify the sender's email address: ")
send_name = input("What should the sender's name be? ")
recipient = input("To what email address should the email be sent? ")
while not recipient:
    recipient = input("Please specify the recipient's email address: ")
subject = input("What should the subject line be? ")
content = []
print("Type the email message body below. End the message with a single period on a line.")
while True:
    line = input()
    if line == ".":
        break
    content.append(line)

message = "\r\n".join(content)
smtp.send(domain, sender, send_name, recipient, subject, message)
