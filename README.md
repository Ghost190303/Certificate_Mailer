# 🎓 Certificate_Mailer

**Certificate_Mailer** is a Flask-based web application that automates the process of generating personalized certificates and emailing them to recipients. Upload a CSV with user details, and the app will create custom certificates using a template and send them as attachments via email.

---

## 🚀 Features

- Upload CSV file with names and emails
- Generate personalized certificates from a template (`.webp`)
- Automatically assign unique certificate IDs
- Save generated certificates in the `Upload_image/` directory
- Send personalized emails with certificate attachments
- Simple login system for admin access

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Libraries**: Pandas, Pillow (PIL), smtplib, email
- **Frontend**: HTML (Jinja templates)
- **Data Format**: CSV for input

---

## Run the Flask app
- python index.py
- Open your browser and go to:
- http://127.0.0.1:5000/

---

## How to Use
1. Go to / and log in using:
- Username: admin
- Password: admin

2. Upload a .csv file with columns:
- fname (First Name)
- lname (Last Name)
- email (Email ID)

3. Certificates will be:
- Generated with names and IDs
- Stored in Upload_image/
- Emailed to each recipient as an attachment

---

## ⚠️ Note
- Replace the Gmail credentials in **index.py** with your App Password for security.
- Ensure certificate.webp and arial.ttf are in the project directory.
- This script uses SMTP over TLS (smtp.gmail.com, port 587).
