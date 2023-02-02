-- init 
-- depends: 
create table user (
	id integer primary key,
	name text not null
);

create table user_attr (
	id integer primary key,
	name text not null
);

create table user_attr_value (
	id integer primary key,
	user_id integer not null,
	attr_id integer not null,
	value text not null,

	foreign key (user_id) references user(id) on delete cascade,
	foreign key (attr_id) references user_attr(id) on delete cascade
);
