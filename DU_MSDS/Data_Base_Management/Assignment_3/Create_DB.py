import mysql.connector
import pandas as pd

# Student: Duncan Ferguson
# Student Id: 871641260
# Final Project
# Date 6/8/2021

"""This file Runs the SQL FILE. the db_host, db_user, db_password, db_name are all global variables
to help make access easier. Please note that if the database does not exist to begin with the file will error"""


global db_host, db_user, db_password, db_name

db_host='127.0.0.1'
db_user='root'
db_password = '64d^)4H6zsQ}'
db_name = 'land_title_chain'

class DOA():
    def __init__(self):
        self.mydb = mysql.connector.connect(host=db_host,
                                            user=db_user,
                                            password=db_password,
                                            database=db_name)

        self.mycur = self.mydb.cursor()

    def clean_db(self):
        sql = 'DROP DATABASE IF EXISTS ' + db_name + ';' + \
              ' CREATE DATABASE ' + db_name + ';' + \
              ' USE ' + db_name + ';'
        self.mycur.execute(sql)

    def runsql_script(self, filename):
        """This Function looks for the SQL script that creates the DB
        It then prints the SQL query on the commandline so the user can see what is is doing"""
        with open(filename, 'r') as sql_file:
        # with open('SQL_Files/Land_Title_Chain.sql', 'r') as sql_file:
            result_iterator = self.mycur.execute(sql_file.read(), multi=True)
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query


    def import_pandas(self, file, table):
        """This Function is meant for Bulk Importing Scrubbed File Pandas Into SQL
        it takes a file in panda form, and table name. It then takes all of the columns
        from that file and puts them into the table. NOTE that if the columns do not line up
        the import won't work. Therefore it needs to be cleaned up before hand"""
        print("Importing into ", table)
        cols = "`,`".join([str(i) for i in file.columns.tolist()])

        for i, row in file.iterrows():
            sql = "INSERT INTO `" + table + "`(`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"
            self.mycur.execute(sql, tuple(row))
        self.mydb.commit()


    def getaccounts(self):
        """This function grabs the account IDs and Account Names current accounts"""
        sql = "Select Account_ID, Account_Names FROM owner_account"
        self.mycur.execute(sql)
        self.sf_account_names = pd.DataFrame(self.mycur, columns=['Account_ID', 'Account_Names'])
        return self.sf_account_names


    def getnewaccounts(self):
        """This function grabs the new account names"""
        sql = "Select Account_Names FROM owner_account WHERE Landman_ID is Null"
        self.mycur.execute(sql)
        self.newaccounts = []
        for row in self.mycur:
            self.newaccounts.append(row[0])
        return sorted(self.newaccounts)


    def getnewaccountstr(self,accountname):
        """This function grabs the details of the properties that have been added for the new accounts"""
        sql = """Select STR, NMA, Land_Description FROM owner_account
                JOIN property
                ON property.Account_ID = owner_account.Account_ID
                WHERE owner_account.Account_Names = '""" + accountname + """'"""
        self.strlist = []
        self.mycur.execute(sql)
        for row in self.mycur:
            self.strlist.append([row[0],row[1],row[2]])
        return sorted(self.strlist)


    def close(self):
        self.mydb.commit()
        self.mydb.close()