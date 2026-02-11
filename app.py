from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

# 🔐 EMAIL CONFIG
SENDER_EMAIL = "nxtsync753@gmail.com"     
APP_PASSWORD = "lwamwggvujfwjfna"           
COMPANY_EMAIL = "dithaxsolutions@gmail.com"

# 🏠 HOME ROUTE
@app.route("/", methods=["GET"])
def home():
    return "Backend is running successfully"

# 📩 COMMON EMAIL FUNCTION
def send_mail(subject, content, reply_to=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = COMPANY_EMAIL
    if reply_to:
        msg["Reply-To"] = reply_to

    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

# 🟣 GET STARTED / REQUEST DEMO
@app.route("/submit", methods=["POST"])
def submit_form():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        program = request.form.get("program")

        content = f"""
New Lead - Get Started / Demo Request

Name    : {name}
Email   : {email}
Phone   : {phone}
Program : {program}
"""

        send_mail(
            subject="New Lead - Dithax Solutions",
            content=content,
            reply_to=email
        )

        return jsonify({"success": True}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"success": False}), 500

# 🟢 ENROLL API
@app.route("/enroll", methods=["POST"])
def enroll():
    try:
        data = request.form

        content = f"""
New Enrollment Request

Name   : {data['name']}
Email  : {data['email']}
Phone  : {data['phone']}
Course : {data['course']}
"""

        send_mail(
            subject=f"Enrollment Request - {data['course']}",
            content=content,
            reply_to=data["email"]
        )

        return jsonify({"message": "Enrollment submitted successfully"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "Server error. Try again."}), 500

# 🔵 ENQUIRE API
@app.route("/enquire", methods=["POST"])
def enquire():
    try:
        data = request.form

        content = f"""
New Enquiry Request

Name   : {data['name']}
Email  : {data['email']}
Phone  : {data['phone']}
Course : {data['course']}
"""

        send_mail(
            subject=f"Enquiry Request - {data['course']}",
            content=content,
            reply_to=data["email"]
        )

        return jsonify({"message": "Enquiry submitted successfully"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "Server error. Try again."}), 500


if __name__ == "__main__":
    app.run(debug=True)
