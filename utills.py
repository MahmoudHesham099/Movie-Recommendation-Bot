import mysql.connector as mysql
import datetime

connection = mysql.connect(host="localhost", user="root",
                           password="", db="flaskapp")

def getUser(user):
    cur = connection.cursor(dictionary = True)
    query = "SELECT * FROM `user_info` WHERE `username`= '{}'".format(user)
    cur.execute(query)
    user = cur.fetchone()
    cur.close()
    return user

def save(user_id):
    cur = connection.cursor(dictionary=True)
    query = "INSERT INTO `user_info` (user_id , date) VALUES(%s,%s)"
    cur.execute(query, (user_id, datetime.datetime.now()))
    connection.commit()
    cur.close()
    return True

