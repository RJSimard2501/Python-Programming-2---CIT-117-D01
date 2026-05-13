#Name: Remi Simard
#Assignment: SQL and Python
#Reflection:
#What I liked about this assignment:
#I enjoyed learning how Python and SQLite work together and store and it was interesting to use SQL joins to combine information from different tables.
#
#What I struggled with:
#I had trouble understanding how joins connect matching records between tables. I also needed practice to prevent duplicate data from being inserted.
#
#In your own words how does decoration work & how does it help coders write better code?
#Decorators let coders change or extend the behavior of functions without changing the original function code. And they also help reduce repeated code and make programs easier to maintain.
#
#In your own words how do the DDL and DML Statements work and how did you use them?
#DDL statements create and define database structures like tables and DML statements work with the data inside the tables. In this assignment I used DDL to create tables and DML to insert and get data.
#
#In your own words describe how SQL Select Joins work in your code?
#SQL joins combine related data from different tables using matching columns. In this program Employee joined to Pay using EmployeeID and Pay joined to SocialSecurityMin using the Year column.
#
#Share exactly 2 things you learned on this assignment:
#1. How to create and populate SQLite tables using Python.
#2. How SQL joins combine related records from multiple tables.

#Imports
import sqlite3
import csv

#Connect to SQLite Database
conn = sqlite3.connect("Retirement.db")
cursor = conn.cursor()

#Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pay (
    EmployeeID INTEGER,
    Year INTEGER,
    Earnings REAL)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SocialSecurityMin (
    Year INTEGER PRIMARY KEY,
    Minimum REAL)""")

#Check if tables already contain data
#Prevent duplicate inserts
cursor.execute("SELECT COUNT(*) FROM Employee")
employee_count = cursor.fetchone()[0]

if employee_count == 0:
    
    #Insert Employee Data
    with open("Employee.txt", "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header row

        for row in reader:
            cursor.execute("""
            INSERT INTO Employee (EmployeeID, Name)
            VALUES (?, ?)
            """, (int(row[0]), row[1]))

    #Insert the Pay Data
    with open("Pay.txt", "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header row

        for row in reader:
            cursor.execute("""
            INSERT INTO Pay (EmployeeID, Year, Earnings)
            VALUES (?, ?, ?)
            """, (int(row[0]), int(row[1]), float(row[2])))

    #Insert Social Security Minimum Data
    with open("SocialSecurityMinimum.txt", "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header row

        for row in reader:
            cursor.execute("""
            INSERT INTO SocialSecurityMin (Year, Minimum)
            VALUES (?, ?)
            """, (int(row[0]), float(row[1])))

    print("Data inserted successfully.")

else:
    print("Data already exists. No duplicate records inserted.")

#Commit Changes
conn.commit()

#Join Tables Togeather
query = """
SELECT
    Employee.EmployeeID,
    Employee.Name,
    Pay.Year,
    Pay.Earnings,
    SocialSecurityMin.Minimum
FROM Employee
JOIN Pay
    ON Employee.EmployeeID = Pay.EmployeeID
JOIN SocialSecurityMin
    ON Pay.Year = SocialSecurityMin.Year
ORDER BY Employee.EmployeeID, Pay.Year
"""

cursor.execute(query)

results = cursor.fetchall()

#Print Results
print("\nRetirement Qualification Report")
print("-" * 70)

for row in results:

    employee_id = row[0]
    name = row[1]
    year = row[2]
    earnings = row[3]
    minimum = row[4]

    if earnings >= minimum:
        qualifies = "Yes"
    else:
        qualifies = "No"

    print(f"ID: {employee_id} | "
          f"Name: {name} | "
          f"Year: {year} | "
          f"Earnings: ${earnings:.2f} | "
          f"Minimum: ${minimum:.2f} | "
          f"Counts Toward Retirement: {qualifies}")

#Close Database
conn.close()
