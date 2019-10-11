import mysql.connector as mcdb

class tb_contact:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectToDB(self, host, user, passwd):
        self.conn = mcdb.connect(host=host, user=user, passwd=passwd, database='db_ecom')
        print('Successfully connected to database')
        self.cur = self.conn.cursor()

    def getAllData(self):
        if self.cur is not None:
            self.cur.execute("SELECT  * from tb_contact")
            data = self.cur.fetchall()
            return list(data)
   
    def insertData(self, contact_name,contact_mobile,contact_email,contact_details):
        if self.cur is not None:
            self.cur.execute("INSERT INTO `tb_contact`(`contact_name`,`contact_mobile`,`contact_email`,`contact_details`) VALUES ('{}','{}','{}','{}')".format(contact_name,contact_mobile,contact_email,contact_details))
            self.conn.commit()

    def deleteData(self, id):
        if self.cur is not None:
            self.cur.execute("delete from tb_contact where contact_id={}".format(id))
            self.conn.commit()

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
