select
    regioes as 'Região',
    sum(populacao) as Total
from estados
group by regioes
order by Total desc

select
    sum(populacao) as Total
from estados

select
    avg(populacao) as Total
from estados
