import mysql.connector as mcdb

class tb_ordermaster:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllData(self):
        if self.cur is not None:
            self.cur.execute(" select * from tb_order_master")
            data = self.cur.fetchall()
            return list(data)

    def getData(self, id):
        if self.cur is not None:
            self.cur.execute("SELECT E.`product_id`, E.`product_name`, E.`product_details`, E.`product_price`, F.`category_name`, E.`product_image` FROM `tb_product` E, `tb_category` F WHERE E.`product_id`={} AND E.`category_id`=F.`category_id`".format(id))
            data = self.cur.fetchall()
            return list(data[0])

    def updateActive(self, ID, status):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_product` SET `is_active`='{}' WHERE `product_id`={};".format(status, ID))
            self.conn.commit()
 


    # def insertUser(self, user_name, gender, email, mobile, password, address, photo):
    #     if self.cur is not None:
    #         self.cur.execute("INSERT INTO `tb_user`(`user_name`, `gender`, `email`, `mobile`, `password`, `address`, `photo`) VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}')".format(user_name, gender, email, mobile, password, address, photo))
    #         self.conn.commit()

    def insertProduct(self, order_date, user_id, order_status):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_order_master`(`order_date`, `user_id`, `order_status`) VALUES ('{}', '{}', '{}')".format(order_date, user_id, order_status))
            self.conn.commit()

    def deleteProduct(self, p_id):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_product` SET `is_deleted`=1 WHERE `product_id`={}".format(p_id))
            self.conn.commit()






    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
