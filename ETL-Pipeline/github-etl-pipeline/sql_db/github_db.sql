create database github_db;
use github_db;

-- github_users table

create table github_users(
	login varchar(100) primary key,
    name varchar(100),
    company varchar(100),    
    location varchar(100),
    followers int,
    public_repos int,
    created_at datetime
);

-- github_repos table

create table github_repos(
	id int auto_increment primary key,
    login varchar(100),
    repo_name varchar(100),
    description text,
    language varchar(100),
    stars int,
    forks int,
    updated_at datetime,
    foreign key (login) references github_users(login)
);

-- to verify the data
select* from github_users, github_repos;
