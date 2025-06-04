import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import requests

import datetime as dt
from datetime import timedelta
import json

def find_week():
    firstday = today.replace(day=1) # 5
    while firstday.weekday() != 6: # 6
      firstday += timedelta(days=1)
      
    if today < firstday: # 7
      return 0
  
    return (today - firstday).days // 7 + 1 # 8

def make_email(title, content, receiver, sender):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = title
    msg.attach(MIMEText(content, 'html', "utf-8"))
    for i in range(0,4):
        with open(DATA_DIR+DIR_NAME+f"{i}.png", "rb") as image_file:
            image = image_file.read()
            image_mime = MIMEImage(image, name=f"{i}.png")
            image_mime.add_header('Content-ID', f'<image{i}>')
            msg.attach(image_mime)
    return msg

def send_email(msg, sender, smtp_server, smtp_port):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_id, email_password)
        server.sendmail(sender, receiver, msg.as_string())
        print('이메일 전송 성공!')
    except Exception as e:
        print(f'이메일 전송 실패: {str(e)}')
    finally:
        server.quit()

def make_html():
    try : 
        respond = requests.get(f"http://localhost:9000/post/?weeks={today.year}-{today.month}-{cur_week}")
        responds = respond.json()
    except : 
        exit(1)
    data = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" id="u0" href="https://ko.rakko.tools/tools/129/lib/tinymce/skins/ui/oxide/content.min.css">
        <link rel="stylesheet" type="text/css" id="u1" href="https://ko.rakko.tools/tools/129/lib/tinymce/skins/content/default/content.min.css">
    </head>
    <body id="tinymce" class="mce-content-body " data-id="content" contenteditable="true" spellcheck="false">"""
    data += """        <h1 style="text-align: center;" data-mce-style="text-align: center;">{year}년 {month}월 {week}주차 뉴스레터</h1>""".format(year=today.year, month=today.month, week=cur_week)
    for new in responds:
        try:
            new_json = json.loads(new["news"].replace('\'', '\"'))
        except Exception as e:
            print(e)
            exit(1)
        data+='''        <h2 style="text-align: center;" data-mce-style="text-align: center;">{title}</h2><p style="text-align: center;" data-mce-style="text-align: center;"><br></p>'''.format(title=new_json["title"])
        data+='''            <div style="text-align : center;" data-mce-style="text-align: center;">
                <img src="cid:image{index}">
            </div>
            <p style="text-align: center;" data-mce-style="text-align: center;">{text}</p>'''.format(text=new_json["text"], year=today.year, month=today.month, week=cur_week, index=new["index"], image=DATA_DIR+DIR_NAME)
    data += """\n     </body>
</html>"""
    return data

DATA_DIR = "/docker/Newsis-Newsletter/"
today = dt.date.today()
cur_week = find_week()
DIR_NAME = f"WEB/Back-end/media/{today.year}-{today.month}-{cur_week}/"
secret_file = ["email_id", "email_password"]

for file_name in secret_file:

    with open(DATA_DIR + "api_key/" + file_name + ".txt", "r") as fp:
        if file_name == "email_id":
            email_id = fp.readline()
        elif file_name == "email_password":
            email_password = fp.readline()

returned_data = make_html()
response = requests.get("http://localhost:9000/user/")
responses = response.json()
for resp in responses:
    receiver = resp['email']
    print("receiver: " + receiver)
    msg = make_email(
        title=f"{resp['name']}님 Newsis Newsletter의 새로운 뉴스를 만나보세요 ({today.month}월 {cur_week}주차)" ,
        content = returned_data, 
        receiver = receiver, 
        sender = email_id)
    send_email(
                msg=msg,
               sender=email_id,
               smtp_server="smtp.gmail.com",
               smtp_port=587
               )