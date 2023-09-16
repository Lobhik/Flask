import sqlite3
import pandas as pd



# create connection by using object
# to connect with hotel_data database
# connection = sqlite3.connect('test_user_data.db')
# connection = connection.cursor()



# importing required libraries
import mysql.connector


# host="db4free.net", database="testdb25",
#                                port=3306, user="testdb25",
#                                password="lobhik123", cursorclass=pymysql.cursors.DictCursor)

connection = mysql.connector.connect(
host ="db4free.net",
database="testdb25",
port=3306,
user ="testdb25",
passwd ="lobhik123"
)

# preparing a cursor object
connection = connection.cursor()

# creating database
connection.execute("CREATE DATABASE geeks4geeks")





# connection.execute(table)
file = pd.read_excel("ALL_DIST.xlsx")
#print(file)


exit()
for index, row in file.iterrows():
    #if index > 92825:
        print(index, row['NO'],row['DIST'],row['PART NO'])
    #print(row['SR NO'],row['Name'])

        #exit()
        connection.execute('''INSERT INTO all_dist(list_number,dist,ass_no,as_name,part_no,part_name) 
                        VALUES ({},'{}',{},'{}','{}',"{}")'''.format(row['NO'],row['DIST'],row['ASS NO'],row['ASS'],row['PART NO'],row['PART']))
        
        #print(connection)

        connection.connection.commit()


exit()


##
# connection.execute( '''
#                    INSERT INTO GEEK (Email, First_Name,Last_Name, Score) VALUES ('fgrh@gmail.com','name34','test_lastname',3 )
#                    ''')

# connection.execute( '''
#                    INSERT INTO GEEK (Email, First_Name,Last_Name, Score) VALUES ('{}','{}','{}',{} )
#                    '''.format("ALTER","ggggg","lobhik",87))

#connection.execute("INSERT INTO GEEK VALUES (3,'werre@gmail.com','test_name','test_lastname',3 )")

connection.connection.commit()


# df = pd.read_csv('csvdata.csv')

# df.to_sql()






# # insert query to insert food  details in
# # the above table
# connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )")
# connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )")
# connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )")
 
 

#  # Creating table
# table = """ CREATE TABLE GEEK (
#             id int PRIMARY KEY   NOT NULL,
#             Email VARCHAR(255) NOT NULL,
#             First_Name CHAR(25) NOT NULL,
#             Last_Name CHAR(25),
#             Score INT
#         ); """
 
# connection.execute(table)



#  # Creating table
# table = """ CREATE TABLE test_user_details (
#             id int PRIMARY KEY   NOT NULL,
#             sr_no int NOT NULL,
#             full_name_mr VARCHAR(400) ,
#             full_name VARCHAR(400),
#             id_no VARCHAR(50),
#             gender VARCHAR(50),
#             age int,
#             family int
#         ); """
 
