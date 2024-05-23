DROP TABLE IF EXISTS machine_log_count;

CREATE TABLE machine_log_count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    directory TEXT NULL,
    work_week int NOT NULL,
    machine_name varchar(60) NOT NULL,
    log_count int NOT NULL,
    log_type varchar(40)
);

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username varchar(60) NOT NULL,
    pwd varchar(60) NOT NULL,
    userrole varchar(60) not NULL
);


DROP TABLE IF EXISTS machine_activity;

CREATE TABLE machine_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    machine_name varchar(60) NOT NULL,
    current_work_week int NOT NULL,
    current_date Date NOT NULL,
    log_type varchar(40)
);