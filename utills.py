import mysql.connector as mysql

connection = mysql.connect(host="localhost", user="root",
                           password="", db="movierec")


def saveAnswers(Answer,username):
    cur = connection.cursor(dictionary=True)

    query = "SELECT `user_id` FROM `userinfo` WHERE `username`= '{}'".format(username)
    cur.execute(query)
    userid = cur.fetchone()
    userid = userid["user_id"]

    query = "INSERT INTO `answers` (`user_id`,`input`) VALUES (%s,%s)"
    cur.execute(query, (userid, Answer))
    connection.commit()
    cur.close()

    return True


def saveNewUser(Answer):
    cur = connection.cursor(dictionary=True)
    query = "INSERT INTO `userinfo` (`username`) VALUES (%s)"
    cur.execute(query, (Answer,))
    connection.commit()
    cur.close()

    return True

def getUser(user):
    cur = connection.cursor(dictionary = True)
    query = "SELECT * FROM `userinfo` WHERE `username`= '{}'".format(user)
    cur.execute(query)
    user = cur.fetchone()
    cur.close()
    return user