# import MySQLdb
import mysql.connector
import csv
conn = mysql.connector.connect(
    host="localhost", user="root", password="gaurav4u7", database="csvtosql")
# conn = mysql.connector.connect(
#     host="localhost", username="root", password="gaurav4u7", database="csvtosql")

with open('iris.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')

    all_values = []

    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4])
        all_values.append(value)

query = "insert into iris values (%s,%s,%s,%s,%s) "


mycursor = conn.cursor()
mycursor.executemany(query, all_values)
conn.commit()
