from app.utils import check_if_employee, cursor, sqllite_connection


def add_employer(employ_id, first_name, last_name, age, job, salary, bonus=None):
    if check_if_employee(employ_id) is None:
        print("This employee is already in there.")
    else:
        # insert data into table
        sql = (
            f"INSERT INTO employee(first_name, last_name, age, job, salary, bonus) VALUES ({first_name}, {last_name}, {age}, "
            f"{job}, {salary}, {bonus})"
        )

        print(sql)

        cursor.execute(sql)

        # commit to make changes
        sqllite_connection.commit()

        print(f"You've added the employee with id: {employ_id}")

print(add_employer(1, "test", "test", 22, "test", 100, 0))

def remove_employer(employ_id):
    if check_if_employee(employ_id) is None:
        print(
            "This employee is not in there. You have to add it first before removing it"
        )
    else:
        # Delete data from table
        sql = f"DELETE FROM employee where employ_id={employ_id}"

        cursor.execute(sql)

        # commit to make changes
        sqllite_connection.commit()

        print(f"You've removed the employee with id: {employ_id}")


def apply_bonus(employ_id, bonus):
    if check_if_employee(employ_id) is not None:
        print("This employee is already in there.")
    else:
        sql = f"UPDATE employee SET bonus={bonus} where employer_id={employ_id}"
        cursor.execute(sql)

        # commit to make changes
        connection.commit()

        print(f"You've added the bonus to employee with id: {employ_id}")


# def add_employee_to_department(department_id, name, users):
#     if check_if_department(department_id) is not None:
#         print("This department is already in there.")
#     else:
#         # insert data into table
#         sql = f"INSERT INTO department values({name}, {users}"
#
#         cursor.execute(sql)
#
#         # commit to make changes
#         connection.commit()
#
#         print(f"You've added the department with id: {department_id}")
#
#
# def remove_employee_from_department(department_id):
#     if check_if_department(department_id) is not None:
#         print("This department is already in there.")
#     else:
#         # Delete data from table
#         sql = f"DELETE FROM department where department_id={department_id}"
#
#         cursor.execute(sql)
#
#         # commit to make changes
#         connection.commit()
#
#         print(f"You've removed the department with id: {department_id}")
