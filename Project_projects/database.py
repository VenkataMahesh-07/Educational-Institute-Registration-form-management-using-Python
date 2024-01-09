import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="Student")
cursor = connection.cursor()

# Query for creating registration table

#registration_table = """CREATE TABLE Registration(Date CHAR(30),Name CHAR(30),Mobile_Number CHAR(30),Alternate_Number CHAR(30),Email_Id CHAR(30),Address CHAR(30),Course_Interested CHAR(30),Batch_Preferred CHAR(30),How_You_Came_To_Know_us CHAR(30),Experience_Fresher CHAR(30),Contact_Person_From_Besant CHAR(30),Counselor CHAR(30),Fees CHAR(30),Comments CHAR(30))"""
#cursor.execute(registration_table)

# Query for creating enquiry table
enquiry_table = """CREATE TABLE Enquiry(Date CHAR(30),Form_Number CHAR(30),Name CHAR(30),Course CHAR(30),Phone_Number CHAR(30),Email_Id CHAR(30),Address CHAR(30),Status CHAR(30))"""
cursor.execute(enquiry_table)

print("Table created Successfully")
connection.close()
