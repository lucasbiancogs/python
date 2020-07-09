-- Vai haver uma relação entre empresa e cidade, porém essa relação estará em outr tabela

create table if not exists empresas (
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    cnpj int unsigned,
    primary key (id),
    unique key (cnpj)
);

-- Tabela NxN
create table if not exists empresas_unidades (
    empresa_id int unsigned not null,
    cidade_id int unsigned not null,
    sede tinyint(1) not null, -- número único, como se fosse booleano
    primary key (empresa_id, cidade_id)
);

-- Isso não foi incluso na aula mas acho bom incluir
alter table empresas_unidades 
    add foreign key (empresa_id) references empresas (id),
    add foreign key (cidade_id) references cidades (id)
