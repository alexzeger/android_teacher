import os
import time
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Config import globalconfig
#测试报告的路径
report_path = globalconfig.Report_path

def sendReport(file_new):
    with open(file_new,"rb")as f:
       mail_body = f.read()

    #qq邮箱服务器
    host_server='smtp.qq.com'
    #发件人登录QQ邮箱的账号
    sender_qq='2540911284@qq.com'
    #qq邮箱的授权码
    pwd='dmtczihsrgsyecgd'
    #发件人的邮箱地址
    sender_qq_mail = '2540911284@qq.com'
    #收件人的邮箱地址
    receiver = '2540911284@qq.com'
    # 可添加多个收件人的邮箱
    receives = ['2540911284@qq.com','baojiong@box-fairy.com']
    #邮件标题
    mail_tilte ='android_teacher自动化测试报告'

    msg = MIMEMultipart()
    msg["Subject"]=Header(mail_tilte,'utf-8')
    msg["From"] =sender_qq_mail
    msg['To'] = ','.join(receives)

    #邮件正文内容
    text_plain = MIMEText("附件是最新的android_teacher自动化测试报告，请查看", 'html', 'utf-8')
    msg.attach(text_plain)

    # 构造附件
    filename = "report.html"
    att3 =MIMEText(open(file_new,'rb').read(),'base64','utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att3.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att3)

    # txt
    # #以下代码可以重命名附件为Report.html
    # txt.add_header('Content-Disposition', 'attachment', filename='Report.html')
    # msg_root.attach(html)

    #ssl登录
    # 邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号要使用465
    smtp=SMTP_SSL(host_server, 465)
    # 向服务器标识用户身份
    smtp.helo(host_server)
    # 向服务器返回确认结果
    smtp.ehlo(host_server)
    # 登录邮箱的账号和授权密码
    smtp.login(sender_qq,pwd)
    print("开始发送邮件...")
    # 开始进行邮件的发送，msg表示已定义的字典
    smtp.sendmail(sender_qq_mail,receives,msg.as_string())

    smtp.quit()
    print("已发送邮件")

# ####################查找测试报告，找出最新的测试报告###########################
def newReport(testReport):
    lists = os.listdir(testReport)
    newlists = sorted(lists)
    file_new = os.path.join(testReport,newlists[-1])

    return file_new



