import os
import math
import random
import smtplib

def generate_otp():
    digits = "0123456789"
    otp = ""
    for _ in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp

def send_email(email, otp):
    msg = f"{otp} is your OTP"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "pritishinde9075@gmail.com"
    sender_password = "nfjpqjqhtsmzhqtv"


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, email, msg)
        print("OTP sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))
    finally:
        server.quit()

def verify_otp():
    email = input("Enter your email: ")
    generated_otp = generate_otp()

    send_email(email, generated_otp)

    user_otp = input("Enter the OTP you received: ")

    if user_otp == generated_otp:
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")

verify_otp()
