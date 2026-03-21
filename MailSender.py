from flask_mail import Message

def send_my_email(mail, sendto, subject, message):
    try:
        msg = Message(
            subject=subject,
            recipients=[sendto]
        )
        msg.html = message
        mail.send(msg)
        return True
    except Exception as e:
        print("Mail Error:", e)
        return False
