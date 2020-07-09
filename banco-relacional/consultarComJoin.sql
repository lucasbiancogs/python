-- Esse tipo de consulta não é interessante pois gera o produto cartesiano das duas tabelas
select * from estados e, cidades c

select * from estados e, cidades c
where e.id = c.estado_id;

-- uma linha por exemplo:
-- select nome from estados e, cidades c
-- gera conflito de ambiguidade

-- Outra questão é que no VSCode ele da problema com a exibição de nomes iguais
-- Por isso deve se colocar apelido
select
    e.nome as Estado,
    c.nome as Cidade,
    regioes as Região
from estados e, cidades c
where e.id = c.estado_id;

select
    c.nome as Cidade,
    e.nome as Estado,
    regioes as Região
from estados e
inner join cidades c
    on e.id = c.estado_id