import mysql.connector as mcdb
from django.core.mail import send_mail
from django.conf import settings
#from cryptography.fernet import Fernet

class tb_admin:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user,passwd=passwd,database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def authenticate(self, email, password):
        if self.cur is not None:
            #fh = open('ecom_app/lib/DO_NOT_MODIFY.conf', 'r')
            #key = fh.read()
            #print(key)
            #cipher_suite = Fernet(key.encode())
            #password = cipher_suite.encrypt(password.encode()).decode()
            #print(password)
            self.cur.execute("SELECT `admin_email`, `admin_pass` FROM `tb_admin` WHERE `admin_email`='{}' AND `admin_pass`='{}'".format(email, password))
            data = self.cur.fetchall()
            print(data)
            if len(data) == 1:
                return True
            else:
                return False
               
    def fprocess(self, email):
        if self.cur is not None:
            self.cur.execute("SELECT `admin_pass` FROM `tb_admin` WHERE `admin_email`='{}' ".format(email))
            data = self.cur.fetchone()
            print(data)
            if len(data) == 1:
                subject = 'Forgot Password'
                message = ' Hi Your Password is ' + data[0]
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                send_mail( subject, message, email_from, recipient_list )
                return True
            else:
                return False
            
          

    def cpassword(self, npass,email):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_admin` SET `admin_pass`='{}' WHERE `admin_email`='{}'".format(npass, email))
            self.conn.commit()
            
    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
