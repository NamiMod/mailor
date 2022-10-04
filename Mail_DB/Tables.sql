create table students(
    name varchar(512),
    email varchar(512),
    class_id int,
    grade numeric(4,2),
    primary key (name),
    foreign key (class_id) references classes(class_id)
);

create table classes(
    class_id int auto_increment,
    class_name varchar(512),
    professor_name varchar(512),
    primary key (class_id)
);

create table system_users(
  user_name varchar(512),
  password varchar(512)
);
