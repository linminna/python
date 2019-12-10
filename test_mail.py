# You are using pip version 18.1, however version 19.3.1 is available.
# pip升级，python -m pip --default-timeout=100 install --upgrade pip
# pip命令升级才能使用pip install yagmail
# 此处，pip升级失败，故 邮件发送暂时未完成
import time
import unittest

import yagmail

from HTMLTestRunner import HTMLTestRunner


# 连接邮箱服务器
# 邮件正文、主题、内容的写入
# 邮件发送

def send_mail(report):
    # 连接邮箱服务器
    yag = yagmail.SMTP(user="13572143003@163.com", password="123456lmn", host="smtp.163.com")
    # 邮件主题
    subject = "自动化测试报告"
    # 邮件正文
    content = ['lmn-test', '正文，请查看附件']
    # 发送邮件（若要给多个用户发送邮件，需要将收件人放至list即可）
    # report 邮件附件的路径
    yag.send('1434935576@qq.com', subject, content, report)
    print("---email-send-success----")


class Test_Mail(unittest.TestCase):
    if __name__ == '__main__':
        test_dir = "./tests"
        suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*')
        # 获取当前日期和时间
        timeStr = time.strftime("%Y_%m_%d_%H_%M_%S")
        # html_report = "./tests/report/" + timeStr + "_mail.html"
        html_report = "./tests/report/mail_report.html"
        fp = open(html_report, "wb")
        runner = HTMLTestRunner(stream=fp, title='', description='')
        runner.run(suit)
        # 流的关闭
        fp.close()
        # 发送报告
        send_mail(html_report)
