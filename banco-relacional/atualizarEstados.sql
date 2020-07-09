-- Atualizações em banco de dados SEMPRE devem vir junto com o comando where
-- É necessário muito cuidado, pois sem o where, um comando pode alterar todo um banco de dados

update estados
set nome = 'Maranhão'
where sigla = 'MA'

select nome from estados where sigla = 'MA'

select 'nome' from estados where sigla = 'MA'

select estados.nome from estados where sigla = 'MA'

select est.nome from estados est where sigla = 'MA'

update estados
set
    nome = 'Paraná',
    populacao = 11.32
where sigla = 'PR'

select
    est.nome,
    sigla,
    populacao
from estados est
where sigla = 'PR'