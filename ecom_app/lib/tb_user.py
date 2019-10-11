import mysql.connector as mcdb
from django.core.mail import send_mail
from django.conf import settings

class tb_user:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllData(self):
        if self.cur is not None:
            self.cur.execute("SELECT `user_id`, `user_name`, `gender`, `email`, `mobile`, `password`, `address`, `photo`, `is_active` FROM `tb_user` WHERE `is_deleted`=0")
            data = self.cur.fetchall()
            return list(data)

    def getData(self, id):
        if self.cur is not None:
            self.cur.execute("SELECT `user_id`, `user_name`, `gender`, `email`, `mobile`, `password`, `address`, `photo` FROM `tb_user` WHERE `user_id`={}".format(id))
            data = self.cur.fetchall()
            return list(data[0])

    def updateActive(self, ID, status):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_user` SET `is_active`='{}' WHERE `user_id`={};".format(status, ID))
            self.conn.commit()

    # def editUser(self, user_id, user_name, gender, email, mobile, password, address):
    #     if self.cur is not None:
    #         self.cur.execute("UPDATE `tb_user` SET `user_name`='{}', `gender`='{}', `email`='{}', `mobile`={}, `password`='{}', `address`='{}' WHERE `user_id`={}".format(user_name, gender, email, mobile, password, address, user_id))
    #         self.conn.commit()

    def editUserWithPhoto(self, user_id, user_name, gender, email, mobile, password, address, photo):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_user` SET `user_name`='{}', `gender`='{}', `email`='{}', `mobile`={}, `password`='{}', `address`='{}', `photo`='{}' WHERE `user_id`={}".format(user_name, gender, email, mobile, password, address, photo, user_id))
            self.conn.commit()

    def insertUser(self, user_name, gender, email, mobile, password, address, photo):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_user`(`user_name`, `gender`, `email`, `mobile`, `password`, `address`, `photo`) VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}')".format(user_name, gender, email, mobile, password, address, photo))
            self.conn.commit()

    def deleteUser(self, user_id):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_user` SET `is_deleted`=1 WHERE `user_id`={}".format(user_id))
            self.conn.commit()



    def authenticate(self, email, password):
        if self.cur is not None:
            #fh = open('ecom_app/lib/DO_NOT_MODIFY.conf', 'r')
            #key = fh.read()
            #print(key)
            #cipher_suite = Fernet(key.encode())
            #password = cipher_suite.encrypt(password.encode()).decode()
            #print(password)
            self.cur.execute("SELECT `email`, `password` FROM `tb_user` WHERE `email`='{}' AND `password`='{}'".format(email, password))
            data = self.cur.fetchall()
            print(data)
            if len(data) == 1:
                return True
            else:
                return False

    def fprocess(self, email):
        if self.cur is not None:
            self.cur.execute("SELECT `password` FROM `tb_user` WHERE `email`='{}' ".format(email))
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

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
