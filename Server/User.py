def login(connection, username, password):
    myCursor = connection.cursor()
    args = [username, password]
    myCursor.callproc('login', args)
    connection.commit()
    res = 0
    for result in myCursor.stored_results():
        res = result.fetchall()[0][0]
    connection.commit()
    return res
