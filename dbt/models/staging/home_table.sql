select 
    m.home_team as team,
    count(m.match_id) as MP,
    count(case 
            when m.home_score > m.away_score 
            then 1 
            else null 
            end) 
            as W,
    count(case 
            when m.home_score < m.away_score 
            then 1 
            else null 
            end) 
            as L,
    count(case 
            when m.home_score = m.away_score 
            then 1 
            else null 
            end) 
            as D,
    sum(m.home_score) as GF,
    sum(m.away_score) as GA,
    sum(m.home_score - m.away_score) as GD
from {{ ref('stg_matches') }} as m
left join
{{ ref('stg_matches_info') }} as l
on m.match_id = l.match_id
group by 
    m.home_team
order by m.home_team
