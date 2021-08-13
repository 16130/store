import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os



# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart()
message['From'] = Header("卢星宇", 'utf-8')  # 发送者
message['To'] = Header("贾老师", 'utf-8')  # 接收者

subject = 'HKR测试报告'
message['Subject'] = Header(subject, 'utf-8')

sender = '1613044385@qq.com'
receivers = ['2431320433@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message.attach(MIMEText('测试文件', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的文件
att1 = MIMEText(open('HKR测试报告.html', 'rb').read(),'base64', 'utf-8')
# 邮件内容
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.html"'
message.attach(att1)

tests = os.getcwd()
for i in os.listdir(tests):
    if '.jpg' in i:
        # for j in range(1, 5):
        targetPath = os.path.join(tests, i)
        Image = MIMEImage(open('login1.jpg', 'rb').read())  # 图片的路径
        Image["Content-Type"] = 'image/jpg'
        Image["Content-Disposition"] = "attachment; filename=loginFailed.jpg"
        message.attach(Image)
    else:
        continue






try:
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpObj.login(sender,"cbwiecfaeuzycjad")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")




