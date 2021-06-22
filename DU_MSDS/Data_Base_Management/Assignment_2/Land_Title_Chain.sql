# Creating Drops
DROP TABLE IF EXISTS contract;
DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS property;
DROP TABLE IF EXISTS section;
DROP TABLE IF EXISTS owner_account;

# Creating Owner Account Table
CREATE TABLE owner_account
(Account_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Account_Name VARCHAR(30),
Total_NMA INT,
Num_O_Props INT);

# Creating Contact Table
CREATE TABLE contact
(Contact_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
First_Name VARCHAR(30),
Last_Name VARCHAR(30),
Phone_Number INT,
Mailing_Address VARCHAR(30),
Mailing_zip VARCHAR(15),
Account_ID BIGINT,
CONSTRAINT contact_Account_ID_fk FOREIGN KEY (Account_ID) REFERENCES owner_account(Account_ID));

# Creating Section Table
CREATE TABLE section
(Section_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Township_Range VARCHAR(10),
Section_Num VARCHAR(10),
Total_Gross_Acres INT
);

# Creating Property Table
CREATE TABLE property
(Property_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
Gross_Acres INT,
Percent_Interest DECIMAL(5,4),
NMA INT,
Land_Description VARCHAR(250),
Num_Times_Verified INT,
Account_ID BIGINT,
Section_ID BIGINT,
CONSTRAINT property_Account_ID_fk FOREIGN KEY (Account_ID) REFERENCES owner_account(Account_ID),
CONSTRAINT property_Section_ID_fk FOREIGN KEY (Section_ID)  REFERENCES section(Section_ID)
);

# Creating Contract
CREATE TABLE contract
(Contract_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Contract_date DATE,
Deed_File BLOB,
Account_ID BIGINT,
Property_ID BIGINT,
CONSTRAINT contract_Account_ID_fk FOREIGN KEY (Account_ID) References owner_account(Account_ID),
CONSTRAINT contract_Property_ID_fk FOREIGN KEY (Property_ID) References property(Property_ID)
);


