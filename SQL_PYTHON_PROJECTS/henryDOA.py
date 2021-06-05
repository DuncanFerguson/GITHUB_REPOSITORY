# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3421; HW1 Henry
# Date: 4/28/2021
# Teacher: dalton.crutchfield@du.edu

"""This is the database function. The bookstore is list as global variable up top so that it can easily
manipulated. i.e. The Password DATA base, etc. There are a classes that hit the database with SQL commands.
The classes returning single lists for COMBO box 1 are Author, Publisher and Category.
The classes following are Book_by_Author, Books_by_Publisher and Books_by_Category These also return
a list of Book Titles for COMBOBOX2. The resulting value get sent to Books Available where a query is done to return
the BRANCH NAME, ON HAND and PRICE"""


import mysql.connector

global bookstore_db, mycur

# Will want to change this to connect to your database
bookstore_db = mysql.connector.connect(user='root',
                                       password='64d^)4H6zsQ}',
                                       host='127.0.0.1',
                                       database='henry_books')
mycur = bookstore_db.cursor()


class Author(object):
    """This function calls the bookstore DB and returns a list of Authors that currently have written books"""
    def __init__(self):
        self.mycur = mycur
        self.authorlist = self.getlist()

    def getlist(self):
        """Getting a list of Authors Throwing back the Full name for search reasons"""
        self.sql = "SELECT DISTINCT a.AUTHOR_NUM, a.AUTHOR_LAST, a.AUTHOR_FIRST," \
                   " CONCAT(a.AUTHOR_FIRST, ' ', a.AUTHOR_LAST) as AUTHOR_NAME " \
                   "FROM henry_author a " \
                   "JOIN henry_wrote w " \
                   "ON w.AUTHOR_NUM = a.AUTHOR_NUM " \
                   "ORDER BY AUTHOR_NAME ASC;"

        self.mycur.execute(self.sql)

        # Adding author names to a list
        self.authordisplay = []
        for row in self.mycur:
            self.authordisplay.append(row[3])
        return sorted(self.authordisplay)


class Book_by_Author(object):
    """This Query is looking for books written by Author. It is looking for the concat version because that
    is how the data is returned for getting the authors"""
    def __init__(self, authorname=""):
        self.mycur = mycur
        self.authorname = authorname
        self.booklist = self.getlist(self.authorname)

    def getlist(self, authorname):
        self.authorname = authorname
        self.sql2 = "SELECT TITLE, a.AUTHOR_FIRST, a.AUTHOR_LAST, CONCAT(a.AUTHOR_FIRST, ' ', a.AUTHOR_LAST) as AUTHOR_NAME " \
                    "FROM henry_book " \
                    "RIGHT JOIN henry_wrote ON henry_wrote.BOOK_CODE = henry_book.BOOK_CODE " \
                    "RIGHT JOIN henry_author a ON a.AUTHOR_NUM = henry_wrote.AUTHOR_NUM " \
                    "WHERE TITLE IS NOT NULL " \
                    "HAVING AUTHOR_NAME = " + "'" + str(self.authorname) + "'"

        self.mycur.execute(self.sql2)

        # Adding Book titles to a list
        self.booklist = []
        for row in self.mycur:
            self.booklist.append(row[0])

        return sorted(self.booklist)


class Publisher(object):
    """Grabbing Book Titles By Publisher"""
    def __init__(self):
        self.mycur = mycur
        self.publisherlist = self.getlist()

    def getlist(self):
        """Grabbing all distinct publisher names that have a book, and returning as a list"""
        self.sql4 = 'SELECT DISTINCT PUBLISHER_NAME ' \
                    'FROM henry_publisher ' \
                    'JOIN henry_book ' \
                    'ON henry_publisher.PUBLISHER_CODE = henry_book.PUBLISHER_CODE;'
        self.mycur.execute(self.sql4)

        self.publishers = []
        for row in self.mycur:
            self.publishers.append(row[0])
        return sorted(self.publishers)


class Book_by_Publisher(object):
    """This Query is looking for books by Publisher. And grabbing the title to be displayed"""
    def __init__(self, publisher=""):
        self.mycur = mycur
        self.publisher = publisher
        self.booklist = self.getlist(self.publisher)

    def getlist(self, publisher):
        self.publisher = publisher
        self.sql3 = "SELECT b.TITLE " \
                    "FROM henry_publisher p " \
                    "JOIN henry_book b " \
                    "ON p.PUBLISHER_CODE = b.PUBLISHER_CODE " \
                    "WHERE p.PUBLISHER_NAME = " + "'"+ self.publisher + "'"

        self.mycur.execute(self.sql3)

        # Adding Booktitles to a list
        self.booklist = []
        for row in self.mycur:
            self.booklist.append(row[0])

        return sorted(self.booklist)


class Category(object):
    """This function calls the bookstore DB and returns a list of DISTINCT Categories
    I did not feel a need to join the books to the inventory because they all lined up"""
    def __init__(self):
        self.mycur = mycur
        self.catlist = self.getlist()

    def getlist(self):
        """Getting a list of Categories"""
        self.sql = "SELECT DISTINCT TYPE FROM henry_book"

        self.mycur.execute(self.sql)

        # Adding cat types to a list
        self.cats = []
        for row in self.mycur:
            self.cats.append(row[0])
        return sorted(self.cats)


class Book_by_Category(object):
    """This Query is looking for books Books by category type.
    This is different than the category call because the JOIN ensures that the books
    displayed are actually in inventory"""
    def __init__(self, cat=""):
        self.mycur = mycur
        self.cat = cat
        self.booklist = self.getlist(self.cat)

    def getlist(self, cat):
        self.cat = cat
        self.sql3 = "SELECT DISTINCT b.TITLE " \
                    "FROM henry_book b " \
                    "JOIN henry_inventory i " \
                    "ON i.BOOK_CODE = b.BOOK_CODE " \
                    "WHERE b.TYPE = " + "'" + self.cat + "'"

        self.mycur.execute(self.sql3)

        # Adding Booktitles to a list
        self.booklist = []
        for row in self.mycur:
            self.booklist.append(row[0])

        return sorted(self.booklist)


class Books_Available(object):
    """Grabbing all the branches by book name and returning as a list
    The first position is Branch Name, ON hand, then Price as displayed in the Select statment"""
    def __init__(self, title=""):
        self.mycur = mycur
        self.title = title
        self.branchlist = self.getlist(self.title)

    def getlist(self, title):
        self.title = title
        self.sql3 = "SELECT b.BRANCH_NAME, i.ON_HAND , bk.PRICE " \
                   "FROM henry_inventory i " \
                   "JOIN henry_branch b " \
                   "ON i.BRANCH_NUM = b.BRANCH_NUM " \
                   "JOIN henry_book bk " \
                   "ON bk.BOOK_CODE = i.BOOK_CODE " \
                   "WHERE bk.TITLE = " + "'" + str(self.title) + "'"

        self.mycur.execute(self.sql3)
        self.branchbooks = []
        for row in self.mycur:
            self.branchbooks.append([row[0], row[1], row[2]])

        return self.branchbooks
