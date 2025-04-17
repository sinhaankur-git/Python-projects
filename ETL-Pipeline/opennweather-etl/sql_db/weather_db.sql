create database weather_db;
use weather_db;

create table weather_data(
	id int primary key auto_increment,
    city varchar(100),
    temperature float,
    humidity int,
    weather varchar(100),
    wind_speed float,
    timestamp datetime
    );    

