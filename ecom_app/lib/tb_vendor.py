import mysql.connector as mcdb

class tb_vendor:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllData(self):
        if self.cur is not None:
            self.cur.execute("SELECT * from  tb_vendor")
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

    def editUserWithPhoto(self,  user_name, gender, email, mobile, address,user_id):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_vendor` SET `user_name`='{}', `gender`='{}', `email`='{}', `mobile`={},  `address`='{}',  WHERE `user_id`={}".format(user_name, gender,email, mobile, address,user_id))
            self.conn.commit()

    def insertUser(self, user_name, gender, email, mobile, address):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_vendor`(`user_name`, `gender`, `email`, `mobile`, `address`) VALUES ('{}', '{}', '{}', {}, '{}')".format(user_name, gender, email, mobile, address))
            self.conn.commit()

    def deleteUser(self, vendor_id):
        if self.cur is not None:
            self.cur.execute("delete  from  `tb_vendor`  WHERE `vendor_id`={}".format(vendor_id))
            self.conn.commit()



    

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
