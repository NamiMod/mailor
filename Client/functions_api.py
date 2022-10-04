import requests
import csv

'''
requests :

1 - > add new student
2 - > delete student
3 - > update student
4 - > get student
5 - > add new class
6 - > delete class
7 - > update class
8 - > get class
9 - > send mail
none - > create class from csv

'''


# add new student
def add_new_student(name, email, grade, class_id, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 1,
        "name": name,
        "email": email,
        "grade": grade,
        "class_id": class_id,
        "username": username,
        "password": password
    })

#add_new_student('nami100', 'mehditeymorian322@gmail.com', 13, 2, 'nami', 'nami')


# delete student
def delete_student(name, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 2,
        "name": name,
        "username": username,
        "password": password
    })


# delete_student('nami99','nami','na')
# delete_student('nami99','nami','nami')


# update student
def update_student(name, email, grade, class_id, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 3,
        "name": name,
        "email": email,
        "grade": grade,
        "class_id": class_id,
        "username": username,
        "password": password
    })


# update_student('nami', 's.namimodarressi.games@gmail.com', 14, 2, 'nami', 'nami')


# get student
def get_student(username, password):
    r = requests.get("http://localhost:8083", json={
        "type": 4,
        "username": username,
        "password": password
    })


# get_student('nami', 'nami')

# add new class
def add_new_class(name, professor_name, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 5,
        "name": name,
        "professor": professor_name,
        "username": username,
        "password": password
    })
    return 1


# add_new_class('Class5','P1','nami','nami')

# delete class
def delete_class(class_id, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 6,
        "id": class_id,
        "username": username,
        "password": password
    })


# delete_class('16','nami','nami')

# update class
def update_class(id, name, professor_name, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 7,
        "id": id,
        "name": name,
        "professor": professor_name,
        "username": username,
        "password": password
    })


# update_class(2,'Algorithm','Professor666','nami','nami')


# get class
def get_class(username, password):
    r = requests.get("http://localhost:8083", json={
        "type": 8,
        "username": username,
        "password": password
    })
    return


# get_class('nami', 'nami')


# send mail
def send_mail(class_id, username, password):
    r = requests.post("http://localhost:8083", json={
        "type": 9,
        "id": class_id,
        "username": username,
        "password": password
    })


# send_mail(2,'nami','nami')

# create class from csv file
def add_new_class_from_csv():
    data = {}
    with open('../class_csv.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['NO']
            data[key] = rows

        r = requests.post("http://localhost:8083", json=data)


add_new_class_from_csv()
