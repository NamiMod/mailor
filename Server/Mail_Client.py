import smtplib
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = '******' # :)
sender_password = '******' # :)


def send_mail_list(students, class_name, professor_name):
    result = []
    for student in students:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(send_mail, student[0], student[1], class_name, professor_name, student[2])
            return_value = future.result()
            result.append(student[2])
            if return_value == 0:
                result.append('Failed')
            elif return_value == 1:
                result.append('Successful')
    return result


def send_mail(student_name, grade, class_name, professor_name, student_email):
    body = 'Student : ' + student_name + '\nGrade : ' + str(grade) + '\nClass : ' \
           + class_name + '\nProfessor : ' + professor_name
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = student_email
    message['Subject'] = 'Message from Mail system for class : ' + class_name
    message.attach(MIMEText(body, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    login_result = session.login(sender_email, sender_password)
    if str(login_result[1]).__contains__('Accepted') == 'False':
        return 0
    text = message.as_string()
    session.sendmail(sender_email, student_email, text)
    session.quit()
    print('Mail Sent')
    return 1
