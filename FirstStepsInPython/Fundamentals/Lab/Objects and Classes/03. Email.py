class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

line_input = input()
while not line_input == "Stop":
    command = line_input.split(" ")
    send_from = command[0]
    receive_to = command[1]
    content_of_mail = command[2]
    email = Email(send_from, receive_to, content_of_mail)
    emails.append(email)
    line_input = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))

for mail in send_emails:
    emails[mail].send()
for email in emails:
    print(email.get_info())
