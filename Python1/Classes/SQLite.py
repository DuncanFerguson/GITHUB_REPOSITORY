import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_property(conn, property):
    """
    Create a new book
    :param conn:
    :param property:
    :return:
    """

    sql = ''' INSERT INTO property(name,price,address,listedDate, realtorID)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, property)
    conn.commit()

    return cur.lastrowid

def create_realtor(conn, realtor):
    """
    Create a new book
    :param conn:
    :param realtor:
    :return:
    """

    sql = ''' INSERT INTO realtor(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, realtor)
    conn.commit()

    return cur.lastrowid

def main():
    database = r"C:\Users\dunca\OneDrive\Desktop\TestingDB.db"

    sql_create_property_table = """ CREATE TABLE IF NOT EXISTS property (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        price integer,
                                        address text,
                                        listedDate integer,
                                        realtorID integer
                                    ); """
    sql_create_realtor_table = """ CREATE TABLE IF NOT EXISTS realtor (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create books table
        create = input('Create the tables? (y/n)')
        if create.lower() == 'y':
            create_table(conn, sql_create_property_table)
            create_table(conn, sql_create_realtor_table)

        #Enter Realtors
        enterRealtors = input('Insert Realtors? (y/n)')
        if enterRealtors.lower() == 'y':
            name= ''
            while name.lower() != 'n':
                name = input('What is Their Name? (enter n to exit)')
                if name.lower() != 'n':
                    create_realtor(conn, (name,))

        #Select all Realtors
        cur = conn.cursor()
        cur.execute('SELECT * FROM realtor')
        rows = cur.fetchall()
        names = list(map(lambda x: x[0], cur.description))
        print(names)
        for row in rows:
            print(row)

        #Enter Properties
        enterProp= input('Insert Properties? (y/n)')
        if enterProp.lower() == 'y':
            name= ''
            while name.lower() != 'n':
                name = input('What is The Name? (enter n to exit)')
                if name.lower() != 'n':
                    price = int(input('What is The Price?'))
                    address = input('What is The Address?')
                    date = input('When Was it Listed?')
                    realtor = int(input('What is the Realtor ID?'))
                    create_property(conn, (name,price,address, date, realtor))

        #Select all Properties
        cur = conn.cursor()
        cur.execute('SELECT * FROM property')
        rows = cur.fetchall()
        names = list(map(lambda x: x[0], cur.description))
        print(names)
        for row in rows:y
            print(row)

    else:
        print("Error! cannot create the database connection.")



if __name__ == '__main__':
    main()
