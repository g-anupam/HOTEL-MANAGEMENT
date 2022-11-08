create database hotel;
use hotel;
create table custdata(custname varchar(20),addr varchar (30),indate varchar(10),outdate
varchar(10));
create table roomtype (sno varchar(5),roomtype varchar(10),rent integer(10));
insert into roomtype values ('1','type A',1000);
insert into roomtype values ('2','type B',2000);
insert into roomtype values ('3','type C',3000);
insert into roomtype values ('4','type D',4000);
create table restaurent (sno integer(10),itemname varchar(10),rate integer(10));
insert into restaurent values(1,"tea",10);
insert into restaurent values(2,"coffee",10);
insert into restaurent values(3,"colddrink",20);
insert into restaurent values(4,"samosa",10);
insert into restaurent values(5,"sandwich",50);
insert into restaurent values(6,"Dhokla",30);
insert into restaurent values(7,"kachori",10);
insert into restaurent values(8,"milk",20);
insert into restaurent values(9,"noodles",50);
insert into restaurent values(10,"pasta",50);
create table laundary(sno integer(10),itemname varchar(10),rate integer(10));
insert into laundary values(1,"pant",10);
insert into laundary values(2,"shirt",10);
insert into laundary values(3,"suit",10);
insert into laundary values(4,"sari",10);

