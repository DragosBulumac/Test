import sqlite3

sqllite_connection = sqlite3.connect("company.db")
cursor = sqllite_connection.cursor()


# check if employee already exists
def check_if_employee(employee_id):
    # query for checking
    sql = f"select * from employee where employer_id={employee_id}"

    check = cursor.execute(sql)

    number_of_rows = check.rowcount

    print("number_of_rows", number_of_rows)
    return number_of_rows


# check if department already exists
def check_if_department(department_id):
    # query for checking
    sql = f"select * from department where department_id={department_id}"

    check = cursor.execute(sql)
    return check
