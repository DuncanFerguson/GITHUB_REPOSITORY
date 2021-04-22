import mysql.connector

class DBTest():
    def __init__(self):
        self.__init__()
        self.mydb = mysql.connector.connect(user='root',
                                            password='64d^)4H6zsQ}',
                                            host='127.0.0.1',
                                            database='henry_books')
        self.mycur = self.mydb.cursor()

    def close(self):
        self.mydb.commit()
        self.mydb.close()

    def getbooks(self):
        sql = "SELECT * FROM henry_authors"
        self.mycur.execute(sql)

        for row in self.mycur:
            print(row[1], " ,", row[2])


test = DBTest()
test.getbooks()
test.close()