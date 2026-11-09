import pymysql

class Database:
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(host=host, user=user, password=password, database=database)

    def search(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM diddy"
        cursor.execute(sql)
        with cursor() as cursor:
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='admin',
    db='academy',
    )

