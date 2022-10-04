def get_classes_data(connection):
    myCursor = connection.cursor()
    args = []
    myCursor.callproc('get_classes_data', args)
    connection.commit()
    res = []
    for result in myCursor.stored_results():
        res = result.fetchall()
    connection.commit()
    return res


def add_new_class(connection, name, professor_name):
    myCursor = connection.cursor()
    args = [name, professor_name]
    myCursor.callproc('add_new_class', args)
    connection.commit()


def update_class(connection, id, name, professor_name):
    myCursor = connection.cursor()
    args = [id, name, professor_name]
    myCursor.callproc('update_class', args)
    connection.commit()


def delete_class(connection, id):
    myCursor = connection.cursor()
    args = [id]
    myCursor.callproc('delete_class', args)
    connection.commit()
