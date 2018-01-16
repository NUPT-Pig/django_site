from email.mime.text import MIMEText
import smtplib

from_addr = '*******@qq.com'
auth_code = '*********'  # get it from qq email setting

smtp_server = 'smtp.qq.com'
smtp_port = 465

def send_email(to_addr, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.set_debuglevel(1)
    server.login(from_addr, auth_code)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_email('********@qq.com', 'test')