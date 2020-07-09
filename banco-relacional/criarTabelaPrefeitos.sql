-- Quando for modelar uma relação 1x1 é bom avaliar se realmente existe a necessidade
-- No caso do exemplo talvez não precisasse, poderia isso ser uma coluna de cidade, por exemplo
-- Isso pq é muito mais rápido uma busca em uma tabela única

create table if not exists prefeitos (
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    cidade_id int unsigned,
    primary key (id),
    unique key (cidade_id),
    foreign key (cidade_id) references cidades (id)
);