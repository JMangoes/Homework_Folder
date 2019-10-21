create table departments (
	dept_no varchar(30) primary key not null,
	dept_name varchar(50) not null);

create table dept_emp (
	emp_no int not null,
	dept_no varchar(30) not null,
	from_date varchar(50) not null,
	to_date varchar(50) not null);

create table dept_manager (
	dept_no varchar(30) not null,
	emp_no int not null,
	from_date varchar(50) not null,
	to_date varchar(50) not null);

create table employees (
	emp_no int not null,
	birth_date varchar(50) not null,
	first_name varchar(250) not null,
	last_name varchar(250) not null,
	gender varchar(10) not null,
	hire_date varchar(50) not null);

create table salaries (
	emp_no int primary key not null,
	salary int,
	from_date varchar(50) not null,
	to_date varchar(50) not null);

create table titles (
	emp_no int not null,
	title varchar(30) not null,
	from_date varchar(50) not null,
	to_date varchar(50) not null);