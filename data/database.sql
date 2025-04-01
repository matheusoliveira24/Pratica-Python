create database if not exists `agenda`

use `agenda`;

drop table if exists `tarefa`;

create table if not exists `tarefa` (
    `id` int not null auto_increment primary key,
    `titulo` char(60) not null,
    `data_conclusao` datetime null
);

