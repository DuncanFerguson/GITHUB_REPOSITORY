#Student: Duncan Ferguson
#Student Id: 871641260
#Class:
#Assignment: Home_Work_1

from tkinter import *
import tkinter as tk
import pandas as pd
import mysql.connector
from mysql.connector import errorcode


class bookstore(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initial_user_interface()

        # self.check_button_1 = IntVar()
        # self.check_button_1 = bookstore.search_cat(self)
        # self.sb = bookstore.submit_button(self)


    def initial_user_interface(self):
        self.parent.title("Henry's Bookstore")
        self.parent.geometry("1000x1000")
        self.label=tk.Label(self.parent, text="Type of Search")
        self.b1 = tk.Checkbutton(self.root, text="Search By Author", variable=self.check_button_1, onvalue=1, offvalue=0, command=self.isCheck).pack()
        self.b2 = tk.Checkbutton(self.root, text="Search by Category", variable=self.check_button_1, onvalue=2, offvalue=0, command=self.isCheck).pack()
        self.b3 = tk.Checkbutton(self.root, text="Search By Publisher", variable=self.check_button_1, onvalue=3, offvalue=0, command=self.isCheck).pack()

    # def search_cat(self):
    #     """Searching by Author, Category and Publisher"""
    #
    #     return
    #
    # def submit_button(self):
    #     Button(self.parent, text="Submit", state=NORMAL, padx=20, pady=5).pack()
    #
    #     # TODO: make this so that it returns the query
    #
    # def isCheck(self):
    #     if self.parent.get == 1:
    #         Label(self.root, text=f'Checkbutton is checked:').pack()
    #     else:
    #         Label(self.root, text=f'Checkbutton is checked:').pack()
    #     return



class DBTest():
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root',
                                            password='64d^)4H6zsQ}',
                                            host='127.0.0.1',
                                            database='henry_books')
        self.mycur = self.mydb.cursor()

    def close(self):
        self.mydb.commit()
        self.mydb.close()

    def getbooks(self):
        sql = "SELECT * FROM henry_author"
        self.mycur.execute(sql)

        for row in self.mycur:
            print(row[1], " ,", row[2])


if __name__ == '__main__':
   root = tk.Tk()
   run = bookstore(root)
   root.mainloop()
   test.getbooks()
   test.close()



