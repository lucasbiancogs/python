-- Criando a tabela estados

create table estados (
    id int unsigned not null auto_increment,
    nome varchar(45) not null,
    sigla varchar(2) not null,
    regioes enum('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul') not null,
    populacao DECIMAL(5, 2) not null,
    primary key (id),
    unique key (nome),
    unique key (sigla)
);