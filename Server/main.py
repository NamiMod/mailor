import socket
from threading import Thread
import json as j
import mysql.connector
from mysql.connector import Error
import Mail_Client
import User
import Student
import Class
import re


class ClientThread(Thread):

    def __init__(self, ip, port, connection):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.connection = connection
        print("[+] New thread started for " + ip + ":" + str(port))

    def run(self):
        condition = 0
        while True:
            data = conn.recv(2048)
            if len(data) == 0:
                break
            data_string = data.decode("utf-8").split("\n")
            output = []
            result = 0
            if data_string[0].__contains__('GET'):
                print("Get request")
                request_data = j.loads(data_string[9])
                request_type = request_data['type']
                if request_type == 4:
                    # get student
                    result = 1
                    username = request_data['username']
                    password = request_data['password']
                    login_result = User.login(connection, username, password)
                    if login_result == 0:
                        result = -1
                    elif login_result == 1:
                        output = Student.get_students_data(connection)

                elif request_type == 8:
                    username = request_data['username']
                    password = request_data['password']
                    login_result = User.login(connection, username, password)
                    if login_result == 0:
                        result = -1
                    elif login_result == 1:
                        output = Class.get_classes_data(connection)
                        result = 1

            if data_string[0].__contains__('POST'):
                print("Post request")
                request_data = j.loads(data_string[9])
                if str(data_string[9]).__contains__('type'):
                    request_type = request_data['type']

                    if request_type == 1:
                        # add new student
                        name = request_data['name']
                        email = request_data['email']
                        grade = request_data['grade']
                        class_id = request_data['class_id']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)
                        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            if str(grade).isnumeric() == False or (str(grade).isnumeric() == True and grade < 0) or (
                                    str(grade).isnumeric() == True and grade > 20):
                                result = -1
                            else:
                                if re.search(regex, email):
                                    Student.add_new_student(connection, name, email, class_id, grade)
                                    result = 1
                                else:
                                    result = -1

                    elif request_type == 2:
                        name = request_data['name']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)
                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            Student.delete_student(connection, name)
                            result = 1
                        pass
                    elif request_type == 3:
                        name = request_data['name']
                        email = request_data['email']
                        grade = request_data['grade']
                        class_id = request_data['class_id']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)

                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            if str(grade).isnumeric() == False or (str(grade).isnumeric() == True and grade < 0) or (
                                    str(grade).isnumeric() == True and grade > 20):
                                result = -1
                            else:
                                Student.update_student(connection, name, email, class_id, grade)
                                result = 1

                    elif request_type == 5:
                        name = request_data['name']
                        professor = request_data['professor']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)
                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            Class.add_new_class(connection, name, professor)
                            result = 1

                    elif request_type == 6:
                        class_id = request_data['id']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)
                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            Class.delete_class(connection, class_id)
                            result = 1

                    elif request_type == 7:
                        name = request_data['name']
                        class_id = request_data['id']
                        professor = request_data['professor']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)
                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            Class.update_class(connection, class_id, name, professor)
                            result = 1

                    elif request_type == 9:
                        class_id = request_data['id']
                        username = request_data['username']
                        password = request_data['password']
                        login_result = User.login(connection, username, password)
                        if login_result == 0:
                            result = -1
                        elif login_result == 1:
                            classes = Class.get_classes_data(connection)
                            class_name = ''
                            professor_name = ''
                            for i in classes:
                                if i[0] == class_id:
                                    class_name = i[1]
                                    professor_name = i[2]
                                    break
                            students = Student.get_students_data(connection)
                            output_students = []
                            for i in students:
                                if i[2] == class_id:
                                    student_name = i[0]
                                    student_grade = i[3]
                                    student_email = i[1]
                                    student = [student_name, student_grade, student_email]
                                    output_students.append(student)
                            mail_result = Mail_Client.send_mail_list(output_students, class_name, professor_name)
                            result = 1
                            output = mail_result
                else:

                    for i in range(0, len(request_data)):
                        temp = request_data[str(i + 1)]
                        name = temp['name']
                        professor = temp['Professor']
                        Class.add_new_class(connection, name, professor)
                        result = 1

            # write in this part
            print(result)
            print(output)


if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(host='localhost', database='Mail_Server', user='root')
        if connection.is_connected():
            print("connected to database successfully")

            TCP_IP = '0.0.0.0'
            TCP_PORT = 8083
            BUFFER_SIZE = 2048
            tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpSock.bind((TCP_IP, TCP_PORT))
            threads = []
            print("server started ...")
            print("*********************************")
            while True:
                tcpSock.listen(4)
                (conn, (ip, port)) = tcpSock.accept()
                newThread = ClientThread(ip, port, connection)
                newThread.start()
                threads.append(newThread)

    except Error as error:
        print('-- Cannot communicate with Database! ** error : ', error)
