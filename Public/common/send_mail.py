import os
import time 

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
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
    #邮件标题
    mail_tilte ='自动化测试报告'

    msg = MIMEMultipart()
    msg["Subject"]=Header(mail_tilte,'utf-8')
    msg["From"] =sender_qq_mail

    #邮件正文内容
    msg.attach(MIMEText('测试报告','html','utf-8'))

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
    smtp=SMTP_SSL(host_server)

    smtp.ehlo(host_server)
    smtp.login(sender_qq,pwd)
    smtp.sendmail(sender_qq_mail,receiver,msg.as_string())

    smtp.quit()
    print("Test Report has send out!!")


# ####################查找测试报告，找出最新的测试报告###########################
def newReport(testReport):
    lists = os.listdir(testReport)
    newlists = sorted(lists)
    file_new = os.path.join(testReport,newlists[-1])

    return file_new



