select * from estados where id = 19

insert into cidades (nome, area, estado_id)
values ('Campinas', 795, 25)

insert into cidades (nome, area, estado_id)
values ('Niteroi', 133.9, 19)

insert into cidades (nome, area, estado_id)
values (
    'Cararu',
    960.6,
    (select id from estados where sigla = 'PE')
)

insert into cidades
    (nome, area, estado_id)
values (
    'Juazeiro do Norte',
    248.2,
    (select id from estados where sigla = 'CE')
)

select * from cidades