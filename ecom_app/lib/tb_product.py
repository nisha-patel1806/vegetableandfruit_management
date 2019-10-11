import mysql.connector as mcdb

class tb_product:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllData(self):
        if self.cur is not None:
            self.cur.execute("SELECT E.`product_id`, E.`product_name`, E.`product_details`, E.`product_price`, F.`category_name`, E.`product_image`, E.`is_active` FROM `tb_product` E, `tb_category` F WHERE F.`category_id`=E.`category_id` AND E.`is_deleted`=0 ORDER BY `product_id`")
            data = self.cur.fetchall()
            return list(data)

    def getData(self, id):
        if self.cur is not None:
            self.cur.execute("SELECT * from `tb_product` WHERE `product_id`={}".format(id))
            data = self.cur.fetchall()
            return list(data[0])

    def updateActive(self, ID, status):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_product` SET `is_active`='{}' WHERE `product_id`={};".format(status, ID))
            self.conn.commit()

    # def editUser(self, user_id, user_name, gender, email, mobile, password, address):
    #     if self.cur is not None:
    #         self.cur.execute("UPDATE `tb_user` SET `user_name`='{}', `gender`='{}', `email`='{}', `mobile`={}, `password`='{}', `address`='{}' WHERE `user_id`={}".format(user_name, gender, email, mobile, password, address, user_id))
    #         self.conn.commit()

    # def editUserWithPhoto(self, user_id, user_name, gender, email, mobile, password, address, photo):
    #     if self.cur is not None:
    #         self.cur.execute("UPDATE `tb_user` SET `user_name`='{}', `gender`='{}', `email`='{}', `mobile`={}, `password`='{}', `address`='{}', `photo`='{}' WHERE `user_id`={}".format(user_name, gender, email, mobile, password, address, photo, user_id))
    #         self.conn.commit()

    def editProduct(self, pname, pdetails, pprice, filePath, category, id):
        if self.cur is not None:
            #pdetails.replace("'", "")
            self.cur.execute("UPDATE `tb_product` SET `product_name`='{}', `product_details`=\"{}\", `product_price`={}, `product_image`='{}', `category_id`=(SELECT `category_id` FROM `tb_category` WHERE `category_name`='{}') WHERE `product_id`={}".format(pname, pdetails, pprice, filePath, category, id))
            self.conn.commit()

    # def insertUser(self, user_name, gender, email, mobile, password, address, photo):
    #     if self.cur is not None:
    #         self.cur.execute("INSERT INTO `tb_user`(`user_name`, `gender`, `email`, `mobile`, `password`, `address`, `photo`) VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}')".format(user_name, gender, email, mobile, password, address, photo))
    #         self.conn.commit()

    def insertProduct(self, pname, pdetails, pprice, filePath, category):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_product`(`product_name`, `product_details`, `product_price`, `product_image`, `category_id`) VALUES ('{}', '{}', {}, '{}', (SELECT `category_id` FROM `tb_category` WHERE `category_name`='{}'))".format(pname, pdetails, pprice, filePath, category))
            self.conn.commit()

    def deleteProduct(self, p_id):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_product` SET `is_deleted`=1 WHERE `product_id`={}".format(p_id))
            self.conn.commit()

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
