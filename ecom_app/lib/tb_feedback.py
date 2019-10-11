import mysql.connector as mcdb

class tb_feedback:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllData(self):
        if self.cur is not None:
            self.cur.execute("SELECT  * from tb_feedback")
            data = self.cur.fetchall()
            return list(data)
   
    def insertData(self, feed,email):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_feedback`(`user_id`,`user_name`,`details`) VALUES ('{}','{}','{}')".format(email,email,feed))
            self.conn.commit()

    def deleteData(self, id):
        if self.cur is not None:
            self.cur.execute("delete from tb_feedback where feedback_id={}".format(id))
            self.conn.commit()

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
