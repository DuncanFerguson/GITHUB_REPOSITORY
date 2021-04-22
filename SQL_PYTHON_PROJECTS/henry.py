#Student: Duncan Ferguson
#Student Id: 871641260
#Class:
#Assignment: Home_Work_1

from tkinter import *
import tkinter as tk
import mysql.connector

class bookstore(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initial_user_interface()

    def initial_user_interface(self):
        self.parent.title("Henry's Bookstore")
        self.parent.geometry("700x700")
        # TODO make label look better
        self.label = tk.Label(self.parent, text="Type of Search").pack()
        self.cb = StringVar()
        self.b1 = tk.Checkbutton(self.parent, text="Author", variable=self.cb, onvalue='author', offvalue="").pack()
        # self.b2 = tk.Checkbutton(self.parent, text="Category", variable=self.cb, onvalue='category', offvalue="").pack()
        self.b3 = tk.Checkbutton(self.parent, text="Publisher", variable=self.cb, onvalue='publisher', offvalue="").pack()
        self.submit_button = tk.Button(self.parent, text="Submit", state=NORMAL, command=self.submitted, padx=20, pady=5).pack()

    def submitted(self):
        # TODO have the button return the right value
        self.cat_choice = self.cb.get()
        self.parent.destroy()


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

    def getbooks(self,selection):
        # TODO only works for author and publisher
        sql = "SELECT * FROM henry_"+selection
        self.mycur.execute(sql)

        for row in self.mycur:
            print(row[1], " ,", row[2])


def runsql(run):
    """This function runs the query"""
    test = DBTest()
    test.getbooks(run.cat_choice)
    test.close()


if __name__ == '__main__':
   root = tk.Tk()
   run = bookstore(root)
   root.mainloop()
   runsql(run)

   # test = DBTest()
   # test.getbooks()
   # test.close()

