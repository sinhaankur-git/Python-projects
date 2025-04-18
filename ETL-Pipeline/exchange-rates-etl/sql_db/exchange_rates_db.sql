create database exchange_rates_db;

use exchange_rates_db;
create table exchange_rates(
	id int auto_increment primary key,
    base_currency varchar(10),
    target_currency varchar(10),
    rate float,
    timestamp datetime,
    unique (base_currency, target_currency, timestamp)
    );


Select* from exchange_rates;