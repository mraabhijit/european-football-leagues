WITH m1 AS (
    SELECT 
        m.match_id as match_id,
        m.home_team as home_team,
        m.away_team as away_team,
        m.home_score as home_score,
        m.away_score as away_score,
        i.league as league,
        i.matchday as matchday,
        i.match_date as match_date,
        i.match_referee as match_referee
    FROM {{ref('stg_matches')}} AS m
    LEFT JOIN {{ref('stg_matches_info')}} AS i
    ON m.match_id = i.match_id
)
SELECT 
    m1.home_team AS team,
    m1.league AS league,
    COUNT(m1.match_id) AS MP,
    SUM(CASE WHEN m1.home_score > m1.away_score THEN 1 ELSE 0 END) AS W,
    SUM(CASE WHEN m1.home_score < m1.away_score THEN 1 ELSE 0 END) AS L,
    SUM(CASE WHEN m1.home_score = m1.away_score THEN 1 ELSE 0 END) AS D,
    SUM(m1.home_score) AS GF,
    SUM(m1.away_score) AS GA,
    SUM(m1.home_score - m1.away_score) AS GD,
    SUM(CASE WHEN m1.home_score > m1.away_score THEN 3 
             WHEN m1.away_score = m1.home_score THEN 1 
             ELSE 0 END) AS P
FROM 
    m1
GROUP BY 
    m1.home_team, m1.league
ORDER BY 
    m1.league ASC,
    P DESC