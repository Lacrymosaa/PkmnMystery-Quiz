import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    username = "marian",
    password = "password1",
    database = "redandblue"
)

cursor = db.cursor()
i = 1
x = 4
while i <= 56:
    numeracao = x
    x += 1
    qu = input("Question: ")
    qu1 = input("Answer 1: ")
    qu2 = input("Answer 2: ")
    qu3 = input("Answer 3: ")
    qu4 = input("Answer 4: ")
    cursor.execute(
        "INSERT INTO questionary (id, Q, q1, q2, q3, q4) VALUES (%s, %s, %s, %s, %s ,%s);",
        (numeracao, qu, qu1, qu2, qu3, qu4)
    )
    db.commit()
    print("Sucess!")
    i += 1

cursor.close()
