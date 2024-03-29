with 

source as (

    select * from {{ source('staging', 'matches') }}

),

renamed as (

    select
        match_id,
        home_team,
        away_team,
        home_score,
        away_score,
        -- home_team_points_earned,
        -- away_team_points_earned,
        -- home_team_gd,
        -- away_team_gd

    from source

)

select * from renamed
