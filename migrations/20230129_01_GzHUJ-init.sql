-- init 
-- depends: 
create table player (
	id integer primary key,
	name text not null unique,
	ext_id integer not null unique
);

create table player_attr (
	id integer primary key,
	name text not null unique
);

create table player_attr_value (
	id integer primary key,
	player_id integer not null,
	attr_id integer not null,
	value text not null,

	unique(player_id, attr_id),
	foreign key (player_id) references player(id) on delete cascade,
	foreign key (attr_id) references player_attr(id) on delete cascade
);


insert into player_attr (name)
values
	('gold'),
	('wood'),
	('crystal'),
	('gemstone')
