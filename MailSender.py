from flask_mail import Mail,Message
def send_my_email(app_obj,sendto,subject,message):
    try:
        app_obj.config['MAIL_SERVER']='smtp.gmail.com'
        app_obj.config['MAIL_PORT'] = 587
        app_obj.config['MAIL_USE_TLS']=True
        app_obj.config['MAIL_USERNAME']='shivamji101202@gmail.com'
        app_obj.config['MAIL_PASSWORD']='vezp ahya xxpo trgo'
        app_obj.config['MAIL_DEFAULT_SENDER']='shivamji101202@gmail.com'
        mail=Mail(app_obj)
        msg=Message(subject=subject,recipients=[sendto])
        msg.html=message
        mail.send(msg)
        return True
    except:
        return False