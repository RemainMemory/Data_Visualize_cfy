import pymysql

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "KINGISME24??",
    "db": "SD_data",
    "charset": "utf8mb3"
}


def get_mysql_connection():
    try:
        con = pymysql.connect(**DB_CONFIG)
        return con
    except Exception as e:
        print(f"Error connecting to database: {str(e)}")
        return None


def execute_sql(sql, params=None):
    try:
        with get_mysql_connection() as con:
            with con.cursor() as cur:
                cur.execute(sql, params)
                con.commit()
                return cur.rowcount
    except Exception as e:
        print(f"Error executing SQL: {str(e)}")
        return None


def query_sql(sql, params=None):
    try:
        with get_mysql_connection() as con:
            with con.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchall()
    except Exception as e:
        print(f"Error executing SQL: {str(e)}")
        return None


def add_student(name, age):
    sql = "INSERT INTO Student (Student_NAME, Student_AGE) VALUES (%s, %s);"
    num = execute_sql(sql, (name, age))
    if num > 0:
        print("Success!")
    else:
        print("Fail!")


def delete_student(student_id):
    sql = "DELETE FROM student WHERE student_id = %s;"
    num = execute_sql(sql, (student_id,))
    if num > 0:
        print("Success!")
    else:
        print("Fail! No student found with the given ID.")


def update_student(student_id, name, age):
    sql = "UPDATE student SET student_name = %s, student_age = %s WHERE student_id = %s;"
    num = execute_sql(sql, (name, age, student_id))
    if num > 0:
        print("Success!")
    else:
        print("Fail!")


def query_student():
    sql = "SELECT * FROM student;"
    result = query_sql(sql)
    for row in result:
        print(row)


def query_student_by_id(student_id):
    sql = "SELECT * FROM student WHERE student_id = %s;"
    result = query_sql(sql, (student_id,))
    print(result)
