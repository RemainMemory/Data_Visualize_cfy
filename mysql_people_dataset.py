import mysql_method as mm

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "KINGISME24??",
    "db": "people",
    "charset": "utf8mb3"
}


def add_people(year, rate):
    sql = "INSERT INTO people (year, rate) VALUES (%s, %s);"
    num = mm.execute_sql(sql, (rate, year))
    if num > 0:
        print("Success!")
    else:
        print("Fail!")