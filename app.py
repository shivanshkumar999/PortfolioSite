from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#  Send mail function
def SendEmail(toaddr,subject,message):
    fromaddr = "666anonymailer999@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'html'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    try:
        s.login(fromaddr, "kxwapeedoljoghol")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        return "Email successfully sent. Wait for Shivansh to contact you."
    except:
        return "An Error occured while sending email."
    finally:
        s.quit()

# -----------------------------------------------------
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contactmail', methods=['POST','GET'])
def contactmail():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        message = request.form.get('message')

    body = f"""\
            <html>
            <body>
            <p>Hello, {name}.<br>
            Thanks for contacting Shivansh. He will get in touch with you shortly on the following contact details provided by you.</p><br>
            <p>Name : <span style='font-weight:bolder'>{name}</span></p>
            <p>Email : <span style='font-weight:bolder'>{email}</span></p>
            <p>Mobile No. : <span style='font-weight:bolder'>{mobile}</span></p>
            <p>Message : <span style='font-weight:bolder'>{message}</span></p>
            </body>
            </html>
            """
    
    res = SendEmail(email,f'Thanks for contacting me, {name}', body)
    SendEmail('shivanshkumar752@gmail.com', f"{name} contacted you via portfolio website", body)
    return render_template('contact.html', res = res)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)

