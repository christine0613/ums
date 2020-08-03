CREATE DATABASE IF NOT EXISTS `userSystem` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `userSystem`;

CREATE TABLE if not exists users 
(userID int not null auto_increment,
firstName varchar(100) not null,
lastName varchar(100) not null,
email varchar(100) not null,
dob int(10) not null,
CONSTRAINT users_pk primary key(id) ) ENGINE=INNODB DEFAULT charset=latin1;