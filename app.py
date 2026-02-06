from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

@app.route("/")
def index():    
    return "App is running Successfully"
@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    program = data.get("program")

    # Gmail credentials
    sender_email = "nxtsync753@gmail.com"       # your Gmail
    sender_password = "lwam wggv ujfw jfna"      # use App Password if 2FA enabled
    receiver_email = "dithaxsolutions@gmail.com"


    # Email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "New Get Started Submission"

    body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Program Interested: {program}
    """
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

