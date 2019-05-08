#coding:utf-8
from django.core.mail import send_mail
from learn_dj.settings import EMAIL_FROM
import random


def get_str(str_length=8):
    str = ''
    strChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(str_length):
        str = str + strChar[random.randint(0,62)]
    return str

def send_user_email(type=1):
    email_title = ""
    email_body = ""
    if type == 1:
        email_title = '单发邮件'
        email_body = get_str()
        # sender = '986725816@qq.com'
        receiver = ['yangsonglin@mofanghr.com']
        send_status = send_mail(email_title,email_body,EMAIL_FROM,receiver,fail_silently=False)
        if send_status:
            pass
    # else:
    #     subject = '群发邮件'
    #     message = get_str(20)
    #     sender = '986725816@qq.com'
    #     receiver = ['yangsonglin@mofanghr.com','971794995@qq.com']


if __name__ == '__main__':
    print(get_str())