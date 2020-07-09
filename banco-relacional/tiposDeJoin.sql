-- Esse comando retorna a união de cidades e prefeitos onde existe correspondência de id
-- da cidade com a coluna foreign key de prefeitos, as duas que estão relacionadas
select
    c.id as id_c, c.nome as nome_c, area, estado_id,
    p.id as id_p, p.nome as nome_p, cidade_id
from cidades c inner join prefeitos p on c.id = p.cidade_id;

select * from prefeitos
select * from cidades

select
    c.id as id_c, c.nome as nome_c, area, estado_id,
    p.id as id_p, p.nome as nome_p, cidade_id
from cidades c left outer join prefeitos p on c.id = p.cidade_id;

select
    c.id as id_c, c.nome as nome_c, area, estado_id,
    p.id as id_p, p.nome as nome_p, cidade_id
from cidades c right join prefeitos p on c.id = p.cidade_id;

select
    c.id as id_c, c.nome as nome_c, area, estado_id,
    p.id as id_p, p.nome as nome_p, cidade_id
from cidades c left outer join prefeitos p on c.id = p.cidade_id
union
select
    c.id as id_c, c.nome as nome_c, area, estado_id,
    p.id as id_p, p.nome as nome_p, cidade_id
from cidades c right join prefeitos p on c.id = p.cidade_id;

