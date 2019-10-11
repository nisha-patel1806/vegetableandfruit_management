import mysql.connector as mcdb

class tb_category:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllCategories(self):
        if self.cur is not None:
            self.cur.execute("SELECT `category_id`, `category_name` FROM `tb_category` WHERE `is_deleted`=0")
            data = self.cur.fetchall()
            return list(data)

    def getCategory(self, cat_id):
        if self.cur is not None:
            self.cur.execute("SELECT `category_id`, `category_name` FROM `tb_category` WHERE `category_id`={}".format(cat_id))
            data = self.cur.fetchall()
            return list(data[0])

    def getAllCategoryNames(self):
        if self.cur is not None:
            self.cur.execute("SELECT `category_name` FROM `tb_category` WHERE `is_deleted`=0")
            data = self.cur.fetchall()
            return list(data)

    # def getCategoryName(self, id):
    #     if self.cur is not None:
    #         self.cur.execute("SELECT `category_name` FROM `tb_category` WHERE `category_id`={}".format(id))
    #         data = self.cur.fetchall()
    #         return list(data)

    # def updateActive(self, ID, status):
    #     if self.cur is not None:
    #         self.cur.execute("UPDATE `tb_user` SET `is_active`='{}' WHERE `user_id`={};".format(status, ID))
    #         self.conn.commit()

    def editCategory(self, cat_id, cat_name):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_category` SET `category_name`='{}' WHERE `category_id`={}".format(cat_name, cat_id))
            self.conn.commit()

    def insertCategory(self, cat_name):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_category`(`category_name`) VALUES ('{}')".format(cat_name))
            self.conn.commit()

    def deleteCategory(self, cat_id):
        if self.cur is not None:
            self.cur.execute("UPDATE `tb_category` SET `is_deleted`=1 WHERE `category_id`={}".format(cat_id))
            self.conn.commit()

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
