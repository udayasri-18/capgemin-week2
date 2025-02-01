class Notification:
    def send(self):
        print("Notification is sent")
class Emailnotification(Notification):
    def send(self):
        print("Email Notification is sent")
class SMSnotification(Notification):
    def send(self):
        print("SMS Notification is sent")
sms=SMSnotification()
sms.send()

email=Emailnotification()
email.send()