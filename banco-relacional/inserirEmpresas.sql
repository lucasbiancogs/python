
-- Da problema dizendo que o int é muito grande
alter table empresas modify cnpj varchar(14);

insert into empresas
    (nome, cnpj)
values
    ('Bradesco', 95694186000132),
    ('Vale', 27283748293782),
    ('Cielo', 04738293047584);
-- Adiciona o número mesmo sem aspas, como um varchar

desc empresas;
desc prefeitos;
desc empresas_unidades;

select * from empresas;
select * from cidades;

insert into empresas_unidades
    (empresa_id, cidade_id, sede)
values
    (1, 3, 1),
    (1, 4, 0),
    (2, 3, 0),
    (2, 4, 1);
