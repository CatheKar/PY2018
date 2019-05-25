insert into programs values (1, 'математика и информационные технологии');
insert into programs values (2, 'теоретическая физика');

insert into courses values (1, 'электодинамика');
insert into courses values (2, 'механика жидкости и газа');
insert into courses values (3, 'теория групп');
insert into courses values (4, 'английский язык');	
insert into courses values (5, 'китайский язык');

insert into programs_courses values (1, 5, 1);
insert into programs_courses values (1, 1, 1);
insert into programs_courses values (1, 2, 2);
insert into programs_courses values (1, 4, 1);
insert into programs_courses values (1, 3, 2);

insert into marks values (1,1,5);
insert into marks values (2,2,3);
insert into marks values (2,3,5);
insert into marks values (1,5,4);
insert into marks values (1,4,5);

	


insert into students(program_id, card, surname, name) values(1, '180101', 'Битов', 'Антон');
insert into students(program_id, card, surname, name) values(2, '180201', 'Аргонова', 'Виолетта');
