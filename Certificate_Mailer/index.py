from flask import Flask, render_template,request
import os
import pandas as pd
from PIL import Image,ImageDraw,ImageFont
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

data=Flask(__name__)
@data.route('/')
def login():
    return render_template('login.html')
@data.route('/login',methods=['POST','GET'])
def name():
     if  request.method == 'POST':
         u_name=request.form['user_name']
         password=request.form['password']
         if u_name == 'admin' and password == 'admin':
             return render_template('index.html')
         else:
             return render_template("login.html",result="invalid  username or password")
@data.route('/info',methods=['POST','GET'])
def info():
    if request.method == 'POST':
        filemain=request.files['f']
        filemain.save(filemain.filename)
        data=pd.read_csv(filemain.filename)
        #os.remove(file.filename)
        file=open('id.csv')
        certdata=file.read().split(',')
        file.close()
        for i in data.index:
            data_one=data['fname'][i].title()+" "+data['lname'][i].title()
            img=Image.open("certificate.webp")
            draw=ImageDraw.Draw(img)
            font_text=ImageFont.truetype("arial.ttf",25)
            font_textc=ImageFont.truetype("arial.ttf",15)
            Image_width, Image_height = img.size
            text_bbox= draw.textbbox( (0, 0),data_one,font=font_text)
            text_width=text_bbox[2] -text_bbox[0]
            text_height=text_bbox[3] -text_bbox[1]
            x=(Image_width - text_width)/2
            y=195
            draw.text((x,y),data_one,"black",font=font_text)
            
            certid=str(random.randrange(1000,10000))
            while certid in certdata:
                certid=str(random.randrange(1000,10000))
            file=open('id.csv','a')
            file.write(',')
            file.write(certid)
            file.close()
            y=295
            x=100
            draw.text((x,y),certid,"black",font=font_textc)

            list_data = os.listdir("Upload_image/")
            while  data_one + '.jpg' in list_data:
                data_one = data_one + '1'
            img.save("Upload_image/" + data_one+'.jpg')
            
            sender_mail = "lucifermorin50@gmail.com"
            passcode = "ygbhllokoumekwnw"
            receiver_mail = data['email'][i]
            
            # Create an SMTP connection
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()  # Transfer layer security
            connection.login(user=sender_mail, password=passcode)
            
            # Create the MIMEMultipart message object
            message = MIMEMultipart()   
            message['From'] = sender_mail
            message['To'] = receiver_mail
            message['Subject'] = "OTP for Verification"
        
            # Create the body of the message
            body = f"""Hi {data_one.strip('1')},
            
            Thank you."""
            
            # Attach the text body to the message
            message.attach(MIMEText(body, 'plain'))
            
            # Specify the file to attach
            file_path = "Upload_image/" + data_one+'.jpg'
            # Change this to the actual path of the file you want to attach
            file_name = os.path.basename(file_path)
            
            # Open the file in binary mode and create a MIMEBase object
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            # Encode the file in base64
            encoders.encode_base64(part)
            
            # Add header to the attachment
            part.add_header('Content-Disposition', f'attachment; filename= {file_name}')
            
            # Attach the file to the message
            message.attach(part)
            
            # Send the email
            try:
                connection.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=message.as_string())
                print("Email sent successfully with the OTP and attachment!")
            except Exception as e:
                print("Error in sending mail:", e)
            
            
            # Close the SMTP connection
            connection.quit()

        return render_template("index.html",result="File is successfully Uploaded")
data.run()