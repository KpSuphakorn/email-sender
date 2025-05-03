import smtplib, ssl
import schedule
import time
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# โหลดค่า .env เข้ามา
load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")

def send_email():
    msg = EmailMessage()
    msg.set_content("สวัสดีครับ! นี่คือข้อความจาก Python ที่ส่งทุกวันตอน 8 โมงเช้า :)")
    msg["Subject"] = "แจ้งเตือนรายวัน"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
        print("อีเมลถูกส่งแล้ว!")

schedule.every().day.at("01:28").do(send_email)
print("กำลังรอเวลาส่งอีเมลทุกวันตอน 8 โมงเช้า...")
while True:
    schedule.run_pending()
    time.sleep(60)