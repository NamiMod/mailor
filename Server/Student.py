def get_students_data(connection):
    myCursor = connection.cursor()
    args = []
    myCursor.callproc('get_students_data', args)
    connection.commit()
    res = []
    for result in myCursor.stored_results():
        res = result.fetchall()
    connection.commit()
    return res


def add_new_student(connection, name, email, class_id, grade):
    myCursor = connection.cursor()
    args = [name, email, class_id, grade]
    myCursor.callproc('add_new_student', args)
    connection.commit()


def update_student(connection, name, email, class_id, grade):
    myCursor = connection.cursor()
    args = [name, email, class_id, grade]
    myCursor.callproc('update_student', args)
    connection.commit()


def delete_student(connection, name):
    myCursor = connection.cursor()
    args = [name]
    myCursor.callproc('delete_student', args)
    connection.commit()
