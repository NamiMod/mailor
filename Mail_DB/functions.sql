-- login
create procedure login (in input_user_name varchar(512), input_password varchar(512))
begin
    declare res int default 0;

    select 1 into res from system_users as s where s.user_name = input_user_name
                                        and s.password = input_password;
    select res;
end;

-- get student data
create procedure get_students_data ()
begin
    select *
    from students;
end;

-- get classes data
create procedure get_classes_data ()
begin
    select *
    from classes;
end;

-- add new student
create procedure add_new_student (in input_name varchar(512),in input_email varchar(512),in input_class_id int,in input_grade numeric(4,2))
begin
    insert into students values (input_name,input_email,input_class_id,input_grade);
end;

-- add new class
create procedure add_new_class (in input_name varchar(512),in input_professor_name varchar(512))
begin
    insert into classes(class_name, professor_name) values (input_name,input_professor_name);
end;

-- update student
create procedure update_student (in input_name varchar(512),in input_email varchar(512),in input_class_id int,in input_grade numeric(4,2))
begin
    delete from students where name = input_name;
    insert into students values (input_name,input_email,input_class_id,input_grade);
end;

-- update class
create procedure update_class (in input_class_id int ,in input_name varchar(512),in input_professor_name varchar(512))
begin
    update classes
    set professor_name = input_professor_name
    where class_id = input_class_id;
end;

-- delete student
create procedure delete_student (in input_name varchar(512))
begin
    delete from students where name = input_name;
end;

-- delete class
create procedure delete_class (in input_id int)
begin
    delete from classes where class_id = input_id;
end;
