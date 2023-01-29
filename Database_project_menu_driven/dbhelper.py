import mysql.connector as connector
class DBhelper:
    def __init__(self):
        self.conn =connector.connect(host='localhost',
                                     password='as42DF*&15G!68hj',
                                     user='root',
                                     database='mydatabase')
        query='create table if not exists user(userid int primary key , username varchar(10),phone varchar(12))'
        cur=self.conn.cursor()
        cur.execute(query)
        print('created')

    def insert_user(self,userid,name,phone):
        query="insert into user(userid,username,phone)\
            values({},'{}','{}')".format(userid,name,phone)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print('user saved to db')

    def fetch_all(self):
        query="select * from user"
        cur = self.conn.cursor()
        cur.execute(query)
        for r in cur:
            print("userid: ",r[0])
            print("userid: ",r[1])
            print("userid: ",r[2])
            print()
            print()

    def delete(self,userid):
        query="delete from user where userid={}".format(userid)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("deleted")

    def update(self,userid,username,phone):
        query="update user set username='{}',phone='{}' where " \
              "userid={}".format(username,phone,userid)
        print(query)
        cur=self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated")