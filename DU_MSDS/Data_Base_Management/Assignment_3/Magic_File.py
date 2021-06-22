from Create_DB import *
import File_Scrubber
import pandas as pd
import Magic_GUI

# Student: Duncan Ferguson
# Student Id: 871641260
# Final Project
# Date 6/8/2021

"""" This file imports Create_DB. There are also folders that are accessed as well
It is best to download the git file https://github.com/DuncanFerguson/SQL_Final_Project.git
and run with that structure. The intention of this project is to create a database
from SQL_Files by running Land_Title_Chain.sql . Then bulk loading Salesforce Reports.
Folder: SF_Reports. Files:" SF_Accounts, SF_Properties, SF_Users, Township_Ranges.

After the database has been made and filled with information. The user is prompted to go through
and find a file to scrub. This file will be located in Folder: Raw_Taxroll_Files File: Sample_File_2_Scubb
After the file is scrubbed, it is uploaded, along with the properties to the data base

A Gui is then prompted to find the new accounts.. null on landman... didnt get to assigning out landmen.
THE gui lets you search by the new account added to look at the accounts
 """

def make_n_load():
    """This function Makes and Loads a Database"""
    # Making the Database
    DOA().runsql_script('SQL_Files/Land_Title_Chain.sql')  # Creating SQL DB
    DOA().close()
    print("Made DB:", db_name)

    # Grabbing Accounts from SF_Reports folder
    df = pd.read_csv("SF_Reports/SF_Accounts.csv",
                     usecols=['Id', 'Name', 'BillingStreet', 'BillingCity', 'BillingStateCode',
                              "BillingPostalCode", "Landman_ID", "Account_Stage"])

    # Renaming Columns to fit the Database
    df = df.rename(columns={'Id':'Account_ID',
                            'Name':'Account_Names',
                            'BillingStreet':'Address',
                            'BillingCity': 'City',
                            'BillingStateCode':'State',
                            'BillingPostalCode':'Zip_Codes',
                            'Landman_ID': 'Landman_ID',
                            'Account_Stage': 'Account_Stage'})

    # Importing owner_accounts
    DOA().import_pandas(df, "owner_account")
    DOA().close()

    # Grabbing Users and inputting them into the Database
    df_users = pd.read_csv("SF_Reports/SF_Users.csv")
    df_users = df_users.rename(columns= {'Full Name': 'Full_Name',
                                         'Landman_ID':'Landman_ID'})
    DOA().import_pandas(df_users, "landmen")

    # Grabbing Sections and inputting them into the Database
    df_sections = pd.read_csv("SF_Reports/Township_Ranges.csv")
    DOA().import_pandas(df_sections, "sections")

    # Grabbing Properties and inputting them into the Database
    df_properties = pd.read_csv("SF_Reports/SF_Properties.csv")
    DOA().import_pandas(df_properties, "property")
    return

def make_db_updates():
    """This Function Makes updates to the Database. It is currently not being used
    but all you have to do is pass a file path in to update the database"""
    DOA().runsql_script('SQL_Files/Land_Title_Chain_Updates.sql')

def snag_n_add():
    """This Function is aimed at making the database and fill in it's contents"""
    # Asking the User to select the file to scrub
    rawlist = File_Scrubber.startoption("To start we will have to import a CSV File.\n "
                          "This file is located in:\n\n"
                          "**Folder Name: RAW_Taxroll_Files**\n\n"
                          "**File Name: Sample_File_2_Scrubb**\n\n"
                          "Click the start button to proceed.")

    account_col = File_Scrubber.HeaderGui("Please click on the Name Column\n"
                                          "This is the column that needs to be scrubbed\n\n"
                                          "**For this Project it's called 'Owner'**",
                                          list(rawlist.columns.values))

    # Sending over the Names to get scrubbed
    names_scrubbed_list = File_Scrubber.fixnames(rawlist, account_col.choice)
    print("Raw File Grabbed")

    # Grabbing Newly Loaded SQL Accounts Then matching ID's new newly scrubbed batch
    accounts_2_scrub_off = DOA().getaccounts()
    raw_file_w_id = File_Scrubber.lookup_ids(names_scrubbed_list, accounts_2_scrub_off)
    # TODO make sure to load the properties for the accounts that do have IDs

    # Sending off raw_file_w_id to have it's addresses scrubbed
    accounts_scrubbed = File_Scrubber.create_new_accounts(raw_file_w_id)

    # Importing the new accounts into the database
    DOA().import_pandas(accounts_scrubbed, "owner_account")
    DOA().close

    # Looking at the scubbed file. Now Adding in Properties
    new_accounts_2_scrub_off = DOA().getaccounts()
    props_2_add = File_Scrubber.lookup_ids(names_scrubbed_list, new_accounts_2_scrub_off)
    props_2_add = props_2_add[props_2_add['Account_ID'].notnull()]  # Getting rid of any from the scrub with no ID
    props_2_add = props_2_add[['STR',
                               'Total_Gross_Acres',
                               'Percent_Interest',
                               'NMA',
                               'Land_Description',
                               'Account_ID']]

    # Adding new properties to the database
    DOA().import_pandas(props_2_add,'property')

def display_imports():
    """This function is aimed at creating a GUI that will Query the database and
    show all the new files that have been added from the scrubbed file."""
    Magic_GUI.GUI()


def main():
    """Main Function that starts the File"""
    DOA().clean_db()  # Calling in clean_db() from Create_DB.py
    make_n_load()  # Using function in file to make and load db.
    snag_n_add()
    # make_db_updates()
    display_imports()
    # print("Final Scrubbed File", scrubbed_file)
    print("Main Done Running")

if __name__ == '__main__':
    main()


# Open Up the Fill Scrubber
# File_Scrubber.main()
