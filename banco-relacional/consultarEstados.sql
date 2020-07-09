-- Para executar, seleciona o bloco e utiliza ctrl+shift+E
select * from estados

select
    nome,
    sigla
from estados

select
    sigla,
    nome as 'Nome do Estado'
from estados
where regioes = 'Sul'

select
    sigla,
    nome as 'Nome do Estado'
from estados
where populacao >= 10
order by populacao

select
    sigla,
    nome as 'Nome do Estado',
    populacao
from estados
where populacao >= 10
order by populacao desc -- ele por padrão trás em ordem crescente, o desc faz em ordem decrescente