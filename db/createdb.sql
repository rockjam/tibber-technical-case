create sequence executions_id_seq;
create table executions (
    id int primary key default nextval('executions_id_seq'),
    "timestamp" timestamp not null default now(),
    commands int not null,
    result int not null,
    duration real not null
);
