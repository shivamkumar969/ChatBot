from flask import Flask, render_template, request,jsonify,session
from MailSender import send_my_email
from Knowledgebase import search_knowledge
from ChartGenerator import create_chart
from CaptcgaGenerator import create_captcha
from savedata import saved_enquiry
from savemessage import saved_message

app = Flask(__name__)
UPLOAD_FOLDER='static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def open_about():
    return render_template('about.html')
@app.route('/chat')
def open_chat():
    return render_template('chat.html')

# setting secret key for session
app.secret_key="shivam 5926 shankar 45 sharma"

@app.route('/faq')
def open_faq():
    return render_template('faq.html')
@app.route('/feedback')
def open_feedback():
    return render_template('feedback.html')

@app.route('/submit_feedback',methods=['POST'])
def save_feedback():
    # read data from form
    name=request.form.get("fename")
    email=request.form.get("feemail")
    gender=request.form.get("fegender")
    suggestion=request.form.get("fesuggestion")
    feedback=request.form.get("fefeedback")
    # creating email message to owner
    mail_msg="Hii Admin,<br> A person with name <b>"+name+"</b>, has submitted a feedback of your <b> Chat Bot Portal. <br> Details of the Suggestion and Feedback are :- </b><br><br><b> Name:<b/>"+name+"<br><b>Email Id of Person:<b>"+email+"<br><br><b>Gender:</b>"+gender+"<br><b>Suggestion:</b>"+suggestion+"<br><b>Feedback Message is:</b>"+feedback+"<br>From-<br>Chatbot"
    # Send mail to user
    send_mail="Hii <b>"+name+"</b><br><br>Your feedback is submitted successfully.<br><br>From-<br><b>Chatbot Team SMS Varanasi</b>"
    #sending email allert to owner
    send_my_email(app,"shivamji101202@gmail.com","A new feedback Recived",mail_msg)
    send_my_email(app,email,"Thanks For Feedback",send_mail)
    message="Thanks for your valuable feedback. We will get back to you shortly."
    return render_template("feedback.html",msgg=message)

@app.route('/chatanalytics')
def open_chatanalytics():
    create_chart(); #call to create new grapg
    return render_template('chatanalytics.html')

@app.route('/contact')
def open_contact():
    return render_template('contact.html')

@app.route('/enquiry')
def open_enquiry():
    pname=create_captcha()
    return render_template('enquiry.html',captcha_img_name=pname)
# Route to generate new captcha image
@app.route('/getnew_captcha',methods=['GET'])
def new_captcha():
    pname=create_captcha()
    return jsonify(pname)


@app.route('/submit_enquery',methods=['POST'])
def save_enquery():
    msg=""
    #reading valid captcha
    user_code=request.form.get("encaptcha")
    or_code=session.get("code")
    if user_code==or_code:
        # If captcha is valid, put form data into the session
        session["enname"] = request.form.get("enname")
        session["enemail"] = request.form.get("enemail")
        session["enmobile"] = request.form.get("enmobile")
        session["encourse"] = request.form.get("encourse")
        session["enstate"] = request.form.get("enstate")
        session["encity"] = request.form.get("encity")

        # Now, call the function to save the data to Excel
        saved_enquiry()
        # read data from form
        name=request.form.get("enname")
        email=request.form.get("enemail")
        mobile=request.form.get("enmobile")
        course=request.form.get("encourse")
        state=request.form.get("enstate")
        city=request.form.get("encity")
        # creating email message to owner
        recive_msg="Hii Admin,<br> A student whose name is <b>"+name+"</b>, has submitted a enquiry of your <b> College Enquiry Portal. <br> Details of the Student is :- </b><br><br><b> Name:<b/>"+name+"<br><b>Email Id:<b>"+email+"<br><b>Mobile Number:</b>"+mobile+"<br><b>Course:</b>"+course+"<br><b>State:</b>"+state+"<br><b>City:</b>"+city+"<br><br>From-<b>"+name+"</b>"
        # Create email for student
        send_msg="Hii "+name+",<br><b>Your enquiry is submitted successfully.</b><br>At College Enquiry Portal. <br> Your Details are :- </b><br><br><b> Name:<b/>"+name+"<br><b>Email Id:<b>"+email+"<br><b>Mobile Number:</b>"+mobile+"<br><b>Course:</b>"+course+"<br><b>State:</b>"+state+"<br><b>City:</b>"+city+"<br><br>From-<b>SMS Varanasi</b>"

        #sending email allert to owner
        send_my_email(app,"shivamji101202@gmail.com","A new Enquiry Recived",recive_msg)
        send_my_email(app,email,"Your Enquiry is submitted successfully.",send_msg)
        msg="Thanks your enquiry is submitted."
    else:
        msg="Invalid Captcha code. Please try again."
    pname=create_captcha()
    return render_template("enquiry.html",captcha_img_name=pname,msg=msg)

@app.route('/developer')
def open_developer():
    return render_template('developer.html')

# to get answer of user query
@app.route('/getbotanswer')
def get_bot_answer():
    user_query=request.args.get("userquery")
    result=search_knowledge(user_query)
    return jsonify(result)

#ajax
@app.route('/testajax')
def open_testajax():
    return render_template("addition.html")

# For AJAX Call..
@app.route('/addnum',methods=['GET'])
def call_testajax():
    x=request.args.get("f_num")
    y=request.args.get("s_num")
    reault=int(x)+int(y)
    result=str(reault)
    msg="Addition is :"+result
    return jsonify(msg)

# Test Email sending
@app.route('/send')
def mail_test():
    r=send_my_email(app,"shivamkumar101202@gmail.com","Test Message","Hello, How are You?")
    if r:
        return "Email send sucessfully."
    else:
        return "Sorry! unabel to send email."
    
# Developer mail sender.
@app.route('/submit_mail',methods=['POST'])
def save_message():
    session["cname"] = request.form.get("cname")
    session["cemail"] = request.form.get("cemail")
    session["cmessage"] = request.form.get("cmessage")


    # Now, call the function to save the data to Excel
    saved_message()
    # read data from form
    name=request.form.get("cname")
    email=request.form.get("cemail")
    message=request.form.get("cmessage")

    # creating email message to owner
    recive_msg="Hii Admin,<br> A person whose name is <b>"+name+"</b>, has submitted a message to contact with you. <br> <b>Details of the Person :- </b><br><br><b> Name: </b>"+name+"<br><b>Email Id: <b>"+email+"<br><b>Message: </b>"+message+"<br><br>From-<b>"+name+"</b>"
    # Create email for student
    send_msg="Hii "+name+",<br><b>Your message is submitted successfully.</b><br>Your Details are :- </b><br><br><b> Name: </b>"+name+"<br><b>Email Id: <b>"+email+"<br><b>Your message:</b><br>"+message+"<br><br>From-<b>SHIVAM KUMAR</b>"

    #sending email allert to owner
    send_my_email(app,"shivamji101202@gmail.com","A new Enquiry Recived",recive_msg)
    send_my_email(app,email,"Your Message is submitted successfully.",send_msg)
    msg="Thanks your message is submitted."
    return render_template("developer.html",msg=msg)

# To run the project
if __name__ == '__main__':
    app.run(debug=True)