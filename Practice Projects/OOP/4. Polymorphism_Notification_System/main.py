# import re

def validate_str(value, attribute):
    if not isinstance(value, str):
        raise TypeError(f"{attribute} should be str")
    elif value.strip() == "":
        raise ValueError(f"{attribute} should no be empty")

class EmailNotification():
    def __init__(self, recipient_email, subject, message):
        self.recipient_email = recipient_email
        self.subject = subject
        self.message = message

    @property
    def recipient_email(self):
        return self.__recipient_email

    @recipient_email.setter
    def recipient_email(self, value):
        validate_str(value, "recipient_email")
        if not "@" in value:
            raise ValueError("recipient email must contain '@'")
        self.__recipient_email = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        validate_str(value, "subject")
        self.__subject = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        validate_str(value, "message")
        self.__message = value

    def send(self):
        return f"Email sent to {self.recipient_email}: {self.subject} - {self.message}"

class SMSNotification():
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        validate_str(value, "phone_number")
        if not (value.isascii() and value.isdigit()):
            raise ValueError("The phone number must contain only digits")
        if len(value) < 7:
            raise ValueError("The phone number must have at least 7 characters.")

        # if not re.fullmatch(r"[0-9]{7,}", value):
        #     raise ValueError("The phone number must have at least 7 characters and must contain only digits.")

        self.__phone_number = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        validate_str(value, "message")
        self.__message = value
    
    def send(self):
        return f"SMS sent to {self.phone_number}: {self.message}"

class PushNotification():
    def __init__(self, device_ID, message):
        self.device_ID = device_ID
        self.message = message

    @property
    def device_ID(self):
        return self.__device_ID

    @device_ID.setter
    def device_ID(self, value):
        validate_str(value, "device_ID")
        self.__device_ID = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        validate_str(value, "message")
        self.__message = value

    def send(self):
        return f"Push notification sent to {self.device_ID}: {self.message}"


def send_all(notifications):
    msg = []
    for notification in notifications:
        msg.append(notification.send())

    return msg

def main():
    # Notification System tests
    email = EmailNotification(
        "anna@example.com",
        "Welcome",
        "Your account has been created."
    )

    assert email.send() == "Email sent to anna@example.com: Welcome - Your account has been created."

    sms = SMSNotification(
        "123456789",
        "Your code is 1234."
    )

    assert sms.send() == "SMS sent to 123456789: Your code is 1234."

    push = PushNotification(
        "device-001",
        "You have a new message."
    )

    assert push.send() == "Push notification sent to device-001: You have a new message."

    notifications = [email, sms, push]

    results = send_all(notifications)

    assert results == [
        "Email sent to anna@example.com: Welcome - Your account has been created.",
        "SMS sent to 123456789: Your code is 1234.",
        "Push notification sent to device-001: You have a new message."
    ]

    try:
        EmailNotification("annaexample.com", "Welcome", "Message")
        assert False
    except ValueError:
        assert True

    try:
        EmailNotification("anna@example.com", "", "Message")
        assert False
    except ValueError:
        assert True

    try:
        EmailNotification("anna@example.com", "Welcome", "")
        assert False
    except ValueError:
        assert True

    try:
        SMSNotification("123abc", "Message")
        assert False
    except ValueError:
        assert True

    try:
        SMSNotification("123", "Message")
        assert False
    except ValueError:
        assert True

    try:
        SMSNotification("123456789", "")
        assert False
    except ValueError:
        assert True

    try:
        PushNotification("", "Message")
        assert False
    except ValueError:
        assert True

    try:
        PushNotification("device-001", "")
        assert False
    except ValueError:
        assert True

    print("All Notification System tests passed!")

if __name__ == "__main__":
    main()