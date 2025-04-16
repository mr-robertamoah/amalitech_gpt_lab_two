#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import psutil
import os

api_key="4678e16b55fbc219a27e916172091b67"
api_secret="072a4b8d01da90edc315a7d7139f1894"

current_time = time.localtime()
formatted_time = time.strftime("%y-%m-%d %H:%M:%S", current_time)

CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

def send_alert(subject, message):

    from_email = os.getenv("FROM_EMAIL")
    to_email = os.getenv("TO_EMAIL")
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    try:
        msg = MIMEMultipart()
        msg['To'] = to_email
        msg['From'] = from_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        print(app_password)
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.send_message(msg)
        print(f"Email sent: 200")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

cpu_usage = psutil.cpu_percent(interval=1)

ram_usage = psutil.virtual_memory().percent

disk_usage = psutil.disk_usage("/").percent

alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message = f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

if alert_message:
    send_alert(f"Python Monitoring Alert Alert-{formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits.")