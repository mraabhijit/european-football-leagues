select 
    m.away_team as team,
    count(m.match_id) as MP,
    count(case 
            when m.away_score > m.home_score 
            then 1 
            else null 
            end) 
            as W,
    count(case 
            when m.away_score < m.home_score 
            then 1 
            else null 
            end) 
            as L,
    count(case 
            when m.away_score = m.home_score 
            then 1 
            else null 
            end) 
            as D,
    sum(m.away_score) as GF,
    sum(m.home_score) as GA,
    sum(m.away_score - m.home_score) as GD
from {{ ref('stg_matches') }} as m
left join
{{ ref('stg_matches_info') }} as l
on m.match_id = l.match_id
group by 
    m.away_team
order by m.away_team