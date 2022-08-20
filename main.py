import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con = connector.connect(host="localhost", user="root", passwd="root", database="pythontest")
        query='create table if not exists user(userId int primary key, username varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created table")

    def insert_user(self, userId, username, phone): 
        query = "insert into user(userId, username, phone) values({}, '{}', '{}')".format(userId, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User added to db")

    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id: ", row[0])
            print("User name: ", row[1])     
            print("Phone: ", row[2])      
            print()
            print()


#main function
helper = DBhelper()
#helper.insert_user(5, "Abhay jjjjj", "1234567890")
helper.fetch_all()
